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

locationX = 0
locationY = 0
while True:
    locationX = locationX = locationX + 0.0001
    n = str((locationX, locationY))
    time.sleep(0.1)
    sock.sendto(n, (Signal_host, Signal_Port))
    print("Vehicle " + str(arg1) + ", Sensor " + str(arg2) + " LOCATION = " + n + ".")

sock.close()