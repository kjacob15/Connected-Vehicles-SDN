import socket
import errno
import threading as Thread
from _thread import *
import time
from multiprocessing import Process
# print_lock = Thread.Lock()

# thread function
host = 'rasp-001.berry.scss.tcd.ie'

def createThread(c):
    while True:
    
        #data received from client
        data= c.recv(1024)
        data= data.decode('utf-8')
        print('Failover Data Thread',data)
        if data == 'Vehicle':
            c.send(str.encode('OK'))
        elif data == 'hello':
            c.send(str.encode('hello'))
        elif data == 'KILL':
            c.send(str.encode('KILL'))
            c.close()
            break
        elif not data:
            print('Connection Closed')                   
            break
        else:
            c.send(str.encode(data))
    c.close()


def controlThread(c):
    while True:

        # data received from client
        data = c.recv(1024)
        data = data.decode('utf-8')
        if data == 'ping':
            c.send(str.encode('Active'))
        elif data == 'ADD':
            c.send(str.encode('Booting Server'))
            
            break
        elif data == 'KILL':
            c.send(str.encode('Connection Closed'))
            c.close()
            break
        else:
            continue
    c.close()

def actingController():
    #Define Port
    port=33000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind((host, port))
    print('Socket bound to port: ', port)

    vehicle_listener= Process(target= data, args=(sock,))
    vehicle_listener.start()

    while True:
        try:
            time.sleep(10)
        except:
            break


def data(sock):
    print("Vehicle socket initialized")
    sock.listen(5)
    print("Vehicle socket listening")

    while True:

        # Establish Client connection
        connection, address= sock.accept()
        
        print("Connected to : ", address[0], ':', address[1])

        p1= Process(target=createThread, args=(connection,))
        p1.start()


def ping(control_sock):
    print("Pinging Server")
    while True:
        command = input("Enter your Command: ")
        if command == 'EXIT':
            control_sock.send(str.encode(command))
            break
        elif command == 'KILL':
            control_sock.send(str.encode(command))
            reply = control_sock.recv(1024)
            print(reply.decode('utf-8'))
            if reply.decode('utf-8') == 'Failover':
                control_sock.close()
                time.sleep(3)                
                actingController()
                break                
            break
        control_sock.send(str.encode(command))
        reply = control_sock.recv(1024)
        print(reply.decode('utf-8'))
        if reply.decode('utf-8') == 'KILL':
            break
        if reply.decode('utf-8') == 'Failover':
            time.sleep(2)
            control_sock.close()
            actingController()
            break     
    control_sock.close()


def main():

    # Port that communicates with the central controller
    control_port = 33100
    global control_sock
    control_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    control_sock.settimeout(5)

    #Talk to main Central Controller
    control_sock.connect((host, control_port))

    print('Control Socket connected to port: ', control_port)

    ping(control_sock)

    # p1= Process(target= data, args=(sock,))
    # p1.start()

    # p= Process(target= ping, args=(control_sock,))
    # p.start()

    # p= Process(target= data, args=(sock,))
    # p.start()

    # while True:
    #     try:
    #         time.sleep(10)
    #     except:
    #         break

    # control_sock.listen(5)
    # print("Socket listening on the port: ", control_port)

# def data(sock):
#     sock.listen(5)
#     print("Socket listening on the port: sock")

#     while True:

#         # Establish Client connection
#         connection, address= sock.accept()

#         # Acquire client lock

#         print("Connected to : ", address[0], ':', address[1])

#         p1= Process(target=createThread, args=(connection,))
#         p1.start()

#     while True:

#         # Establish Client connection
#         connection, address = sock.accept()

#         # Acquire client lock
#         #
#         print("Connected to : ", address[0], ':', address[1])

#         p = Process(target=ping, args=(control_sock,))
#         p.start()
#         p.join()

#         # f=Process(ping, (control_sock,))
#         # f.start()
#         # f.join()
#         # start_new_thread(ping, (control_sock,))


if __name__ == '__main__':
    main()
