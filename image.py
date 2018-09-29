#!/usr/bin/python2

import numpy
import cv2
print "print cv2 version",cv2.__version__


#x=cv2.imread('dog.jpg',1)
x=cv2.imread('cat.png',1)
#x1=x-50
y=cv2.imread('dog1.png',1)
z = cv2.add(x,y)
new = cv2.addWeighted(x,0.4,y,1.0,1)
cv2.imshow('draw',new)
#z=cv2.imread('dog1.jpg',1)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
print x

x[55,55] = [255,255,255]
px= x[55,55]

x[100:150,100:150] = [255,255,255]


#a=x[0:300,0:300]
#print a 
#cv2.imshow('window',a)

cv2.imshow('windowname',x1)
#cv2.imshow('downame',y)
#cv2.imshow('win',z)




cv2.waitKey(0)
#cv2.destroyAllWindow()
cv2.destroyWindow('windowname')
"""
