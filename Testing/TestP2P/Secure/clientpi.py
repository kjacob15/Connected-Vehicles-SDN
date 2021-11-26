import socket
from time import sleep

host = 'rasp-002.berry.scss.tcd.ie'
port = 33005


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


while True:
    command= input("Enter your Command: ")
    if command == 'EXIT':
        s.send(str.encode(command))
        break
    elif command == 'KILL':
        s.send(str.encode(command))
        break
    s.send(str.encode(command))
    reply= s.recv(1024)
    print(reply.decode('utf-8'))
s.close()
