from imutils.video import VideoStream
import imagezmq
import socket
import time

server_ip = ""

sender = imagezmq.ImageSender(connect_to="tcp://{}:5555".format(server_ip))

hostname = socket.gethostname()

vs = VideoStream(src=0).start()

time.sleep(2.0)
 
while True:
	frame = vs.read()
	sender.send_image(hostname, frame)