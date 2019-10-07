import paho.mqtt.client as mqtt
import time

print ("running v0.12")

# mqtt specifics
MQTT_HOST = "mosquitto"
MQTT_PORT = 1883
MQTT_TOPIC = "test_topic"

# connection event
def on_connect(client, data, flags, rc):
    if rc==0:
         print("connected OK")
         client.subscribe(MQTT_TOPIC)
    else:
        print("Bad connection:", str(rc))

# received message event
def on_message(client, data, msg):
    print("Received topic:", str(msg.topic))
    current_time = time.time()
    filename = "face_" + str(current_time) + ".jpg"
    with open(filename, "wb") as f:
        print("Writing: ", filename)
        #f.write(cv2.imdecode(msg.payload))
        f.write(msg.payload)
        f.close()

# create MQTT client
client = mqtt.Client()

# assign event callbacks
client.on_connect = on_connect
client.on_message = on_message

# client connection
client.connect(MQTT_HOST, MQTT_PORT, 60)

# start loop
client.loop_forever()

