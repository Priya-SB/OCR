# -*- coding: utf-8 -*-
"""
Get pixel coordinates of an image where the mouse double clicks
"""

import cv2
array=[]

class Extractor():
    def __init__(self, filename):
        self.img = cv2.imread(filename,1)
        self.mapper()
        
    def mapper(self):
        #cv2.namedWindow('image',cv2.WINDOW_NORMAL)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.get_coord)
        while(1):
            cv2.imshow('image',self.img)
            if cv2.waitKey(0) & 0xFF == 27:
                break
        cv2.destroyAllWindows()


    def get_coord(self,event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            array.append([x,y])
            cv2.circle(self.img,(x,y),5,(0,0,255),-1)
            cv2.imshow('image',self.img)

def main(filename):
    Extractor(filename)
    """
    for i in range(0,len(array)):
        if i%2==0:
            j=i+1
            return(str(array[i][0]),str(array[i][1]),str(array[j][0]),str(array[j][1]))
    """
    return(str(array[0][0]), str(array[0][1]), str(array[1][0]), str(array[1][1]))
            
    
#main("pg1.jpg")


    