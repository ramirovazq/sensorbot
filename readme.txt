# systemd or services route
/home/pi/.config/systemd/user

# automatically starting service during boot
# https://github.com/torfsen/python-systemd-tutorial#automatically-starting-the-service-during-boot

# list services
systemctl --user list-unit-files | grep telegram

# start and stop
systemctl --user start telegram_sensor.service
systemctl --user stop telegram_sensor.service

# return status
systemctl --user status telegram_sensor.service

# enable service 
systemctl --user enable telegram_sensor.service
systemctl --user disable telegram_sensor.service