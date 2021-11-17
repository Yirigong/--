import RPi.GPIO as GPIO
import time

Buzzer_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(Buzzer_PIN, GPIO.OUT)

# 주파수 (262Hz)
pwm = GPIO.PWM(Buzzer_PIN,262)
pwm.start(10)

melody1 = [392, 392, 440, 440, 392, 392, 330]
melody2 = [392, 392, 330, 330, 294]
melody3 = [392, 392, 440, 440, 392, 392, 330]
melody4 = [392, 330, 294, 330, 262]
try:
    for i in melody1:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.5)
    for i in melody2:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(1)
    for i in melody3:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.5)
    for i in melody4:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.5)
finally:
    pwm.stop()
    GPIO.cleanup()
