import socket
import time
import sys 
import random

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

s = 0.0
while True:
    # incrementing speed

    for i in range(random.randint(1,9)): 
        s = s + 5.2 * i
        if(s > 80):
            break
        else :
            print("Vehicle " + str(vehicle_number) + ", Sensor " + str(sensor_number) + " SPEED = " + str(s) + " km/h.")
            x = str(s)
            sock.sendto(x.encode('utf-8'), (signal_host, signal_port))
            time.sleep(0.1)
    # stopping the car 
    #d = 10
    while(s > 0.0):
        if(s > 80):
            s =  s - 20
            continue
        s =  s - 20
        if(s < 0.0 ):
            s = 0.0    
        print("Vehicle " + str(vehicle_number) + ", Sensor " + str(sensor_number) + " SPEED = " + str(s) + " km/h.")
        x = str(s)
        sock.sendto(x.encode('utf-8'), (signal_host, signal_port))
        time.sleep(0.1)
sock.close()