#John

# import socket programming library
import socket

# import thread module
from _thread import *
import threading
import json

global iter_change
iter_change = 0

print_lock = threading.Lock()

global vehicle_info
vehicle_info = {}

# thread function


def threaded(c, address):
    global iter_change, vehicle_info
    while True:

        # data received from client
        data = c.recv(1024)
        data = data.replace("\'", "\"")
        print(data)
        try:
            data = json.loads(str(data))
            vehicle_info[data['vehicle_number']] = str(address)
        except:
            pass

        if not data:
            print('Bye')

            # lock released on exit
            # print_lock.release()
            break

        iter_change += 1
        if iter_change >= 50:
            c.send('CHANGE_OVER 4')
            #del vehicle_info[4]
        else:
            print('vehicle')
            c.send('CONTINUE '+str(json.dumps(vehicle_info)))

    # connection closed
    c.close()


threads = []


def Main():
    host = "10.35.70.1"

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 33133
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    try:
        while True:

            # establish connection with client
            c, addr = s.accept()

            # lock acquired by client
            # print_lock.acquire()
            t = threading.Thread(target=threaded, args=(c, addr[1]))
            t.start()
            threads.append(t)
            print('Connected to :', addr[0], ':', addr[1])
            #print('new thread started')
            # Start a new thread and return its identifier
            start_new_thread(threaded, (c, addr[1],))
            #print('while lopp ended')
    except KeyboardInterrupt:
        print('keyboard interrupt')
    finally:
        s.close()
        for i in threads:
            i.join()


if __name__ == '__main__':
    Main()
