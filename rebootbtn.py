import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from busio import I2C
import time
import board

class RebootButton:
    def __init__(self):
        GPIO.setwarnings(True) # Ignore warning for now

        
    def setupWith(self, pinNumber):
        self.pinNumber = pinNumber
        # GPIO.setmode(GPIO.BCM) # Use OTHER (not physical) pin numbering
        GPIO.setup(pinNumber, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
        GPIO.add_event_detect(pinNumber, GPIO.RISING, callback=self.button_callback) # Setup event on pin 10 rising edge

    def button_callback(self, channel):
        if GPIO.input(self.pinNumber):
            print("Button was pushed!")

    # def readAndPrint(self):
    #     message = input("Press enter to quit\n\n") # Run until someone presses enter
