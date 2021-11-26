import socket
import time
import sys 
from threading import Thread
from queue import Queue

UDP_IP = "10.35.70.2"

#main Thread
def handle_client(
    front_proximity_sensor_port, right_proximity_sensor_port, back_proximity_sensor_port, left_proximity_sensor_port, 
        location_sensor_port, speed_sensor_port, fuel_sensor_port):
    # t=[]
    print("Starting Thread")
    #data, addr = socket.recvfrom(1024)  # buffer size is 1024 bytes
    #data = data.decode('utf-8')
    #print("received message: ", data)

    t1= Thread(target=frontProxClient, args=(front_proximity_sensor_port,))
    t2= Thread(target=rightProxClient, args=(right_proximity_sensor_port,))
    t3= Thread(target=backProxClient,  args=(back_proximity_sensor_port,))
    t4= Thread(target=leftProxClient, args=(left_proximity_sensor_port,))
    t5= Thread(target=locationClient, args=(location_sensor_port,))
    t6= Thread(target=speedClient, args=(speed_sensor_port,))
    t7= Thread(target=fuelClient, args=(fuel_sensor_port,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()


def frontProxClient(port):
    print("Started frontProxClient")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port)) 
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data = data.decode('utf-8')
        print("Received message from FRONT PROXIMITY SENSOR: ", data)

def rightProxClient(port):
    print("Started rightProxClient")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data = data.decode('utf-8')
        print("Received message from RIGHT PROXIMITY SENSOR: ", data)    

def backProxClient(port):
    print("Started backProxClient")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))    
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data = data.decode('utf-8')
        print("Received message from BACK PROXIMITY SENSOR: ", data)

def leftProxClient(port):
    print("Started leftProxClient")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))  
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data = data.decode('utf-8')
        print("Received message from LEFT PROXIMITY SENSOR: ", data)

def locationClient(port):
    print("Started locationClient")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))    
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data = data.decode('utf-8')
        print("Received message from LOCATION SENSOR: ", data)

def speedClient(port):
    print("Started speedClient")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))    
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data = data.decode('utf-8')
        print("Received message from SPEED SENSOR: ", data)

def fuelClient(port):
    print("Started fuelClient")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    sock.bind((UDP_IP, port))   
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data = data.decode('utf-8')
        print("Received message from FUEL SENSOR: ", data)

threads = []
queue = Queue()

try:
    arg1 = int(sys.argv[1])
    front_proximity_sensor_port = 33000 + (10)*arg1 + 1
    right_proximity_sensor_port = 33000 + (10)*arg1 + 2
    back_proximity_sensor_port = 33000 + (10)*arg1 + 3
    left_proximity_sensor_port = 33000 + (10)*arg1 + 4
    location_sensor_port = 33000 + (10)*arg1 + 5
    speed_sensor_port = 33000 + (10)*arg1 + 6
    fuel_sensor_port = 33000 + (10)*arg1 + 7
    global mainThread
    mainThread= Thread(
        target=handle_client, 
        args=(
            front_proximity_sensor_port, right_proximity_sensor_port, back_proximity_sensor_port, left_proximity_sensor_port,
            location_sensor_port, speed_sensor_port, fuel_sensor_port
        )
    )
    #time.sleep(7)
    mainThread.start()
except IndexError:
    print("Must provide one argument: the vehicle number.")
    exit()
except ValueError:
    print("The vehicle number must be a valid integer.")
    exit()

