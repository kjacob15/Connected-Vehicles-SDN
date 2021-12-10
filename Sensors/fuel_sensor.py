<<<<<<< HEAD
=======
#Udisha

>>>>>>> 41354dd5e7b90b3d74fcdd9ccd807d74787f0790
import socket
import time
import sys 
#import random
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
os.makedirs("logs/vehicle" + str(vehicle_number), exist_ok=True)
f = open("logs/vehicle" + str(vehicle_number) + "/fuel_sensor_logs.txt", "a")

f.write("\n")
f.write(str(datetime.now()) + "\n")
f.write("UDP target IP:" + signal_host + "\n")
f.write("UDP target port:" + str(signal_port) + "\n")

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP

fuel = 0.0 

while True:
    fuel = fuel + 0.5
    f.write(str(datetime.now()) + " Vehicle " + str(vehicle_number) + ", Sensor " + str(sensor_number) + " FUEL CONSUMED = " + str(fuel) + "%.\n")
    f.flush()
    x = str(fuel)
    sock.sendto(x.encode('utf-8'), (signal_host, signal_port))
    time.sleep(0.1)
    
    if(fuel == 0 or fuel < 0):
        fuel = 0.0 
        f.write(str(datetime.now()) + " Vehicle " + str(vehicle_number) + ", Sensor " + str(sensor_number) + " FUEL CONSUMED = " + str(fuel) + "%.\n")
        f.flush()
        x = str(fuel)
        sock.sendto(x.encode('utf-8'), (signal_host, signal_port))
        time.sleep(0.1)
    if(f == 100):
        break;

sock.close()
<<<<<<< HEAD
    
=======
    
>>>>>>> 41354dd5e7b90b3d74fcdd9ccd807d74787f0790
