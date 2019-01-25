#import paho.mqtt.publish as publish
# 
#MQTT_SERVER = "172.17.0.0"
#MQTT_PATH = "sensordata"
 
#publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER)

#simulator device 1 for mqtt message publishing
import paho.mqtt.client as paho
import time
import random
#hostname
broker="192.16.0.60"
#port
port=1883
publisher = "sensordata"
def on_publish(client,userdata,result):
    print("Device 1 : Data published.")
    pass
client= paho.Client("admin")
client.on_publish = on_publish
client.connect(broker,port)
message="Device 1 : Data " + str(d)
ret= client.publish(MQTT_PATH,message)
print("Stopped..." +message)
