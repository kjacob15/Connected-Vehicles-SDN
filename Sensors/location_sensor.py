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
    sock.sendto(n.encode('utf-8'), (Signal_host, Signal_Port))
    print("Vehicle " + str(vehicle_number) + ", Sensor " + str(sensor_number) + " LOCATION = " + n + ".")

sock.close()