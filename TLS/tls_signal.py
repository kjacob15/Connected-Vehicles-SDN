#Kevin

import socket
import time

#signal_host = "127.0.0.1"
signal_host = "10.35.70.1"
signal_port = 55001
msg = "STOP"

print("UDP target IP:", signal_host)
print("UDP target port:", signal_port)
# print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
try:
    while True:
        # conn, addr = sock.accept()
        if msg == "STOP":
            msg="GO"
        else:
            msg = "STOP"
        time.sleep(10)
        sock.sendto(msg.encode('utf-8'), (signal_host, signal_port))
        print("message:", msg)
        print("Message sent")
except KeyboardInterrupt:
    sock.close()