import threading

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

class MotorStates():
	NO_PINS_000 = 0
	ONE_PIN_001 = 1
	ONE_PIN_010 = 2
	TWO_PIN_011 = 3
	ONE_PIN_100 = 4
	TWO_PIN_101 = 5
	TWO_PIN_110 = 6
	THR_PIN_111 = 7

class BrailleWheel():
	CONFIGURATION = [
						MotorStates.NO_PINS_000,
						MotorStates.THR_PIN_111, 
						MotorStates.ONE_PIN_010,
						MotorStates.ONE_PIN_100,
						MotorStates.TWO_PIN_110,
						MotorStates.TWO_PIN_101,
						MotorStates.ONE_PIN_001,
						MotorStates.TWO_PIN_011,
					]

class BrailleStepper(threading.Thread):

	def __init__(self, stesPerRev, onPort, atI2CAddress,
		side, brailleWheel, debug=True):
		# hardware related config
		self.motorHAT = Adafruit_MotorHAT()
		self.stepper = self.motorHAT.getStepper(stesPerRev, onPort)
		self.stepper.setSpeed(15)
		
		# motor related config
		self.STEPS_FOR_45_DEGREES = 509.5
		
		# state related config (the state of where the motor is currently)
		self.leftOverFromLastStep = 0
		self.state = MotorStates.NO_PINS_000

		# the configuration of the braille wheel that is connected to the motor.
		self.config = brailleWheel.CONFIGURATION
		

	def goToState(self, toState):
		currentIndex = self.config.index(self.state)
		goToIndex = self.config.index(toState)
		indexDiff = goToIndex - currentIndex
		if indexDiff < 0:
			indexDiff = 8 + indexDiff
		stepsToTake = (indexDiff * self.STEPS_FOR_45_DEGREES) + self.leftOverFromLastStep
		
		self.leftOverFromLastStep = stepsToTake%1
		stepsToTake = stepsToTake - self.leftOverFromLastStep

		if not debug:
			self.stepper.step(stepsToTake, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
		print("BrailleStepper: Taking {1} 45 degree state changes equalling {2} steps taken".format(indexDiff, stepsToTake))