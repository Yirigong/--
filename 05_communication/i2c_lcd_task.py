from lcd import drivers
import time
import datetime
import Adafruit_DHT

display = drivers.Lcd()
TEMP_PIN = 14
sensor = Adafruit_DHT.DHT11
try:
    print("Writing to display")
    while True:
        now = datetime.datetime.now()
        humidity,temperature = Adafruit_DHT.read_retry(sensor,TEMP_PIN)
        display.lcd_display_string(now.strftime("%x%X"),1)
        display.lcd_display_string('{0:0.1f}*C {1:0.1f}%'.format(temperature, humidity),2)
finally:
    print("Cleaning up!")
    display.lcd_clear()