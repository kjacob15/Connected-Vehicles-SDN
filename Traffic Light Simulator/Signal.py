import socket
import time

try:
    network_number = int(sys.argv[1])
    Signal_host = "10.35.70." + str(network_number)
except IndexError:
    print("Must provide one arguments: the network number.")
    exit()
except ValueError:
    print("The network number must be a valid integer.")
    exit()

Signal_Port = 33007
msg = "STOP"

print("UDP target IP:", Signal_host)
print("UDP target port:", Signal_Port)
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
        sock.sendto(msg.encode('utf-8'), (Signal_host, Signal_Port))
        print("message:", msg)
        print("Message sent")
except KeyboardInterrupt:
    sock.close()