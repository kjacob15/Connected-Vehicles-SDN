import socket

UDP_IP = "10.35.70.2"
UDP_Port = 33005
MESSAGE = "Hello, World!"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_Port)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_Port))
print("Message sent")