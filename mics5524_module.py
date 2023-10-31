import adafruit_dht
import time

adc0 = MCP3008(channel=0)

class MICS5524Module:
    def get_sensor_readings(self):
        while True:
            try:
                print(adc0.value)

            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                print(error.args[0])
                time.sleep(2.0)
                continue
            except Exception as error:
                self.dht_device.exit()
                raise error
