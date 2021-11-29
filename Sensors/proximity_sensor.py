import socket
import time
import random
import sys

try:
    network_number = int(sys.argv[1])
    vehicle_number = int(sys.argv[2])
    sensor_number = int(sys.argv[3])
    signal_host = "10.35.70." + str(network_number)
    Signal_Port = 33000 + (10)*vehicle_number + sensor_number
except IndexError:
    print("Must provide three arguments: network number, vehicle number and sensor number.")
    exit()
except ValueError:
    print("The network number, vehicle number and sensor number must be valid integers.")
    exit()

print("UDP target IP:", Signal_host)
print("UDP target port:", Signal_Port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
prox = 3
while True:
    ran = random.random()
    if(ran < 0.5):
        prox = prox - 0.1
    else:
        prox = prox + 0.1
    n = str(min(prox, 3))
    time.sleep(0.1)
    sock.sendto(n.encode('utf-8'), (Signal_host, Signal_Port))
    print("Vehicle " + str(vehicle_number) + ", Sensor " + str(sensor_number) + " PROXIMITY = " + n + ".")

sock.close()