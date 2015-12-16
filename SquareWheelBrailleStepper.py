from ULNStepper import ULNStepper
import atexit

class MotorStates():
	NO_PINS_00 = 0
	ONE_PIN_01 = 1
	ONE_PIN_10 = 2
	TWO_PIN_11 = 3

class BrailleWheel():
	CONFIGURATION = [
                        MotorStates.TWO_PIN_11,
                        MotorStates.ONE_PIN_01,
                        MotorStates.NO_PINS_00,
                        MotorStates.ONE_PIN_10,
                        ]


class BrailleStepper():
	def __init__(self,
		brailleWheel, 
		stepsPerRev=4076,
		onPort=[18,27,22,23],
		debug=False):

		# register destruction steps
		atexit.register(self.turnOffMotors)

		self.debug = debug

		# initalize hardward only if its in production
		if not debug:
			self.stepper = ULNStepper(in1=onPort[0], in2=onPort[1], in3=onPort[2], in4=onPort[3])
			#self.stepper.setSpeed(15)
			
		# motor related config
		self.STEPS_FOR_90_DEGREES = 511
		
		# state related config (the state of where the motor is currently)
		self.state = MotorStates.ONE_PIN_10

		# the configuration of the braille wheel that is connected to the motor.
		self.config = brailleWheel.CONFIGURATION
		

	def goToState(self, toState):
		currentIndex = self.config.index(self.state)
		goToIndex = self.config.index(toState)
		indexDiff = goToIndex - currentIndex
		
		print("Current:{}, To: {}, Diff: {}".format(currentIndex, goToIndex, indexDiff))
		
		
		stepsToTake = (indexDiff * self.STEPS_FOR_90_DEGREES)
		
		# update internal state
		self.state = toState

		# recalculate stepsToTake to maintain accuracy.
		print("BrailleStepper: Taking {0} 90 degree state changes equalling {1} steps taken".format(indexDiff, stepsToTake))
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
