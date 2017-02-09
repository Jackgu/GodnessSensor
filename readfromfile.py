# -*- coding:utf-8 -*-
import cv2
from time import time
import datetime
import numpy as np
import os



def traverse_dir(path):
    for file_or_dir in os.listdir(path):
        abs_path = os.path.abspath(os.path.join(path, file_or_dir))
        if os.path.isdir(abs_path):  # dir
            traverse_dir(abs_path)
        else:                        # file
            if file_or_dir.endswith('.jpg'):
                frame = cv2.imread(abs_path)

                cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"

                frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # カスケード分類器の特徴量を取得する
                cascade = cv2.CascadeClassifier(cascade_path)

                facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(10, 10))
                # facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.01, minNeighbors=3, minSize=(3, 3))
                if len(facerect) > 0:
                    print(abs_path +', face detected')
                    color = (255, 255, 255)  # 白
                    for rect in facerect:
                        # 検出した顔を囲む矩形の作成
                        # cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)

                        x, y = rect[0:2]
                        width, height = rect[2:4]
                        image = frame[y - 10: y + height, x: x + width]

                        num = np.random.randint(1000)
                        name = abs_path.replace(".jpg", "___"+str(num)+".jpg")
                        print name
                        cv2.imwrite(name, image, [int(cv2.IMWRITE_JPEG_QUALITY), 90])


                        # Draw a rectangle around the faces
                        # for (x, y, w, h) in facerect:
                        #    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                        # Display the resulting frame
                else:
                    print(abs_path +', no face')



    return

traverse_dir("./data/other")