import RPi.GPIO as GPIO
import time

Buzzer_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(Buzzer_PIN, GPIO.OUT)

# 주파수 (262Hz)
pwm = GPIO.PWM(BUZZER_PIN,262)
pwm.start(10)

time.sleep(2)
pwm.ChangeDutyCycle(0)

pwm.stop()
GPIO.cleanup()
