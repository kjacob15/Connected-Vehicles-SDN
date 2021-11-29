from ctypes import DEFAULT_MODE
import socket
import time
import sys 
import random
from threading import Thread

try:
    network_number = int(sys.argv[1])
    vehicle_number = int(sys.argv[2])
    sensor_number = int(sys.argv[3])
    signal_host = "10.35.70." + str(network_number)
    signal_port = 33000 + 10*vehicle_number + sensor_number

except IndexError:
    print("Must provide three arguments: network number, vehicle number and sensor number.")
    exit()
except ValueError:
    print("The network number, vehicle number and sensor number must be valid integers.")
    exit()

print("UDP target IP:", signal_host)
print("UDP target port:", signal_port)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP

try:
    sock.bind((signal_host, signal_port))
    print("Socket bind complete.")
except socket.error as msg:
    print(msg)
    print("Socket bind failed.")

speed = 0
max_speed = 70
threads = []

def move(): 
    global speed
    for i in range(0,150, random.randint(8,10)): 
        print("Vehicle " + str(vehicle_number) + ", Sensor " + str(sensor_number) + " SPEED = " + str(i) + " km/h.")
        x = str(i)
        sock.sendto(x.encode('utf-8'), (signal_host, signal_port))
        time.sleep(0.2)
        speed = i
        if(i >= max_speed):
            slowdown(i)
            
    exit()    

def slowdown(s):
    global speed
    print("Slowing Down----------->")
    for j in range (s, max_speed-20, -random.randint(8,10)):
        print("Vehicle " + str(vehicle_number) + ", Sensor " + str(sensor_number) + " SPEED = " + str(j) + " km/h.")
        x = str(j)
        sock.sendto(x.encode('utf-8'), (signal_host, signal_port))
        time.sleep(0.2)
        speed = j
    speedup(speed)
    exit()
            
def speedup(s):
    global speed
    print("Accelerating-------------->")
    for k in range (s, max_speed+10, random.randint(8,10)):
        print("Vehicle " + str(vehicle_number) + ", Sensor " + str(sensor_number) + " SPEED = " + str(k) + " km/h.")
        x = str(k)
        sock.sendto(x.encode('utf-8'), (signal_host, signal_port))
        time.sleep(0.2)
        speed = k
        #x = str(s)
        #sock.sendto(x.encode('utf-8'), (signal_host, signal_port))

def stop(s):
    global speed
    print("Braking!!!!!!!!!Braking!!!!!!!!Braking!!!!!!!")
    for j in range (s,-1, -random.randint(8,10)):
        print("Vehicle " + str(vehicle_number) + ", Sensor " + str(sensor_number) + " SPEED = " + str(j) + " km/h.")
        x = str(j)
        sock.sendto(x.encode('utf-8'), (signal_host, signal_port))
    print("Vehicle " + str(vehicle_number) + ", Sensor " + str(sensor_number) + " SPEED = "  + "0 km/h.")
    speed = 0
    x = str(speed)
    sock.sendto(x.encode('utf-8'), (signal_host, signal_port))

def fuel_refill():
    global speed
    stop(speed)
    print("WAIT FUEL REFILLING ---------- WAIT FUEL REFILLING -----------WAIT FUEL REFILLING")

#def handle_client(socket):

    #print("Starting Thread")
    
    
    #threads.append(t)

try:
    while True:  
        #t = []  
        time.sleep(4)
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data = data.decode('utf-8')
        print("received message: ------------------------------------", data)
        if data == "FUEL":
            t = Thread(target = fuel_refill)   
            t.start()
            time.sleep(1)
        elif data == "GO":   
            t = Thread(target=move)    
            t.start()
        else :
            t = Thread(target = stop, args=(speed,))  
            t.start()  

except KeyboardInterrupt:
    sock.close()