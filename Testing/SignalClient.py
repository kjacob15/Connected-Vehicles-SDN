import socket

UDP_IP = "10.6.56.41"
UDP_PORT = 33007

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
sock.listen(2)
while True:
    conn, addr = sock.accept()
    data = conn.recvfrom(1024)  # buffer size is 1024 bytes
    data = data.decode('utf-8')
    print("received message: ", data)

sock.close()



