#John & Jack

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

global data_fp, data_bp, data_rp, data_lp, data_loc, data_speed, data_fuel, data_voltage,vehicle_number
data_fp, data_rp, data_bp, data_lp, data_loc, data_speed, data_fuel, data_voltage = '', '', '', '', '', '', '', ''

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
    f.write("Starting Thread\n")
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
    f.write("Started frontProxClient\n")
    f.flush()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_fp = data.decode('utf-8')
        f.write(str(datetime.now()) + " Received message from FRONT PROXIMITY SENSOR: " + str(data_fp) + "\n")
        f.flush()

def rightProxClient(port):
    global data_rp
    f.write("Started rightProxClient\n")
    f.flush()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_rp = data.decode('utf-8')
        f.write(str(datetime.now()) + " Received message from RIGHT PROXIMITY SENSOR: " + str(data_rp) + "\n")
        f.flush()

def backProxClient(port):
    global data_bp
    f.write("Started backProxClient\n")
    f.flush()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_bp = data.decode('utf-8')
        f.write(str(datetime.now()) + " Received message from BACK PROXIMITY SENSOR: " + str(data_bp) + "\n")
        f.flush()

def leftProxClient(port):
    global data_lp
    f.write("Started leftProxClient\n")
    f.flush
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_lp = data.decode('utf-8')
        f.write(str(datetime.now()) + " Received message from LEFT PROXIMITY SENSOR: " + str(data_lp) + "\n")
        f.flush()

def locationClient(port):
    global data_loc
    f.write("Started locationClient\n")
    f.flush()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_loc = data.decode('utf-8')
        f.write(str(datetime.now()) + " Received message from LOCATION SENSOR: " + str(data_loc) + "\n")
        f.flush()

def speedClient(port):
    global data_speed
    f.write("Started speedClient\n")
    f.flush()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(100)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_speed = data.decode('utf-8')
        f.write(str(datetime.now()) + " Received message from SPEED SENSOR: " + str(data_speed) + "\n")
        f.flush()

def fuelClient(port):
    global data_fuel
    f.write("Started fuelClient\n")
    f.flush()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(5)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_fuel = data.decode('utf-8')
        f.write(str(datetime.now()) + " Received message from FUEL SENSOR: " + str(data_fuel) + "\n")
        f.flush()

def voltageClient(port):
    global data_voltage
    f.write("Started voltageClient\n")
    f.flush()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    sock.settimeout(5)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_voltage = data.decode('utf-8')
        f.write(str(datetime.now()) + " Received message from VOLTAGE SENSOR: " + str(data_voltage) + "\n")
        f.flush()

def updateCentralControl():
    global data_fp,data_lp,data_rp,data_bp,data_loc,data_speed,data_fuel,vehicle_number
    check = ''
    flag = True
    with lock:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        invalid = True
        while invalid:
            try:
                print('trying- success')
                invalid = False
                s.connect(('10.35.70.1',33133))
            except:
                invalid = True
        try:
            for i in range(15):
                time.sleep(5)
                s.sendall(str(json.dumps({'vehicle_number':vehicle_number,'data':[
    {'front_prox':data_fp,'back_prox':data_bp,'right_prox':data_rp,'left_prox':data_lp,
    'speed':data_speed,'loc':data_loc,'fuel':data_fuel}]})).encode())
                check_data = s.recv(1024).decode()
                check = str(check_data.split(' ',1)[0])
                check_data = check_data.split(' ',1)[1:]
                print(check)
                try:
                            same_network_vehicles = json.loads(check_data[0])
                            print(same_network_vehicles)
                except:
                        pass
                if check == 'CONTINUE':
                    #print(str(s.recv(1024)))
                    print('continue')
                    pass
                elif check == 'CHANGE_OVER':
                    if check_data==str(vehicle_number) or True:
                        print('change over detected'+str(vehicle_number))
                        s.close()
                        invalid=True
                        while invalid:
                            try:
                                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                                invalid = False
                                s.connect(('10.35.70.2',33133))
                            except:
                                invalid = True
                        print('change over detected')
                else:
                    break
        except Exception as e:
            print('send fail',str(e))
        print('send')
        # print(str(s.recv(1024)))
        s.close()



def Main():
    global vehicle_number
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
        os.makedirs("logs", exist_ok=True)
        os.makedirs("logs/vehicle" + str(vehicle_number), exist_ok=True)
        global f
        f = open("logs/vehicle" + str(vehicle_number) + "/vehicle_logs.txt", "a")

        f.write("\n")
        f.write(str(datetime.now()) + "\n")
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
