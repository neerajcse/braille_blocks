import RPi.GPIO as GPIO
import time

class BrailleEmbosser():
    def __init__(self, pin=21):
        self.pin = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def emboss(self):
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(self.pin, GPIO.LOW)
