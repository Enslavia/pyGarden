#!/usr/bin/python

import StepperMultipleSteps
from math import pi
from multiprocessing import Process

def moveToPosition(start, finish, axisLenghts, stepperWheelsR, stepsPerRevolution, stepPins, directionPins, directionValues, stepDelays):
    selfName = 'moveToPosition'
    args = [start, finish, axisLenghts, stepperWheelsR, stepsPerRevolution, stepPins, directionPins, directionValues, stepDelays]
    print(str(selfName) + ' running with args: ' + str(args))
    oneStepLenghts = list()
    for i in range(3):
        oneStepLenghts.append(2 * pi * stepperWheelsR[i] / stepsPerRevolution[i])
    print(oneStepLenghts)
    stepAmounts = list()
    directions  = list()
    for i in range(3):
        stepAmounts.append(int((finish[i] - start[i]) // oneStepLenghts[i]))
        dir = directionValues[i]
        if finish[i] < start[i]:
            dir = int(not dir)
        directions .append(dir)
    print(stepAmounts)
    print(directions)
    processStepperX = Process()
    processStepperY = Process()
    processStepperZ = Process()
    stepperProcesses = {0 : processStepperX, 1: processStepperY, 2 : processStepperZ}
    for i in stepperProcesses.values():
        i.start()
        i.join()
    for i in stepperProcesses.keys():
        stepperProcesses[i] = Process(target=StepperMultipleSteps.stepperMultipleSteps, args=(stepAmounts[i], stepPins[i], directionPins[i], directions[i], stepDelays[i]))
        stepperProcesses[i].start()
    for i in stepperProcesses.values():
        i.join()
        print('joined ' + str(i))

if __name__ == "__main__":
    start               = [1, 2, 3]
    finish              = [100, 200, 300]
    axisLenghts         = [1000, 2000, 3000]
    stepperWheelsR      = [50, 50, 50]
    stepsPerRevolution  = [200, 200, 200]
    stepPins            = [1, 2, 3]
    directionPins       = [4, 5, 6]
    directionValues     = [0, 0, 1]
    stepDelays          = [0.005, 0.005, 0.005]
    moveToPosition(start, finish, axisLenghts, stepperWheelsR, stepsPerRevolution, stepPins, directionPins, directionValues, stepDelays)


# def stepperMultipleSteps(howManySteps, stepPin, directionPin, directionValue, stepDelay):
