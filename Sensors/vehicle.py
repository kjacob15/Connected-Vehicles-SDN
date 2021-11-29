import socket
import time
import sys
from threading import Thread
import json
import threading

lock = threading.Lock()

UDP_IP = ""
Network_Controller= ""

global data_fp, data_bp, data_rp, data_lp, data_loc, data_speed, data_fuel
data_fp, data_rp, data_bp, data_lp, data_loc, data_speed, data_fuel = '', '', '', '', '', '', ''

# with lock:
#	port = 33000
#	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#	sock.connect((UDP_IP,port))
#	sock.send('TEST'.encode('ascii'))

# main Thread


def handle_client(
    front_proximity_sensor_port, right_proximity_sensor_port, back_proximity_sensor_port, left_proximity_sensor_port,
        location_sensor_port, speed_sensor_port, fuel_sensor_port):
    # t=[]
    print("Starting Thread")
    # data, addr = socket.recvfrom(1024)  # buffer size is 1024 bytes
    #data = data.decode('utf-8')
    #print("received message: ", data)

    t1 = Thread(target=frontProxClient, args=(front_proximity_sensor_port,))
    t2 = Thread(target=rightProxClient, args=(right_proximity_sensor_port,))
    t3 = Thread(target=backProxClient,  args=(back_proximity_sensor_port,))
    t4 = Thread(target=leftProxClient, args=(left_proximity_sensor_port,))
    t5 = Thread(target=locationClient, args=(location_sensor_port,))
    t6 = Thread(target=speedClient, args=(speed_sensor_port,))
    t7= Thread(target=fuelClient, args=(fuel_sensor_port,speed_sensor_port))

    threads = [t1, t2, t3, t4, t5, t6, t7]

    for i in threads:
        i.start()


def frontProxClient(port):
    global data_fp
    print("Started frontProxClient")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_fp = data.decode('utf-8')
        print("Received message from FRONT PROXIMITY SENSOR: ", data_fp)


def rightProxClient(port):
    global data_rp
    print("Started rightProxClient")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_rp = data.decode('utf-8')
        print("Received message from RIGHT PROXIMITY SENSOR: ", data_rp)


def backProxClient(port):
    global data_bp
    print("Started backProxClient")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_bp = data.decode('utf-8')
        print("Received message from BACK PROXIMITY SENSOR: ", data_bp)


def leftProxClient(port):
    global data_lp
    print("Started leftProxClient")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_lp = data.decode('utf-8')
        print("Received message from LEFT PROXIMITY SENSOR: ", data_lp)


def locationClient(port):
    global data_loc
    print("Started locationClient")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_loc = data.decode('utf-8')
        print("Received message from LOCATION SENSOR: ", data_loc)

def speedClient(port):
    global data_speed
    print("Started speedClient")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_speed = data.decode('utf-8')
        print("Received message from SPEED SENSOR: ", data_speed)

def fuelClient(port,speed_port):
    global data_fuel
    print("Started fuelClient")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port)) 
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock2.bind(UDP_IP,speed_port)
    sock.settimeout(5) 

    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_fuel = data.decode('utf-8')
        print("Received message from FUEL SENSOR: ", data_fuel)
        if(data_fuel == "FUEL"):
            x = "FUEL"
            sock2.sendto(x.encode('utf-8'), (UDP_IP, speed_port))

def updateCentralControl():
    global data_fp, data_lp, data_rp_data_bp, data_loc, data_speed, data_fuel
    with lock:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        invalid = True
        while invalid:
            try:
                #print('trying- success')
                invalid = False
                s.connect((UDP_IP, 33000))
            except:
                invalid = True
        try:
            for i in range(10):
                time.sleep(10)
                s.sendall(str(json.dumps({'vehicle_number': '4', 'data': [
                    {'front_prox': data_fp, 'back_prox': data_bp, 'right_prox': data_rp, 'left_prox': data_lp,
                     'speed': data_speed, 'loc': data_loc, 'fuel': data_fuel}]})).encode())
        except:
            print('send fail')
        print('send')
        print(str(s.recv(1024)))
        s.close()


def Main():
    try:
        network_number = int(sys.argv[1])
        vehicle_number = int(sys.argv[2])
        UDP_IP = "10.35.70." + str(network_number)
        front_proximity_sensor_port = 33000 + (10)*vehicle_number + 1
        right_proximity_sensor_port = 33000 + (10)*vehicle_number + 2
        back_proximity_sensor_port = 33000 + (10)*vehicle_number + 3
        left_proximity_sensor_port = 33000 + (10)*vehicle_number + 4
        location_sensor_port = 33000 + (10)*vehicle_number + 5
        speed_sensor_port = 33000 + (10)*vehicle_number + 6
        fuel_sensor_port = 33000 + (10)*vehicle_number + 7
        global mainThread
        mainThread = Thread(
            target=handle_client,
            args=(
                front_proximity_sensor_port, right_proximity_sensor_port, back_proximity_sensor_port, left_proximity_sensor_port,
                location_sensor_port, speed_sensor_port, fuel_sensor_port
            )
        )
        # time.sleep(7)
        mainThread.start()
        updateCentralControl()
    except IndexError:
        print("Must provide one argument: the vehicle number.")
        exit()
    except ValueError:
        print("The vehicle number must be a valid integer.")
        exit()
    except KeyboardInterrupt:
        print('keyboard interrupt')
        exit()


if __name__ == '__main__':
    Main()
