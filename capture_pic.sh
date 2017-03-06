#!/bin/bash

seq=`date +%Y-%m-%d-%H-%M-%S`
groupId="RomainelettuceAndStrawberry"
#fswebcam -d /dev/video -r 640x480 --jpeg 90 -F 5 /mnt/robotic_farm/farm_snapshot_$now.jpg
fswebcam --rotate 180 -r 640x480 --jpeg 90 -F 255 /mnt/robotic_farm/${groupId}_${seq}.jpg

/usr/bin/python /var/work/robotic_farm/monitor.py $groupId $seq >> /var/work/robotic_farm/history.log
