from time import sleep as sleepy

import serial as serial

port = "/dev/ttyACM0"
arduino = serial.Serial(port, 9600, timeout=5)
sleepy(5)


class DHT11:

    def __init__(self, temp, hum):
        self.temp = temp
        self.hum = hum

    def getTemperature(self):
        arduino.write(b'0')
        sleepy(5)
        temp = arduino.readline()
        temp = temp.decode("utf-8")
        self.temp = temp
        return self.temp

    def getHumidity(self):
        arduino.write(b'1')
        sleepy(5)
        hum = arduino.readline()
        hum = hum.decode("utf-8")
        self.hum = hum
        return self.hum
