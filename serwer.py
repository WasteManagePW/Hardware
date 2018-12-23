# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:20:17 2018

@author: finwe
"""


#!/usr/bin/env python3

import socket
import statistics
from wasteLib import waste_objects
import pickle
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
wyniki = [0] * 10
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        i = 0
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(b'Received')
            data_var = pickle.loads(data)
            
print(data_var.levels)
print(statistics.median(data_var.levels))
print(data_var.errors)
print(data_var.battery)