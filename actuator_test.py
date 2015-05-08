from BrailleStepper import BrailleStepper, BrailleWheel
from CharacterSets import EnglishCharacterSet

import sys
import time
import threading


def changeStepperState(stepperMotor, toChar, charSet, side):
	try:
		toState = charSet.getConfig(side, toChar)
		stepperMotor.goToState(toState)
	except:
		print("Oops something weird happened." + sys.last_value)


wheel = BrailleWheel()
leftStepper = BrailleStepper(brailleWheel=wheel)

left_motor_thread = threading.Thread()
EN_charSet = EnglishCharacterSet()


while(True):
	user_command = input("Input next character. Type 'exit' to stop:")
	if user_command=="exit":
		break
	else:
		if not left_motor_thread.isAlive():
			left_motor_thread = threading.Thread(target=changeStepperState, args=(leftStepper, user_command, EN_charSet, 0))
			left_motor_thread.start()
	time.sleep(1)