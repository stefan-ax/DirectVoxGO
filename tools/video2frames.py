from email.mime import base
import cv2
import os

basedir = "data/custom/venus-rough-1"
video_name = 'venus_rough_video_1.mp4'

video = cv2.VideoCapture(os.path.join(basedir, video_name))

os.makedirs(os.path.join(basedir, 'source'))

i = 0
while(video.isOpened()):
    ret, frame = video.read()
    if ret == False:
        break
    
    _ = cv2.imwrite(os.path.join(basedir, 'source/', video_name[:-4]) + f'_{i}.png', frame, )
    i += 1