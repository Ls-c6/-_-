import cv2
import numpy as np

# Blue Red
color=[[90,105,100,179,255,255],[0,186,112,8,255,255]]
pencolor=[[255,0,0],[0,0,255]]
draw=[] # [x,y,color]
cap=cv2.VideoCapture(0)
def findPen(img):
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for i in range(len(color)):
        # hsv最低門檻值和最高門檻值(判斷顏色)
        lower=np.array(color[i][:3])
        upper=np.array(color[i][3:6])
        # 傳出灰階圖(只有目標顏色為白)
        mask=cv2.inRange(hsv,lower,upper)
        penx,peny=findContour(mask)
        cv2.circle(temp,(penx,peny),10,pencolor[i],5)
        # 不是噪點再執行
        if peny!=-1:
            # 將座標加入
            draw.append([penx,peny,i])

def findContour(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=-1,-1,-1,-1
    for i in contours:
        # 判斷是否為噪點
        if cv2.contourArea(i)>0:
            # 近似值越大多邊形邊越多 越小則越少
            top=cv2.approxPolyDP(i,cv2.arcLength(i,True)*0.02,True)
            # 把圖形框起並畫出 (左上座標,右上座標,寬度,高度)
            x,y,w,h=cv2.boundingRect(top)
    # 筆尖位置
    return x+w//2,y

def Draw(draw):
    for point in draw:
        cv2.circle(temp,(point[0],point[1]),10,pencolor[point[2]],5)

while True:
    now,next=cap.read()
    if now:
        # 時刻更新當前幀
        temp=next.copy()
        findPen(next)  
        Draw(draw)
        temp=cv2.resize(temp,(0,0),fx=1.2,fy=1.2)
        cv2.imshow("contour",temp)
    else:
        break
    # 按下esc中止程式
    if cv2.waitKey(1)==27:
        break
