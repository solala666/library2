import cv2
import os
import numpy as np
#读取文件夹中的每一张图片
path=os.listdir('D:/HP/library/data')
for i in range(0,len(path)):
    endpath=path[i]
    #读取图片
    img=cv2.imread('D:/HP/library/data/'+str(endpath),-1)
    #将图片转换成hsv形式
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #确定绿色的区域范围
    mingreen=np.array([40,70,70])
    maxgreen=np.array([77,255,255])
    #设置阈值，去除背景
    mask=cv2.inRange(imgHSV,mingreen,maxgreen)
    dst=cv2.bitwise_and(img,img,mask=mask)
    #显示图片
    cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    cv2.imshow('img',dst)
    # 将每张图片提取到的ROI区域写入新文件夹
    cv2.imwrite('D:/HP/library/cv2data/'+str(endpath),dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
