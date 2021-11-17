from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_PIN = 5
LED_PIN2 = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def WTSWNO1():
    return render_template("led_task.html")

@app.route("/led/<color>/<op>")
def led_op(op, color):
    if color == 'blue' and op == 'on':
        GPIO.output(LED_PIN2, GPIO.HIGH)
        return "LED ON"
    elif color == 'blue' and op == 'off':
        GPIO.output(LED_PIN2, GPIO.LOW)
        return "LED OFF"
    elif color == 'red' and op == 'on':
        GPIO.output(LED_PIN, GPIO.HIGH)
        return "LED ON"
    elif color == 'red' and op == 'off':
        GPIO.output(LED_PIN, GPIO.LOW)
        return "LED OFF"




if __name__ == "__main__":
    try:
        app.run(host = "0.0.0.0")
    finally:
        GPIO.cleanup()