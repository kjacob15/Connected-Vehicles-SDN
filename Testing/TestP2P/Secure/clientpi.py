import socket
from time import sleep

host = 'rasp-001.berry.scss.tcd.ie'
# host= '10.6.56.41'
port = 33000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


while True:
    command= input("Enter your Command: ")
    if command == 'EXIT':
        s.send(str.encode(command))
        break
    elif command == 'KILL':
        s.send(str.encode(command))
        reply= s.recv(1024)
        print(reply.decode('utf-8'))
        if reply.decode('utf-8') == 'KILL':
            s.close()
            break
        break
    else:
        s.send(str.encode(command))
    reply= s.recv(1024)
    print(reply.decode('utf-8'))
    if reply.decode('utf-8') == 'KILL':
        s.close()
        break
