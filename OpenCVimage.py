import cv2 as cv
import numpy as nump

def rescale(frame, scale=0.75):
    dimension = (int(frame.shape[1]*scale),int(frame.shape[0]*scale))
    return cv.resize(frame, dimension,interpolation=cv.INTER_AREA) 
cv.imshow('Daun Nangka', rescale(cv.imread('dataset/nangka/001.jpg')))
cv.imshow('Daun Sirih',  rescale(cv.imread('dataset/sirih/001.jpg')))
cv.waitKey(0)
