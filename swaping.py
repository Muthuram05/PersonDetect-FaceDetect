#import libary
import cv2

train=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcame=cv2.VideoCapture(0)
while True:
  work,vedio=webcame.read()
  gray = cv2.cvtColor(vedio, cv2.COLOR_BGR2GRAY)
  face = train.detectMultiScale(gray)
  i = 0
  for (x, y, w, h )in face:
      cv2.rectangle(vedio, (x, y), (x + w, y + h), (255, 0, 0), 3)
      i = i+1
      cv2.putText(vedio,'face'+str(i),(x-10,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

  cv2.imshow("ram",vedio)
  key = cv2.waitKey(1)
  if key == 32:
    quit()
