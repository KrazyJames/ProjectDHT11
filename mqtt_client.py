import time

import paho.mqtt.client as mqtt_client


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection
    else:
        print('Connection failed')


# Cuando recibe el mensaje, imprime
def on_message(client, userdata, message):
    print('Message received:', message.payload.decode("utf-8"))


Connected = False  # global variable for the state of the connection

broker_address = "localhost"  # Broker address, local host
user = "user1"  # Connection username
password = "1234"  # Connection password

client = mqtt_client.Client("Cliente")  # create new instance
client.username_pw_set(user, password=password)  # set username and password
client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback

client.connect(broker_address)  # connect to broker

client.loop_start()  # start the loop

while not Connected:  # Wait for connection
    time.sleep(0.1)

client.subscribe("python/test")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print('exiting')
    client.disconnect()
    client.loop_stop()
