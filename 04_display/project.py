import RPi.GPIO as GPIO #GPIO 라이브러리
import time #time 라이브러리

GPIO.setmode(GPIO.BCM)
trig = 15
echo = 14
LED_PIN = 9
Buzzer_PIN = 27
SEGMENT_PINS = [2,3,4,5,6,7,8]
DIGIT_PINS = [10, 11, 12, 13]
data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9
print("start")
GPIO.setup(trig, GPIO.OUT) #출력이므로 OUT
GPIO.setup(echo, GPIO.IN) #입력이므로 IN
GPIO.setup(LED_PIN, GPIO.OUT) #출력이므로 OUT
GPIO.setup(Buzzer_PIN, GPIO.OUT) #출력이므로 OUT
pwm = GPIO.PWM(Buzzer_PIN,262)

for segment in SEGMENT_PINS:
    GPIO.setup(segment,GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)
for digit in DIGIT_PINS:
    GPIO.setup(digit,GPIO.OUT)
    GPIO.output(digit,GPIO.LOW)

def display(digit, number): #4-digit 사용 함수
    for i in range(4):
        if i + 1 == digit:
            GPIO.output(DIGIT_PINS[i], GPIO.LOW)
        else:
            GPIO.output(DIGIT_PINS[i], GPIO.HIGH)
    for i in range(7):
        GPIO.output(SEGMENT_PINS[i], data[number][i])
    time.sleep(0.001)

try :
    while True :
        GPIO.output(trig, False)
        time.sleep(0.001)
        GPIO.output(trig, True)
        time.sleep(0.001)
        GPIO.output(trig, False)
        while GPIO.input(echo) == 0:
            pass
        start = time.time()
        while GPIO.input(echo) == 1:
            pass
        stop = time.time()
        duration_time = stop - start #시간 측정
        distance = 17160 * duration_time #거리 계산
        distance = round(distance) #거리 반올림
        print("Distance : ", distance, "cm") #터미널에 거리 출력

        if(distance > 50): #만약 거리가 50(cm)보다 멀어지면
            print("Wake UP!") #터미널에 Wake UP! 출력
            pwm.start(10) #피에조 부저 소리 ON
            GPIO.output(LED_PIN,GPIO.HIGH) #LED ON
            time.sleep(1)
            pwm.stop() #피에조 부저 소리 OFF
            GPIO.output(LED_PIN,GPIO.LOW) #LED oFF


        #4-digit FND로 거리 출력    
        if(distance<10): #한자리 수 인 경우
            display(4,distance)
        elif(distance<100): #두자리 수 인 경우
            display(3,distance//10)
            display(4,distance%10)
        elif(distance<1000): #세자리 수 인 경우
            display(2,distance//100)
            display(3,(distance%100)//10)
            display(4,distance%10)
        else: #네자리 수 인 경우
            display(1,distance//1000)
            display(2,(distance%1000)//100)
            display(3,(distance%100)//10)
            display(4,distance%10)
finally:
    pwm.stop()
    print("END")
    GPIO.cleanup()