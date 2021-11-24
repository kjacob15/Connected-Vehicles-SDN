import socket
import time

Signal_host = "10.6.56.41"
Signal_Port = 33007
MESSAGE = "STOP"

print("UDP target IP:", Signal_host)
print("UDP target port:", Signal_Port)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
while True:
    # conn, addr = sock.accept()
    if MESSAGE == "STOP":
        MESSAGE="GO"
    else:
        MESSAGE == "STOP"
    time.sleep(6)
    sock.sendto(MESSAGE.encode('utf-8'), (Signal_host, Signal_Port))
    print("Message sent")

sock.close()