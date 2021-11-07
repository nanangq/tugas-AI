import cv2 as cv
import numpy as nump

def rescale(frame, scale=0.75):
    dimension = (int(frame.shape[1]*scale),int(frame.shape[0]*scale))
    return cv.resize(frame, dimension,interpolation=cv.INTER_AREA) 

bl = nump.zeros((500,500,3), dtype='uint8')

cv.rectangle(bl,(0,0), (250,250),(0,255,0),thickness=2)
cv.imshow('kosong',bl)

cv.imshow('nangka', rescale(cv.imread('dataset/nangka/001.jpg')))
cv.waitKey(0)