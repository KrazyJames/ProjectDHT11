import paho.mqtt.publish as publish
import time
MQTT_SERVER = "localhost"
#MQTT_SERVER= "mqtt.eclipse.org"
MQTT_PATH = "test_channel"
#st = ("DateTime " + time.strftime("%c"))
while True:
    st = ("DateTime " + time.strftime("%c"))
    publish.single(MQTT_PATH, st , qos=1, retain=False, hostname=MQTT_SERVER)
    publish.single("Temperatura", "20.4", qos=1, retain=False, hostname=MQTT_SERVER, client_id="Cliente1")
    publish.single("Humedad", "53%", hostname=MQTT_SERVER, client_id="Cliente2")
    publish.single("Clase_IoT", "Hola alumnos de Intro. al IoT", hostname=MQTT_SERVER, client_id="Cliente3")
    time.sleep(5) #duerme 60 segundos