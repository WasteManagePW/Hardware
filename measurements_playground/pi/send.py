import json
from Whole_measure import distance
import pytz
import datetime
import paho.mqtt.client as mqtt
import time

def send(measurement):
    msg = {}
    msg['sensor_id'] = 1
    msg['value'] = measurement
    msg['timestamp'] = str(datetime.datetime.now(tz=pytz.utc))
    
    msg_str = json.dumps(msg)#encode

    client = mqtt.Client('us-015')
    client.connect('test.mosquitto.org')
    client.publish('main/test', msg_str)

if __name__ == '__main__':
    while True:
        send(distance())
        time.sleep(2)

