from flask import Flask
import RPi.GPIO as GPIO

LED_RED = 22
LED_BLUE = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED,GPIO.OUT)
GPIO.setup(LED_BLUE,GPIO.OUT)


app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <p>Hello, Flask!!</p>
    <a href = "/led/red/on">RED LED ON</a>
    <br>
    <a href = "/led/red/off">RED LED OFF</a>
    <br>
    <a href = "/led/blue/on">BLUE LED ON</a>
    <br>
    <a href = "/led/blue/off">BLUE LED OFF</a>
    '''

@app.route('/led/<color>/<op>')
def LED_OP(color, op):
    if color == 'red' and op == 'on':
        GPIO.output(LED_RED, GPIO.HIGH)
        return '''
        <p>RED LED ON</p>
        <a href = "/">GO Home</a>
        '''
    elif color == 'red' and op == 'off':
        GPIO.output(LED_RED,GPIO.LOW)
        return '''
        <p>RED LED OFF</p>
        <a href = "/">GO Home</a>
        '''
    elif color == 'blue' and op == 'on':
        GPIO.output(LED_BLUE,GPIO.HIGH)
        return '''
        <p>BLUE LED ON</p>
        <a href = "/">GO Home</a>
        '''
    elif color == 'blue' and op == 'off':
        GPIO.output(LED_BLUE,GPIO.LOW)
        return '''
        <p>BLUE LED OFF</p>
        <a href = "/">GO Home</a>
        '''
    
if __name__ == "__main__":
    try: 
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()