import time

import paho.mqtt.client as mqtt_client  # Libreria para mqtt de Paho, se instala aparte


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection
    else:
        print("Connection failed")


Connected = False  # global variable for the state of the connection

broker_address = "localhost"
user = "user1"
password = "1234"

client = mqtt_client.Client("Publicador")  # create new instance
client.username_pw_set(user, password=password)  # set username and password
client.on_connect = on_connect  # attach function to callback
client.connect(broker_address)  # connect to broker

client.loop_start()  # start the loop

while not Connected:  # Wait for connection
    time.sleep(0.1)

try:
    while True:
        value = input('Enter the message:')
        client.publish("python/test", value)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
