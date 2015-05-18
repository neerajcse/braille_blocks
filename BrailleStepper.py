from ULNStepper import ULNStepper
import atexit

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


class BrailleStepper():
	def __init__(self,
		brailleWheel, 
		stesPerRev=4076,
		onPort=[18,27,22,23],
		debug=False):

		# register destruction steps
		atexit.register(self.turnOffMotors)

		self.debug = debug

		# initalize hardward only if its in production
		if not debug:
			self.stepper = ULNStepper(in1=onPort[0], in2=onPort[1], in3=onPort[2], in4=onPort[4])
			#self.stepper.setSpeed(15)
			
		# motor related config
		self.STEPS_FOR_45_DEGREES = 255
		
		# state related config (the state of where the motor is currently)
		self.leftOverFromLastStep = 0
		self.state = MotorStates.ONE_PIN_100

		# the configuration of the braille wheel that is connected to the motor.
		self.config = brailleWheel.CONFIGURATION
		

	def goToState(self, toState):
		currentIndex = self.config.index(self.state)
		goToIndex = self.config.index(toState)
		indexDiff = goToIndex - currentIndex
		if indexDiff < 0:
			indexDiff = 8 + indexDiff
		print("Current:{}, To: {}, Diff: {}".format(currentIndex, goToIndex, indexDiff))
		
		# make sure that last leftover (i.e 0.5) is added if it exists.
		stepsToTake = (indexDiff * self.STEPS_FOR_45_DEGREES) + self.leftOverFromLastStep
		
		# update internal state
		self.leftOverFromLastStep = stepsToTake%1
		self.state = toState

		# recalculate stepsToTake to maintain accuracy.
		stepsToTake = stepsToTake - self.leftOverFromLastStep
		print("BrailleStepper: Taking {0} 45 degree state changes equalling {1} steps taken".format(indexDiff, stepsToTake))
		if not self.debug:
			self.stepper.takeSteps(int(stepsToTake))
		

	def turnOffMotors(self):
		if not self.debug:
			#for i in range(1,5):
			#	self.motorHAT.getMotor(i).run(Adafruit_MotorHAT.RELEASE)
			del self.stepper
			print("Turning off")
		else:
			print("Turning off motors")
