import socket
import threading as Thread
import time
from _thread import *
from multiprocessing import Process

print_lock = Thread.Lock()

# thread function
def createThread(c):
    while True:

        #data received from client
        data= c.recv(1024)
        data= data.decode('utf-8')
        print('Data Thread',data)
        if data == 'Vehicle':
            c.send(str.encode('OK'))
        elif data == 'hello':
            c.send(str.encode('hello'))
        elif data == 'KILL':
            c.send(str.encode('KILL'))
            
            break
        if not data:
            print('Connection Closed')

            #release lock
            
            break
        
        # Send data back to the client
        c.send(str.encode('Test'))
    
    c.close()

def controlThread(c):
    while True:

        #data received from client
        data= c.recv(1024)
        data= data.decode('utf-8')
        print('Control Thread', data)
        if data == 'ping':
            c.send(str.encode('Active'))
        elif data == 'ADD':
            c.send(str.encode('Booting Server'))
            
            break
        elif data == 'KILL':
            c.send(str.encode('Connection Closed'))
            
            break
        else:
            c.send(str.encode(data))
            continue
        # print(data)
        # if not data:
        #     print('Connection Closed')

            #release lock
        #     
        #     break
        
        # # Send data back to the client
        # c.send(str.encode('KILL'))
    
    c.close()

def data(sock):
    sock.listen(5)
    print("Socket listening on the port: sock")

    while True:

        # Establish Client connection
        connection, address= sock.accept()

        # Acquire client lock
        print_lock.acquire()
        print("Connected to : ", address[0], ':', address[1])

        p1= Process(target=createThread, args=(connection,))
        p1.start()

def control(control_sock):
    control_sock.listen(5)
    print("Socket listening on the port: Control Sock ")

    while True:
        control_connection, control_address= control_sock.accept()

        print_lock.acquire()
        print("Connected to : ", control_address[0], ':', control_address[1])

        p2=Process(target= controlThread, args=(control_connection,))
        p2.start()

def main():
    host='10.6.56.41'

    port=33000

    # Port that communicates with the central controller
    control_port= 33100

    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    control_sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.close()

    sock.bind((host,port))
    print('Socket bound to port: ', port)

    control_sock.bind((host,control_port))
    print('Control Socket bound to port: ', control_port)

    vehicle_listener= Process(target= data, args=(sock,))
    vehicle_listener.start()
    
    controller= Process(target= control, args=(control_sock,))
    controller.start()

    while True:
      try:
          time.sleep(10)
      except:
          break


if __name__ == '__main__':
    main()
    