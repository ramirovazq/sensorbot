from picamera import PiCamera
from time import sleep

camera = PiCamera()

def take_photo(time_seconds=3, rotation=180, filedir='/home/pi/webcam/fotos/', filename='image.jpg'):
   camera.start_preview()
   sleep(time_seconds)
   camera.rotation = rotation
   camera.capture(filedir + filename)
   camera.stop_preview()
   print("foto tomada !!")


def take_video(time_seconds=5, rotation=180, filedir='/home/pi/webcam/videos/', filename='video.h264'):
   camera.start_preview()
   print("start_preview !!")
   camera.rotation = rotation
   camera.start_recording(filedir + filename)
   sleep(time_seconds)
   camera.stop_recording()
   camera.stop_preview()
   print("video terminado !!")

if __name__ == "__main__":
        take_photo(filename="rbvs.jpg")
        #take_video(time_seconds=10, filename='test.h264')
