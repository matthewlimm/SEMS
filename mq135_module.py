# from guizero import App, Box, Text, TextBox, PushButton, ButtonGroup, MenuBar, info, yesno, warn
# from time import sleep
# from subprocess import call 
# import RPi.GPIO as GPIO
# import busio
# import digitalio
# import board
# import adafruit_mcp3xxx.mcp3008 as MCP
# from adafruit_mcp3xxx.analog_in import AnalogIn
import random

# # Create the SPI bus
# spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# # Create the cs (chip select)
# cs = digitalio.DigitalInOut(board.D22)
# # Create the mcp object
# mcp = MCP.MCP3008(spi, cs)
# # Create analog inputs connected to the input pins on the MCP3008.
# channel_0 = AnalogIn(mcp, MCP.P0)

class MQ135Module:
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id
    
    def get_sensor_readings(self):
        def _range(x, in_min, in_max, out_min, out_max):
            return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
            
        while True:
            # Test your module, then define the value range - in this case between 0 and 60000.
            # sensorValue = _range(channel_0.value, 0, 60000, 0, 1023)
            # print("AQI:", sensorValue)
            #return sensorValue
            return random.randint(1,100)