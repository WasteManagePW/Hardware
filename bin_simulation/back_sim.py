import socket
import json
from measurement import Measurement
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://test:1234@localhost/maciej', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 9999)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)


while True:
    print('Waiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(len(data), address))

    if data:
        msg = json.loads(data.decode('utf-8'))
        print(msg)
        m = Measurement(id=msg['id'], id_czujnik=msg['id_czujnik'], czas_pomiaru=msg['czas_pomiaru'], measurments=msg['measurments'])
        print(m)
        session.add(m)
        session.commit()