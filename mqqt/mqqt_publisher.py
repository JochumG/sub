import paho.mqtt.publish as publish

MQTT_SERVER = "192.168.0.60"
MQTT_PATH = "sensordata"
 
publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER)
print("Stopped...")
