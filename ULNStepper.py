# ULNStepper.py
from __future__ import print_function
import sys
import time
import RPi.GPIO as GPIO
import atexit

class ULNStepper():
    # Initliaze the ULN Driver stepper motor
    def __init__(self, in1=18, in2=27, in3=22, in4=23, direction=2):

        # Initialize GPIO mode to use GPIO pin numbers
        try:
            GPIO.setmode(GPIO.BCM)
        except Exception:
            t, e = sys.exc_info()[:2]
            print(e)

        # Setup GPIO such that all these pins are for OUTPUT only.
        self.StepPins = [in1, in2, in3, in4]
        for pin in self.StepPins:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin, False)

        # Define advanced sequence
        # as shown in manufacturers datasheet
        self.Seq = [[1,0,0,0],
                       [1,1,0,0],
                       [0,1,0,0],
                       [0,1,1,0],
                       [0,0,1,0],
                       [0,0,1,1],
                       [0,0,0,1],
                       [1,0,0,1]]
        self.StepCount = len(self.Seq)-1
        self.StepDir = direction

        self.StepCounter = 0

        def __del__(self):
                for pin in self.StepPins:
                    GPIO.output(pin, False)
                GPIO.cleanup()


    def takeOneStep(self):
        for pin in range(0, 4):
            xpin = self.StepPins[pin]
            if self.Seq[self.StepCounter][pin]!=0:
              GPIO.output(xpin, True)
            else:
              GPIO.output(xpin, False)

        self.StepCounter += self.StepDir
        if (self.StepCounter >= self.StepCount):
            self.StepCounter = 0
        if (self.StepCounter < 0):
            self.StepCounter = self.StepCount

        # From experiements the ideal time for sleeping is twice the amount of time taken for one step.
        time.sleep(0.0025)

    def takeSteps(self, N):
        for i in range(0,N):
            self.takeOneStep()
