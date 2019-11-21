import time

import paho.mqtt.client as mqtt  # Libreria para mqtt de Paho, se instala aparte
import serial as serial

port = "/dev/ttyACM0"
arduino = serial.Serial(port, 9600, timeout=5)
time.sleep(5)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection
    else:
        print("Connection failed")


def on_message(userdata, message):
    # TO DO how you handle data you requested
    m = message.payload.decode("utf-8")
    print('Message received:', m)



Connected = False  # global variable for the state of the connection

broker_address = "192.168.43.94"
user = "user1"
password = "1234"

client = mqtt.Client("Publicador")  # create new instance
client.username_pw_set(user, password=password)  # set username and password
client.on_connect = on_connect  # attach function to callback
client.connect(broker_address)  # connect to broker
client.on_message = on_message

client.loop_start()  # start the loop

while not Connected:  # Wait for connection
    time.sleep(0.1)

try:
    while True:
        # TO DO your stuff here
        print('Enviando temp')
        arduino.write(b'0')
        time.sleep(5)
        temp = arduino.readline()
        temp = temp.decode("utf-8")
        temp = temp.strip()
        print(temp)
        client.publish("python/temp", temp)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
