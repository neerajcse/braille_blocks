from BrailleStepper import BrailleStepper, BrailleWheel
from CharacterSets import EnglishCharacterSet

import sys
import time
import threading
import traceback


def changeStepperState(stepperMotor, toChar, charSet, side):
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


wheel = BrailleWheel()
leftStepper = BrailleStepper(brailleWheel=wheel)

left_motor_thread = threading.Thread()
EN_charSet = EnglishCharacterSet()


while(True):
	user_command = str(raw_input("Input next character. Type 'exit' to stop:"))
	if user_command=="exit":
		break
	else:
		if not left_motor_thread.isAlive():
			left_motor_thread = threading.Thread(target=changeStepperState, args=(leftStepper, str(user_command), EN_charSet, 0,))
			left_motor_thread.start()
	time.sleep(1)
