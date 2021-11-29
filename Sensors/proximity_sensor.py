import socket
import time
import random
import sys

try:
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    Signal_Port = 33000 + (10)*arg1 + arg2
except IndexError:
    print("Must provide two arguments: the vehicle number and the sensor number.")
    exit()
except ValueError:
    print("The vehicle number and the sensor number must be valid integers.")
    exit()

Signal_host = "10.35.70.2"

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
    print("Vehicle " + str(arg1) + ", Sensor " + str(arg2) + " PROXIMITY = " + n + ".")

sock.close()