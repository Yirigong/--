import picamera
import time

path = '/home/pi/src6/06_multimedia'

camera = picamera.PiCamera()

try:
    camera.resolution = (1920,1080)
    camera.start_preview()
    time.sleep(3)
    for i in range(10):
        file_name = 'minwoo%s.jpg' %i+1
        camera.capture('%s/%s' %(path,file_name))
        print(i+1)
        time.sleep(1)
finally:
    camera.stop_preview()
