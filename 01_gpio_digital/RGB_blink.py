import RPi.GPIO as GPIO
import time

LED_Red = 4 #빨강
LED_Yellow = 5 #노랑
LED_Green = 6 #초록

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_Red, GPIO.OUT)
GPIO.setup(LED_Yellow, GPIO.OUT)
GPIO.setup(LED_Green, GPIO.OUT)



for i in range(2):
    GPIO.output(LED_Red, GPIO.HIGH) #빨강 키기
    print("Red on")
    time.sleep(2)
    GPIO.output(LED_Red, GPIO.LOW) #빨강 끄기
    GPIO.output(LED_Yellow, GPIO.HIGH) #노랑 키기
    print("Yellow on")
    time.sleep(2)
    GPIO.output(LED_Yellow, GPIO.LOW) #노랑 끄기
    GPIO.output(LED_Green, GPIO.HIGH) #초록 키기
    print("Green on")
    time.sleep(2)
    GPIO.output(LED_Green, GPIO.LOW) #초록 끄기
GPIO.cleanup()