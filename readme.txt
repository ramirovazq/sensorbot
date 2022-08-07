# systemd or services route
/home/pi/.config/systemd/user

# automatically starting service during boot
# https://github.com/torfsen/python-systemd-tutorial#automatically-starting-the-service-during-boot

# list services
systemctl --user list-unit-files | grep telegram

# start and stop
systemctl --user start telegram_sensor.service
systemctl --user stop telegram_sensor.service
systemctl --user daemon-reload

# return status
systemctl --user status telegram_sensor.service
systemctl --user status telegram_sensor.service -n 50

# enable service 
systemctl --user enable telegram_sensor.service
systemctl --user disable telegram_sensor.service

# camera commands list-devices
$ v4l2-ctl --list-devices
$ ffmpeg -f v4l2 -list_formats all -i /dev/video0
$ v4l2-ctl --list-formats-ext

ffmpeg -f v4l2 -framerate 25 -video_size 640x480 -t 10 -i /dev/video0 output_1.mp4

ffplay -fs -f v4l2 -input-format mjpg -video_size 640x360 -framerate 30 -i /dev/video0

# good one for test
ffplay -fs -f v4l2  -video_size 640x360 -framerate 30 -i /dev/video0
ffplay -fs -f v4l2  -video_size 640x480 -framerate 30 -i /dev/video0
## fs = full_screen -
ffplay -fs -f v4l2  -video_size 864x480 -framerate 30 -i /dev/video0 stable

ffplay -fs -f v4l2  -video_size 960x544 -framerate 30 -i /dev/video0 bien 
ffplay -fs -f v4l2  -video_size 1024x576 -framerate 30 -i /dev/video0 bien
ffplay -fs -f v4l2  -video_size 1184x656 -framerate 30 -i /dev/video0 bien
ffplay -fs -f v4l2  -video_size 1184x656 -framerate 30 -i /dev/video0 mas o menos
ffplay -fs -f v4l2  -video_size 960x720 -framerate 30 -i /dev/video0 mas o menos
ffplay -fs -f v4l2  -video_size 1792x1008 -framerate 30 -i /dev/video0 no

ffmpeg -f v4l2  -y -video_size 640x480 -framerate 30 -i /dev/video0 video.mp4 stable?
ffmpeg -f v4l2  -video_size 864x480 -framerate 30 -i /dev/video0 -vcodec copy video.mp4 stable?
ffmpeg -f v4l2  -y -video_size 640x480 -framerate 30 -i /dev/video0 -t 5 video.mp4


## GOOD ONES
# excellent reference -> https://www.labnol.org/internet/useful-ffmpeg-commands/28490/
## more stable taking video very fast
# transforms to mp4
ffmpeg -i video.mkv -c:v libx264 filename1.mp4 
# 10 seconds of video
ffmpeg -f v4l2  -y -video_size 640x480 -framerate 30 -i /dev/video0 -codec copy -t 10 video.mkv  
#take an image of video in second 2
ffmpeg -ss 00:00:02 -y -i video.mkv -vf scale=800:-1 -vframes 1 image1.jpg 
ffmpeg -y -i video.mkv -c:v libx264 -preset ultrafast filename1.mp4 