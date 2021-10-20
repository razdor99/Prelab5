import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pwmPin = 26
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 100)
pwm.start(100)
try:
  for i in range(100):
    pwm.ChangeDutyCycle(100-i)
    time.sleep(.02)
except KeyboardInterrupt:
  print("closing")
GPIO.cleanup()