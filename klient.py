# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:20:54 2018

@author: finwe
"""

#!/usr/bin/env python3
from wasteLib import waste_objects
import socket
import random
import time
import pickle
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
n = 10
signal = waste_objects.update([0]*n, random.randint(10, 90))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    for i in range(n):
        signal.levels[i] = random.randint(50, 70)
        time.sleep(0.1)
    ran = random.randint(1, 10)
    if ran == 1:
        signal.errors.append("Signal malfunction")
    ran = random.randint(1, 10)
    if ran <= 2:
        signal.errors.append("Sensor malfunction")
    ran = random.randint(1, 10)
    if ran <= 3:
        signal.errors.append("Cables malfunction")
    data_string = pickle.dumps(signal)
    s.send(data_string)
    data = s.recv(1024)

print('Received', repr(data))