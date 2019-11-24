from paho.mqtt.client import Client

# import time
from DHT11 import DHT11

dht11 = DHT11()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        # global Connected  # Use global variable
        # Connected = True  # Signal connection
    else:
        print("Connection failed")


def on_message(client, userdata, message):
    m = message.payload.decode("utf-8")
    print('Message received:', m)
    if m == '1':
        print("Sending humidity...")
        client.publish("jaime.escobar.mtz@gmail.com/IoT/Teempo/hum", dht11.get_humidity())
        print("Humidity sent")
    elif m == '0':
        print("Sending temperature...")
        client.publish("jaime.escobar.mtz@gmail.com/IoT/Teempo/temp", dht11.get_temperature())
        print("Temperature sent")


# Connected = False  # global variable for the state of the connection

broker_address = "maqiatto.com"
user = "jaime.escobar.mtz@gmail.com"
password = "IoTGuaymas"

client = Client("Publicador")  # create new instance
client.username_pw_set(user, password=password)  # set username and password
client.on_connect = on_connect  # attach function to callback
client.connect(broker_address, port=1883)  # connect to broker
client.on_message = on_message  # attach function to callback
client.subscribe("jaime.escobar.mtz@gmail.com/IoT/Teempo/client")
client.loop_forever()
# client.loop_start()  # start the loop

# while not Connected:  # Wait for connection
#     time.sleep(0.1)
#
# try:
#     while True:
#         pass
#
# except KeyboardInterrupt:
#     client.disconnect()
#     client.loop_stop()
