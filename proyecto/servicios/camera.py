from time import sleep
import os
import subprocess

def take_webphoto(time_seconds=7, filedir='/home/pi/sensorcam/storage/fotos/', filename='image.jpg', resolution='1920x1080'):
   ## because fswebcam couldnt be used by systemd
   ## it was necessary to include a link in venv/bin folder
   ## fswebcam -> /usr/bin/fswebcam
   #os.system(f"fswebcam -i 0 -d /dev/video0 -r {resolution} --no-banner -q {filedir}{filename}")
   subprocess.Popen(f"fswebcam -i 0 -d /dev/video0 -r {resolution} --no-banner -q {filedir}{filename}", shell=True, executable='/bin/bash')
   sleep(time_seconds)

'''
def take_video(time_seconds=5, rotation=180, filedir='/home/pi/sensorcam/storage/videos/', filename='video.h264'):
   camera.start_preview()
   print("start_preview !!")
   camera.rotation = rotation
   camera.start_recording(filedir + filename)
   sleep(time_seconds)
   camera.stop_recording()
   camera.stop_preview()
   print("video terminado !!")
'''

if __name__ == "__main__":
   take_webphoto(filename='webphoto.jpg')
   #take_photo(filedir='/home/pi/sensorcam/storage/fotos/', filename="rbvs.jpg")
   #take_video(time_seconds=10, filename='test.h264')
