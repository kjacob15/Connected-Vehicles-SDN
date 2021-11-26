import time
import datetime
import socket
from threading import Thread
from queue import Queue

UDP_IP = "10.6.56.41"
UDP_PORT = 33007

# tracking = time.time()
# print(tracking)
maxSpeed= 70
speed=0
threads = []
queue = Queue()


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
print("Socket created.")
try:
    sock.bind((UDP_IP, UDP_PORT))
    print("Socket bind comlete.")
except socket.error as msg:
    print(msg)
    print("Socket bind failed.")


#main Thread
def handle_client(socket):
    # t=[]
    print("Starting Thread")
    data, addr = socket.recvfrom(1024)  # buffer size is 1024 bytes
    data = data.decode('utf-8')
    print("received message: ", data)

    t= Thread(target=move)
    if data == "GO":       
        t.start()
    else:
        global speed
        t.setDaemon= True
        t= Thread(target=halt, args=(speed,))
        t.start()
    
    threads.append(t)

    
def move():
    global speed
    for x in range(0,120,5):
        print("Speed = ", x)
        time.sleep(1)
        speed=x
        if x >= maxSpeed:
            slowDown(x)

def slowDown(x):
    print("---Slowing Down")
    global speed
    speed=x
    for y in range (x,maxSpeed-20, -5):
        print("Slowing Speed = ", y)
        time.sleep(1)
        speed=y
    speedup(speed)

def speedup(s):
    print("Accelerating--->")
    global speed
    speed=s
    for k in range (s,maxSpeed+10,5):
        print("Acc Speed = ", k)
        time.sleep(1)
        speed=k
        if speed >= maxSpeed:
            slowDown(speed)    

def halt(s):
    print("Braking!")
    for j in range (s,0, -10):
        print("Braking Speed = ", j)

try:   
    while True:
        global mainThread
        mainThread= Thread(target=handle_client, args=(sock,))
        time.sleep(7)
        mainThread.start()
except KeyboardInterrupt:
    sock.close()