#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")


#fswebcam -r 160x120 --no-banner /home/pi/sensorcam/storage/fotos/minimal.jpg
#fswebcam -r 1920x1080 --no-banner /home/pi/sensorcam/storage/fotos/maximal.jpg

#fswebcam -i 0 -d /dev/video0 -r 1920x1080 -q --title @raspberry  /home/pi/sensorcam/storage/fotos/image.jpg
fswebcam -i 0 -d /dev/video0 -r 1920x1080 --no-banner -q /home/pi/sensorcam/storage/fotos/image.jpg


echo $DATE
echo "foto tomada"


# verify possible formats
# ffmpeg -f v4l2 -list_formats all -i /dev/video0

#640x480 160x120 176x144 320x176 320x240 432x240 352x288 544x288 640x360 752x416 
#800x448 864x480 960x544 1024x576 800x600 1184x656 960x720 1280x720 1392x768 1504x832 
#1600x896 1280x960 1712x960 1792x1008 1920x1080

# taking video
# ffmpeg -f v4l2 -framerate 25 -video_size 640x480 -i /dev/video0 output.mkv
# ffmpeg -f v4l2 -framerate 25 -video_size 640x480 -t 3 -i /dev/video0 output.mkv
# ffmpeg -f v4l2 -framerate 25 -video_size 640x480 -i /dev/video0 output.mkv