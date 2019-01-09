#from sqlalchemy import create_engine

#engine = create_engine('sqlite:///:memory:', echo=True)

import json
import sys
import datetime
import time
import socket

if len(sys.argv) < 3:
    print('Usage: python3 {} [measurments] [id_czujnik]'.format(sys.argv[0]))
    quit()

ip = '127.0.0.1'
port = 9999
addr = (ip, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = {}
msg['id'] = int(sys.argv[1])
msg['measurments'] = float(sys.argv[2])
msg['czas_pomiaru'] = str(datetime.date.today())
#msg['time'] = time.strftime('%H:%M:%S')
msg['id_czujnik'] = sys.argv[3]

msg_str = json.dumps(msg).encode('utf-8')
print(msg_str)
sock.sendto(msg_str, addr)
print("Send!")