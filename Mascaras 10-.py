import cv2
import numpy as np

pelota=cv2.imread('pelotas.jpg')

imagen=cv2.cvtColor(pelota,cv2.COLOR_BGR2HSV)

rojobajo=np.array([0,0,220])
rojoalto=np.array([65,65,255])
maskr=cv2.inRange(pelota,rojobajo,rojoalto)

amarillobajo=np.array([0,171,185])
amarilloalto=np.array([168,249,255])
maskm=cv2.inRange(pelota,amarillobajo,amarilloalto)

naranjabajo=np.array([1,51,156])
naranjaalto=np.array([80,136,254])
maskn=cv2.inRange(pelota,naranjabajo,naranjaalto)

unionA=cv2.bitwise_or(maskr,maskm)
unionB=cv2.bitwise_or(unionA,maskn)

cv2.imshow('Foto original',pelota)
cv2.imshow('Pelota,Rojo,amarillo,naranja',unionB)
cv2.waitKey(0)
cv2.destroyAllWindows()

azulbajo=np.array([60,36,0])
azulalto=np.array([255,209,140])
maska=cv2.inRange(pelota,azulbajo,azulalto)

verdebajo=np.array([0,106,69])
verdealto=np.array([140,255,215])
maskv=cv2.inRange(pelota,verdebajo,verdealto)

rosabajo=np.array([60,6,125])
rosaalto=np.array([217,188,252])
maskro=cv2.inRange(pelota,rosabajo,rosaalto)

union1=cv2.bitwise_or(maska,maskv)
union2=cv2.bitwise_or(union1,maskro)

cv2.imshow('Foto original',pelota)
cv2.imshow('Pelota,Azul,verde,rosa',union2)
cv2.waitKey(0)
cv2.destroyAllWindows()