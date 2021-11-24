import socket
#import time
import sys 
import random

try:
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    signal_port = 33000 + 10*arg1 + arg2

except IndexError:
    print("Must provide two arguments: the vehicle number and the sensor number")
    exit()
except ValueError:
    print("The vehicle number and the sensor number must be valid integers.")
    exit()

signal_host = "10.6.56.41"

print("UDP target IP:", signal_host)
print("UDP target port:", signal_port)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP


s = 0
#while True:
    # incrementing speed
i = 5
for i in range(random.randint(1,9)): 
    s = s + 5 * i
    if(s > 80):
        break
    else :
        print("Speed of the vehicle " + str(arg1) + " " + str(s) + " km/h.--")

# stopping the car 
#d = 10
while(s > 0):
    if(s > 80):
        s =  s - 20
        continue
    s =  s - 20
    if(s < 0 ):
        s = 0    
    print("Speed of the vehicle " + str(arg1) + " " + str(s) + " km/h.")
    
sock.close()