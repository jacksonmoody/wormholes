import socket
import cv2
import pickle
import struct
import imutils

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '127.0.0.1' #Replace with server IP
port = 5555 

client_socket.connect((host_ip,port)) 

# b: bytes 
data = b""
# Q: unsigned long integer
payload_size = struct.calcsize("Q")

while True:

    #Send payload
    while len(data) < payload_size:
        packet = client_socket.recv(4*1024)
        if not packet: break
        data+=packet

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q",packed_msg_size)[0]

    #Send message
    while len(data) < msg_size:
        data += client_socket.recv(4*1024)

    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)

    #Show received image
    cv2.imshow("Receiving",frame)
    cv2.waitKey(1) 

client_socket.close()