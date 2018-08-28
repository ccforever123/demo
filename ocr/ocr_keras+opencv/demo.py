# -*- coding:utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('1.bmp', 0)

#使用cv2显示图片
'''
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#使用matplotlib显示图片
'''
plt.imshow(img, cmap='gray', interpolation='bicubic')
# 隐藏x，y轴坐标轴
plt.xticks([]), plt.yticks([])
plt.show()
'''

#捕获摄像头视频帧
cap = cv2.VideoCapture(0)
while(True):
	# 获取每帧视频
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame', gray)
	if cv2.waitKey(1) & 0xff == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()