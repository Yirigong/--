import RPi.GPIO as GPIO

led = 23
switch = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
#내부 풀다운 저항
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:    
    while True:
        val = GPIO.input(switch)
        print(val)
        GPIO.output(led, val)
finally:
    GPIO.cleanup()
    print('cleanup and exit')