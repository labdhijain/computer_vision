#!/usr/bin/python2
import numpy
import cv2
x=cv2.imread('dog.jpg',1)
print x
i=cv2.split(x)[0][0][0]
print i
j=cv2.split(x)[1][0][0]
print j
k=cv2.split(x)[2][0][0]
print k

cv2.imshow('window',x)
cv2.waitKey(0)
cv2.destroyAllWindow()

