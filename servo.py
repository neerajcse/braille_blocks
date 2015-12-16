import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
pwm = GPIO.PWM(13, 100)
pwm.start(5)

while True:
  cmd = str(raw_input("Next command"))
  if cmd=="exit":
    break
  duty = float(cmd) / 10.0 + 2.5
  pwm.ChangeDutyCycle(duty)

GPIO.cleanup()
