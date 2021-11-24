import socket

UDP_IP = "10.35.70.2"
UDP_PORT = 33005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
print("Socket created.")
try:
    sock.bind((UDP_IP, UDP_PORT))
    print("Socket bind comlete.")
except socket.error as msg:
    print(msg)
    print("Socket bind failed.")

print("Debugging point 1")
cond= 2
# sock.listen(2)
while cond>0:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    data = data.decode('utf-8')
    print("received message: ", data)
    cond= 0

sock.close()



