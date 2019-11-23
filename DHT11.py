from time import sleep as sleepy

import serial as serial


# For Linux
# port = "/dev/ttyACM0"

class DHT11:

    def __init__(self):
        self.temp = 0
        self.hum = 0
        self.port = "com5"

    def get_temperature(self):
        arduinouno = serial.Serial(self.port, 9600, timeout=5)
        sleepy(5)
        arduinouno.write(b'0')
        sleepy(5)
        temp = arduinouno.readline().decode("utf-8").strip()
        self.temp = temp
        return self.temp

    def get_humidity(self):
        arduinouno = serial.Serial(self.port, 9600, timeout=5)
        sleepy(5)
        arduinouno.write(b'1')
        sleepy(5)
        hum = arduinouno.readline().decode("utf-8").strip()
        self.hum = hum
        return self.hum
