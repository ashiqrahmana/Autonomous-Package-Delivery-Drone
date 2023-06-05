#! /bin/sh
gst-launch-1.0  -v udpsrc port=5600 caps='application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264' \
! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink fps-update-interval=1000 sync=false &
roslaunch mavros px4.launch fcu_url:="udp://:14540@192.168.1.36:14557" && fg
