#Eerste deepbot actie script listener 28-01-3019

#KEEP this scipt running
#nohup python /home/pismurf/mqqt//mqqt/deebot_subscriber.py &

import paho.mqtt.client as mqtt

MQTT_SERVER = "192.168.0.60"
MQTT_PATH = "deebot"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Deebot Connected (code "+str(rc)+")")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    print("Suscribing to be able to start Deebot")
    client.subscribe(MQTT_PATH)

    
	
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    action =str(msg.payload)
    print(msg.topic+" "+action)
    decider = {
	"stop": print ("--> sending IR command to Dock Bot"),
	"start": print ("--> sending IR command to vaccuum")
	}
    decider.get(action,"A clue, No")
	# more callbacks, etc
client = mqtt.Client("script")
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER,1883,60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
