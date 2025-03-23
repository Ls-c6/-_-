import cv2
import numpy as np
def empty(v):
    pass

cap=cv2.VideoCapture(0)
cv2.namedWindow("check")
cv2.resizeWindow("check",720,460)
cv2.createTrackbar("Hue min","check",0,179,empty)
cv2.createTrackbar("Hue max","check",179,179,empty)
cv2.createTrackbar("Sat min","check",0,255,empty)
cv2.createTrackbar("Sat max","check",255,255,empty)
cv2.createTrackbar("Val min","check",0,255,empty)
cv2.createTrackbar("Val max","check",255,255,empty)

while True:
    hmin=cv2.getTrackbarPos("Hue min","check")
    hmax=cv2.getTrackbarPos("Hue max","check")
    smin=cv2.getTrackbarPos("Sat min","check")
    smax=cv2.getTrackbarPos("Sat max","check")
    vmin=cv2.getTrackbarPos("Val min","check")
    vmax=cv2.getTrackbarPos("Val max","check")
    now,next=cap.read()
    hsv=cv2.cvtColor(next, cv2.COLOR_BGR2HSV)
    lower=np.array([hmin,smin,vmin])
    upper=np.array([hmax,smax,vmax])
    mask=cv2.inRange(hsv,lower,upper)
    result=cv2.bitwise_and(next,next,mask=mask)
    cv2.imshow("Result",result)
    cv2.imshow("mask",mask)
    # 按下esc中止
    if cv2.waitKey(1)==27:
        break
