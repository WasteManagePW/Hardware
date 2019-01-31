import json
from Whole_measure import distance
import datetime
import paho.mqtt.client as mqtt

def send(measurement):
    msg = {}
    msg['sensor_id'] = 1
    msg['measurement'] = measurement
    msg['timestamp'] = str(datetime.datetime.now())
    
    msg_str = json.dumps(msg)#encode

    client = mqtt.Client('us-015')
    client.connect('test.mosquitto.org')
    client.publish('main/test', msg_str)

if __name__ == '__main__':
    send(distance())

