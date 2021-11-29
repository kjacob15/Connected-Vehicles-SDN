import socket
import time
import sys
from threading import Thread
import json
import threading
import os
from datetime import datetime

lock = threading.Lock()

UDP_IP = ""
Network_Controller= ""

global data_fp, data_bp, data_rp, data_lp, data_loc, data_speed, data_fuel, data_voltage
data_fp, data_rp, data_bp, data_lp, data_loc, data_speed, data_fuel, data_voltage = '', '', '', '', '', '', '', ''

os.makedirs("logs", exist_ok=True)
f = open("logs/vehicle_logs.txt", "a")

f.write("\n")
f.write(str(datetime.now()) + "\n")

# with lock:
#	port = 33000
#	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#	sock.connect((UDP_IP,port))
#	sock.send('TEST'.encode('ascii'))

# main Thread


def handle_client(
    front_proximity_sensor_port, right_proximity_sensor_port, back_proximity_sensor_port, left_proximity_sensor_port,
        location_sensor_port, speed_sensor_port, fuel_sensor_port, voltage_sensor_port):
    # t=[]
    f.write("Starting Thread")
    f.flush()
    # data, addr = socket.recvfrom(1024)  # buffer size is 1024 bytes
    #data = data.decode('utf-8')
    #print("received message: ", data)

    t1 = Thread(target=frontProxClient, args=(front_proximity_sensor_port,))
    t2 = Thread(target=rightProxClient, args=(right_proximity_sensor_port,))
    t3 = Thread(target=backProxClient,  args=(back_proximity_sensor_port,))
    t4 = Thread(target=leftProxClient, args=(left_proximity_sensor_port,))
    t5 = Thread(target=locationClient, args=(location_sensor_port,))
    t6 = Thread(target=speedClient, args=(speed_sensor_port,))
    t7 = Thread(target=fuelClient, args=(fuel_sensor_port,))
    t8 = Thread(target=voltageClient, args=(voltage_sensor_port,))

    threads = [t1, t2, t3, t4, t5, t6, t7, t8]

    for i in threads:
        i.start()


def frontProxClient(port):
    global data_fp
    f.write("Started frontProxClient")
    f.flush()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_fp = data.decode('utf-8')
        f.write("Received message from FRONT PROXIMITY SENSOR: " + str(data_fp))
        f.flush()

def rightProxClient(port):
    global data_rp
    f.write("Started rightProxClient")
    f.flush()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_rp = data.decode('utf-8')
        f.write("Received message from RIGHT PROXIMITY SENSOR: " + str(data_rp))
        f.flush()

def backProxClient(port):
    global data_bp
    f.write("Started backProxClient")
    f.flush()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_bp = data.decode('utf-8')
        f.write("Received message from BACK PROXIMITY SENSOR: " + str(data_bp))
        f.flush()

def leftProxClient(port):
    global data_lp
    f.write("Started leftProxClient")
    f.flush
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_lp = data.decode('utf-8')
        f.write("Received message from LEFT PROXIMITY SENSOR: " + str(data_lp))
        f.flush()

def locationClient(port):
    global data_loc
    f.write("Started locationClient")
    f.flush()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_loc = data.decode('utf-8')
        f.write("Received message from LOCATION SENSOR: " + str(data_loc))
        f.flush()

def speedClient(port):
    global data_speed
    f.write("Started speedClient")
    f.flush()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_speed = data.decode('utf-8')
        f.write("Received message from SPEED SENSOR: " + str(data_speed))
        f.flush()

def fuelClient(port):
    global data_fuel
    f.write("Started fuelClient")
    f.flush()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(5)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_fuel = data.decode('utf-8')
        f.write("Received message from FUEL SENSOR: " + str(data_fuel))
        f.flush()

def voltageClient(port):
    global data_voltage
    f.write("Started voltageClient")
    f.flush()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(5)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_voltage = data.decode('utf-8')
        f.write("Received message from VOLTAGE SENSOR: " + str(data_voltage))
        f.flush()

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
            f.write('send fail')
            f.flush()
        f.write('send')
        f.write(str(s.recv(1024)))
        f.flush()
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
        voltage_sensor_port = 33000 + (10)*vehicle_number + 8
        global mainThread
        mainThread = Thread(
            target=handle_client,
            args=(
                front_proximity_sensor_port, right_proximity_sensor_port, back_proximity_sensor_port, left_proximity_sensor_port,
                location_sensor_port, speed_sensor_port, fuel_sensor_port, voltage_sensor_port
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
