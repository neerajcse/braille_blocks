import RPi.GPIO as GPIO
import atexit

class HeadHorizontalCarriage():
    def __init__(self, port=13):
      self.port = port
      try:
        GPIO.setmode(GPIO.BCM)
      except e:
        print "GPIO Mode already set"
      GPIO.setup(self.port, GPIO.OUT)
      self.pwm = GPIO.PWM(self.port, 100)
      self.pwm.start(0)
      self.state = 0
      # register destruction steps
      atexit.register(self.resetServo)
    
    def goToNextPosition(self):
      newState = self.state + 20
      newState = newState % 180
      angle = (newState / 10.0) + 2.5
      self.pwm.ChangeDutyCycle(angle)
      self.state = newState
      
    def resetServo(self):
      print "Resetting"
      self.pwm.ChangeDutyCycle(2.5)
