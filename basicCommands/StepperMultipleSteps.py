#!/usr/bin/python

import StepperOneStep
import os

def stepperMultipleSteps(howManySteps, stepPin, directionPin, directionValue, stepDelay):
    selfName = 'stepperMultiSteps'
    args = [howManySteps, stepPin, directionPin, directionValue, stepDelay]
    processData = ('; process id:' + str(os.getpid()))
    if hasattr(os, 'getppid'):
        processData = processData + ('; parent process:' + str(os.getppid()))
    print(str(selfName) + ' running with args: ' + str(args) + processData)
    for i in range(howManySteps):
        StepperOneStep.stepperOneStep(stepPin, directionPin, directionValue, stepDelay)

if __name__ == "__main__":
    stepperMultipleSteps(10, 1, 2, 0, 0.01)
