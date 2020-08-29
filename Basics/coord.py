# -*- coding: utf-8 -*-
"""
Get pixel coordinates of an image where the mouse double clicks
"""

import cv2
array=[]

def get_coord(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        array.append([x,y])
        cv2.circle(img,(x,y),5,(0,0,255),-1)
        cv2.imshow('image',img)

img = cv2.imread('myImage.jpg',1)
cv2.namedWindow('image')
cv2.setMouseCallback('image', get_coord)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(0) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()
print(array)