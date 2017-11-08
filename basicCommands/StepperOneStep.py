#!/usr/bin/python

import sys
import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

def stepperOneStep(stepPin, directionPin, directionValue, stepDelay):
    selfName = 'stepperOneStep'
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(stepPin     , GPIO.OUT)
    GPIO.setup(directionPin, GPIO.OUT)

    GPIO.output(directionPin, directionValue)
    GPIO.output(stepPin, GPIO.LOW)
    time.sleep(stepDelay)
    GPIO.output(stepPin, GPIO.HIGH)
    time.sleep(stepDelay)
    args = [stepPin, directionPin, directionValue, stepDelay]
    print(str(selfName) + ' running with args: ' + str(args))

if __name__ == "__main__":
    stepperOneStep(1, 2, 0, 0.01)

# if __name__ == "__main__":
#     selfName = 'stepperOneStep'
#     expectedArgsAmount = 4
#     if(len(sys.argv) < expectedArgsAmount):
#         print(str(selfName) + 'got ' + str(len(sys.argv)) + 'args instead of ' + str(expectedArgsAmount))
#     stepperOneStep(stepPin, directionPin, directionValue, stepDelay)
