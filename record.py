# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import cv2
import numpy as np
# 选取摄像头，0为笔记本内置的摄像头，1,2···为外接的摄像头
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# 为保存视频做准备
fourcc = cv2.cv.CV_FOURCC("m", "p", "4", "v")
# 第三个参数则是镜头快慢的，20为正常，小于二十为慢镜头
out = cv2.VideoWriter('output2.mp4', fourcc,10.0,(640,480))
while True:
    # 一帧一帧的获取图像
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 1)
        # 在帧上进行操作
        # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # 开始保存视频
        ####out.write(frame)
        # 显示结果帧
        cv2.imshow("frame", frame)
        num = np.random.randint(1000)
        name = "./data/j"+str(num)+".jpg"
        cv2.imwrite(name, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# 释放摄像头资源
cap.release()
out.release()
cv2.destroyAllWindows()