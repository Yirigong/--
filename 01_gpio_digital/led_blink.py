import RPi.GPIO as GPIO
import time

LED_Red = 4 #빨강
LED_Green = 5 #초록
LED_Blue = 6 #파랑

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

for i in range(10):
    GPIO.output(LED_Red, GPIO.HIGH) #빨강 키기
    print("Red on")
    time.sleep(1)
    GPIO.output(LED_Red, GPIO.LOW) #빨강 끄기
    print("Red off")
    time.sleep(1)
GPIO.cleanup()