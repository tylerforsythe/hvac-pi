from busio import I2C
import adafruit_bme680
import time
import board

class AirSensor:
    def __init__(self):
        #global i2c
        #global bme680
        # Create library object using our Bus I2C port
        self._i2c = I2C(board.SCL, board.SDA)
        self._bme680 = adafruit_bme680.Adafruit_BME680_I2C(self._i2c)

        # change this to match the location's pressure (hPa) at sea level
        self._bme680.sea_level_pressure = 1013.25


    def readAndPrint(self):
        return
        print("Temperature: %0.1f C" % self._bme680.temperature)
        print("Gas: %d ohm" % self._bme680.gas)
        print("Humidity: %0.1f %%" % self._bme680.humidity)
        print("Pressure: %0.3f hPa" % self._bme680.pressure)
        print("Altitude = %0.2f meters" % self._bme680.altitude)
        # print("\n")
