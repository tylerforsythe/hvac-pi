import airsensor
from rebootbtn import RebootButton
from timer import Timer
import threading
import queue
import time

def read_kbd_input(inputQueue):
    print('Ready for keyboard input:')
    while (True):
        input_str = input()
        inputQueue.put(input_str)

def main():
    print ("beginning main start")

    EXIT_COMMAND = "exit"
    inputQueue = queue.Queue()

    inputThread = threading.Thread(target=read_kbd_input, args=(inputQueue,), daemon=True)
    inputThread.start()

    logTimer = Timer("air_log")
    logTimer.start(2)

    rebootCheck = RebootButton()
    airSensor = airsensor.AirSensor()

    while (True):
        if (inputQueue.qsize() > 0):
            input_str = inputQueue.get()
            print("input_str = {}".format(input_str))

            if (input_str == EXIT_COMMAND):
                print("Exiting serial terminal.")
                break
            
            # Insert your code here to do whatever else you want with the input_str.

        # The rest of your program goes here.
        if logTimer.hasElapsed():
            airSensor.readAndPrint()

        time.sleep(0.01)

    print("End.")


if __name__ == "__main__":
    main()


# Create a loop that runs while a variable is true
# every iteration of the loop, check a sequence of timers:
# timer for logging temperature sensor values to file
# timer for checking for button presses
# timer for checking relay inputs
# each time a tiner elapses for the specified amount, run a piece of processing code for it