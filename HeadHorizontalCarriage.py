import RPi.GPIO as GPIO
import atexit

class HeadHorizontalCarriage():
    def __init__(self, port=13):
      self.port = port
      GPIO.setup(self.port, GPIO.OUT)
      self.pwm = GPIO.PWM(13, 100)
      pwm.start(0)
      self.state = 0
      # register destruction steps
	  atexit.register(self.resetServo)
    
    def goToNextPosition(self):
      newState = self.state + 20
      angle = (newState / 10.0) + 2.5
      self.pwm.ChangeDutyCycle(angle)
      self.state = newState
      
    def resetServo(self):
      self.pwn.ChangeDutyCycle(2.5)