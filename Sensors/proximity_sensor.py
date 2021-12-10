<<<<<<< HEAD
=======
#Jack

>>>>>>> 41354dd5e7b90b3d74fcdd9ccd807d74787f0790
import socket
import time
import random
import sys
import os
from datetime import datetime

try:
    network_number = int(sys.argv[1])
    vehicle_number = int(sys.argv[2])
    sensor_number = int(sys.argv[3])
    Signal_host = "10.35.70." + str(network_number)
    Signal_Port = 33000 + (10)*vehicle_number + sensor_number
except IndexError:
    print("Must provide three arguments: network number, vehicle number and sensor number.")
    exit()
except ValueError:
    print("The network number, vehicle number and sensor number must be valid integers.")
    exit()

os.makedirs("logs", exist_ok=True)
os.makedirs("logs/vehicle" + str(vehicle_number), exist_ok=True)
f = open("logs/vehicle" + str(vehicle_number) + "/proximity_sensor_" + str(sensor_number) + "_logs.txt", "a")

f.write("\n")
f.write(str(datetime.now()) + "\n")
f.write("UDP target IP:" + Signal_host + "\n")
f.write("UDP target port:" + str(Signal_Port) + "\n")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
prox = 3
while True:
    ran = random.random()
    if(ran < 0.5):
        prox = prox - 0.1
    else:
        prox = prox + 0.1
    n = str(min(max(prox, 0), 3))
    time.sleep(0.1)
    sock.sendto(n.encode('utf-8'), (Signal_host, Signal_Port))
    f.write(str(datetime.now()) + " Vehicle " + str(vehicle_number) + ", Sensor " + str(sensor_number) + " PROXIMITY = " + n + "." + "\n")
    f.flush()

sock.close()
f.close()