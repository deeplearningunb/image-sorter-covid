import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('archive/dataset/test/NORMAL/NORMAL2-IM-0340-0001.jpeg',0)
img2 = cv2.imread('archive/dataset/test/PNEUMONIA/person113_bacteria_542.jpeg',0)
img3 = cv2.imread('archive/dataset/test/Covid/COVID-260.png',0)

ret3, img = cv2.threshold (img, 0,250, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret3, img2 = cv2.threshold (img2, 0,250, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret3, img3 = cv2.threshold (img3, 0,250, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret, img = cv2.threshold(img, 170, 200, cv2.THRESH_TOZERO)
ret, img2 = cv2.threshold(img2, 170, 200, cv2.THRESH_TOZERO)
ret, img3 = cv2.threshold(img3, 170, 200, cv2.THRESH_TOZERO)
# th2 = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#             cv2.THRESH_BINARY,11,2)




# imS = cv2.resize(th3, (960, 540))  
imS = cv2.resize(img, (960, 540))  
imS2 = cv2.resize(img2, (960, 540))  
imS3 = cv2.resize(img3, (960, 540))  


# Resize image
cv2.imshow("Normal", imS)                            # Show image
cv2.imshow("penumonia ", imS2)                            # Show image
cv2.imshow("Covid", imS3)                            # Show image

cv2.waitKey(0)   