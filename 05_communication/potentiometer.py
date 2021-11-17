import spidev
import time
import RPi.GPIO as GPIO

LED_PIN=2
spi = spidev.SpiDev()

spi.open(0,0)

spi.max_speed_hz = 100000

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def analog_read(channel):
    ret = spi.xfer2([1, (8+channel) << 4, 0])
    adc_out = ((ret[1] & 3)<<8) + ret[2]
    return adc_out


try:
    while True:
        ldr_value = analog_read(0)
        if(ldr_value <= 512):
            GPIO.output(LED_PIN, GPIO.HIGH) 
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
        print("LDR Value: %d" % ldr_value)
        time.sleep(0.5)

finally:
    spi.close()