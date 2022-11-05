import imagezmq
import imutils
import cv2
import socket

hostname = socket.gethostname()

ip = socket.gethostbyname(hostname)

print("IP Address: {}".format(ip))

imageHub = imagezmq.ImageHub()

while True:
    (hostname, frame) = imageHub.recv_image()
    cv2.imshow("Image", frame)
    cv2.waitKey(1)
