import cv2 as cv
import numpy as nump

def rescale(frame, scale=0.45):
    dimension = (int(frame.shape[1]*scale),int(frame.shape[0]*scale))
    return cv.resize(frame, dimension,interpolation=cv.INTER_AREA) 

# bl = nump.zeros((500,500,3), dtype='uint8')

# cv.rectangle(bl,(0,0), (250,250),(0,255,0),thickness=2)
# cv.imshow('kosong',bl)

######################################################### 
imageBase = cv.imread('dataset/nangka/001.jpg')
######################################################### 
print(imageBase)#print image information as array
print(imageBase.shape)#show image resolution h x w
######################Show Image############################# 

#####################Crop Image############################# 
im_crop = imageBase[400:300,1200:900]
cv.imshow('crop',im_crop)
cv.waitKey(0)

print(im_crop.shape)

imageCopy = imageBase.copy()
editContrast = cv.addWeighted(imageCopy,2,nump.zeros(imageCopy.shape,imageCopy.dtype),0,-100)
renderEdge = cv.Canny(editContrast, 100,200)

cv.imshow('nangka', rescale(imageBase))
# cv.imshow('nangka copy', rescale(editContrast))
cv.imshow('nangka copy', rescale(renderEdge))
cv.waitKey(0)
cv.destroyAllWindows()





