import picamera
import time

path = '/home/pi/src6/06_multimedia'

camera = picamera.PiCamera()

camera.resolution = (1920,1080)
camera.start_preview()
time.sleep(3)
while True:
    res = input("photo : 1, video : 2, exit : 9")
    if res == '1':
        now_str = time.strftime("%Y%m%d_%H%M%S")
        camera.capture('%s/photo_%s.jpg' %(path,now_str))
    elif res == '2':
        now_str = time.strftime("%Y%m%d_%H%M%S")
        camera.start_recording('%s/video_%s.h264' %(path,now_str))
        input('press enter to stop recoding..')
        camera.stop_recording()
    elif res == '9':
        camera.stop_preview()
        break

