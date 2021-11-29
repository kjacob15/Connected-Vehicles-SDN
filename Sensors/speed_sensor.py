import socket
import time
import sys 
import random
import os
from datetime import datetime

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

os.makedirs("logs", exist_ok=True)
f = open("logs/fuel_sensor_logs.txt", "a")

f.write("\n")
f.write(str(datetime.now()) + "\n")
f.write("UDP target IP:" + signal_host + "\n")
f.write("UDP target port:" + str(signal_port) + "\n")

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP

s = 0.0
while True:
    # incrementing speed

    for i in range(random.randint(1,9)): 
        s = s + 5.2 * i
        if(s > 80):
            break
        else :
            f.write(str(datetime.now()) + "Vehicle " + str(vehicle_number) + ", Sensor " + str(sensor_number) + " SPEED = " + str(s) + " km/h.\n")
            f.flush()
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
        f.write(str(datetime.now()) + "Vehicle " + str(vehicle_number) + ", Sensor " + str(sensor_number) + " SPEED = " + str(s) + " km/h.\n")
        f.flush()
        x = str(s)
        sock.sendto(x.encode('utf-8'), (signal_host, signal_port))
        time.sleep(0.1)
sock.close()