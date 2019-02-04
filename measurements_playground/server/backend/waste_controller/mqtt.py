import paho.mqtt.client as mqtt #import the client1
import time
import json
import os
import logging
logging.basicConfig(level=logging.DEBUG)

def on_connect(client, userdata, flags, rc):
    client.subscribe("main/test")
    print('connected')

def on_subscribe(client, userdata, mid, granted_qos):
    print('subscribed')

def on_message(client, userdata, msg):
    from . import models
    print("message received ", str(msg.payload.decode("utf-8")))
    msg = json.loads(str(msg.payload.decode("utf-8")))

    s = models.Sensor.objects.get(pk=msg['sensor_id'])
    m = s.measurement_set.create(value=msg['value'], timestamp=msg['timestamp'])
    #m = models.Measurement(sensor_id=msg['sensor_id'], value=msg['value'], timestamp=msg['timestamp'])
    print(m)

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', '../backend.settings')
client = mqtt.Client("elo")
logger = logging.getLogger(__name__)
client.enable_logger(logger)
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message

    #client.connect("test.mosquitto.org")
client.connect("iot.eclipse.org")
#client.loop_forever()
