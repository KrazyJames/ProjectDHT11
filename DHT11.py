from time import sleep as sleepy
import serial as serial

# For Linux uncomment line below
# port = "/dev/ttyACM0"

# Windows
port = "COM5"
arduinouno = serial.Serial(port, 9600, timeout=5)

class DHT11:

    def __init__(self):
        self.arduino = arduinouno
        self.temp = 0
        self.hum = 0

    def get_temperature(self):
        self.arduino = arduinouno
        self.arduino.write(b'0')
        sleepy(5)
        temp = self.arduino.readline()
        temp = temp.decode("utf-8")
        self.temp = temp
        return self.temp

    def get_humidity(self):
        self.arduino = arduinouno
        self.arduino.write(b'1')
        sleepy(5)
        hum = self.arduino.readline().decode("utf-8").strip()
        self.hum = hum
        return self.hum
