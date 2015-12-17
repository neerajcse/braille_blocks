from SquareWheelBrailleStepper import BrailleStepper, BrailleWheel
from BinaryCharacterSet import BinaryCharacterSetMapper
from BrailleUtils import BrailleEmbosser
from HeadhHorizontalCarriage import HeadhHorizontalCarriage

import sys
import time
import threading
import traceback



def changeStepperState(stepperMotor, toChar, charSet, side, readyEvent):
    tb=""
    try:
        print("Changing stepper motor state to " + toChar)
        toState = charSet.getConfig(side, toChar)
        stepperMotor.goToState(toState)
    except Exception, e:
        tb=traceback.format_exc()
        print("Oops something weird happened. %s" % e)
    finally:
        print tb
        readyEvent.set()
        print("Ready event triggered for " + "left" if side == 0 else "right")

def punchBraille(leftStepperReady, rightStepperReady, brailleEmbosser):
    leftStepperReady.wait()
    rightStepperReady.wait()
    brailleEmbosser.emboss()


wheel = BrailleWheel()
leftStepper = BrailleStepper(brailleWheel=wheel, onPort=[18,23,24,25])
rightStepper = BrailleStepper(brailleWheel=wheel, onPort=[4,17,27,22])
brailleEmbosser = BrailleEmbosser(pin=21)
carriage = HeadhHorizontalCarriage(port=13)

left_motor_thread = threading.Thread()
right_motor_thread = threading.Thread()
BINARY_charSet = BinaryCharacterSetMapper()


while(True):
    user_command = str(raw_input("Input next character. Type 'exit' to stop:"))
    if user_command=="exit":
        break
    else:
        leftStepperReady = threading.Event()
        rightStepperReady = threading.Event()
        if not left_motor_thread.isAlive():
            left_motor_thread = threading.Thread(target=changeStepperState, args=(leftStepper, str(user_command), BINARY_charSet, 0,leftStepperReady,))
            left_motor_thread.start()
        if not right_motor_thread.isAlive():
            right_motor_thread = threading.Thread(target=changeStepperState, args=(rightStepper, str(user_command), BINARY_charSet, 1, rightStepperReady,))
            right_motor_thread.start()
        punchBraille(leftStepperReady, rightStepperReady, brailleEmbosser)
        carriage.goToNextStep()
    time.sleep(1)
