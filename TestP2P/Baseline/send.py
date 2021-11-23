import socket

UDP_IP = "10.35.70.2"
UDP_Port = 33005
MESSAGE = "Hello, World- This is a socket connection!"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_Port)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # UDP
conn, addr = sock.accept()
conn.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_Port))
print("Message sent")

sock.close()