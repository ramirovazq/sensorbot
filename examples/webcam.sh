#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 1280x720 --no-banner /home/pi/webcam/fotos/entrada.jpg

echo $DATE
echo "foto tomada"



