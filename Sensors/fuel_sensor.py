import socket
import time
import sys 
#import random


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

f = 0.0 


try :
    while True:
        f = f + 0.5
        print("Vehicle " + str(vehicle_number) + ", Sensor " + str(sensor_number) + " FUEL CONSUMED = " + str(f) + "%.")
        #x = str(f)
        #sock.sendto(x.encode('utf-8'), (signal_host, signal_port))
        time.sleep(0.1)
        if(f == 0 or f < 0):
            f = 0.0 
            print("Vehicle " + str(vehicle_number) + ", Sensor " + str(sensor_number) + " FUEL CONSUMED = " + str(f) + "%.")
            x = str(f)
            sock.sendto(x.encode('utf-8'), (signal_host, signal_port))
        
        if(f == 100):
            x = "FUEL"
            sock.sendto(x.encode('utf-8'), (signal_host, signal_port))
            f = 0.0
            time.sleep(5)
except :
    sock.close()