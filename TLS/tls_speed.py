#Udisha

from ctypes import DEFAULT_MODE
import socket
import time
import sys 
import random
from threading import Thread

try:
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    #signal_port = 33000 + 10*arg1 + arg2

except IndexError:
    print("Must provide two arguments: the vehicle number and the sensor number")
    exit()
except ValueError:
    print("The vehicle number and the sensor number must be valid integers.")
    exit()

#signal_host = "127.0.0.1"
signal_host = "10.35.70.1"
signal_port = 55001
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP
print("Socket created.")

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
        print("Vehicle " + str(arg1) + ", Sensor " + str(arg2) + " SPEED = " + str(i) + " km/h.")
        time.sleep(0.2)
        speed = i
        if(i >= max_speed):
            slowdown(i)
            #x = str(s)
            #sock.sendto(x.encode('utf-8'), (signal_host, signal_port))
    exit()    

def slowdown(s):
    global speed
    print("Slowing Down----------->")
    for j in range (s, max_speed-20, -random.randint(8,10)):
        print("Vehicle " + str(arg1) + ", Sensor " + str(arg2) + " SPEED = " + str(j) + " km/h.")
        time.sleep(0.2)
        speed = j
    speedup(speed)
    exit()


def speedup(s):
    global speed
    print("Accelerating-------------->")
    for k in range (s, max_speed+10, random.randint(8,10)):
        print("Vehicle " + str(arg1) + ", Sensor " + str(arg2) + " SPEED = " + str(k) + " km/h.")
        time.sleep(0.2)
        speed = k
        #x = str(s)
        #sock.sendto(x.encode('utf-8'), (signal_host, signal_port))
        
    
def stop(s):
    global speed
    print("Braking!!!!!!!!!Braking!!!!!!!!Braking!!!!!!!")
    for j in range (s,-1, -random.randint(8,10)):
        print("Vehicle " + str(arg1) + ", Sensor " + str(arg2) + " SPEED = " + str(j) + " km/h.")
        #x = str(s)
        #sock.sendto(x.encode('utf-8'), (signal_host, signal_port))
    print("Vehicle " + str(arg1) + ", Sensor " + str(arg2) + " SPEED = "  + "0 km/h.")
    speed = 0

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