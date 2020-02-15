import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from busio import I2C
import time
import board

class FurnaceSwitch:
    def __init__(self):
        GPIO.setwarnings(True) # Ignore warning for now
        # GPIO.setmode(GPIO.BCM) # Use OTHER (not physical) pin numbering
        
    def setupWith(self, pinNumber):
        self.pinNumber = pinNumber
        GPIO.setup(pinNumber, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pinNumber, GPIO.BOTH, callback=self.event_callback)

    def event_callback(self, channel):
        if GPIO.input(self.pinNumber):  # if port 25 == 1  
            print("Rising edge detected on " + str(self.pinNumber))
        else:                  # if port 25 != 1  
            print("Falling edge detected on " + str(self.pinNumber))

    # def readAndPrint(self):
    #     message = input("Press enter to quit\n\n") # Run until someone presses enter
