import cv2
import numpy as np

img = cv2.imread('./images/light.jpg',1)

x1 = cv2.Sobel(img[:,:,0], cv2.CV_16S, 1, 0)
y1 = cv2.Sobel(img[:,:,0], cv2.CV_16S, 0, 1)

absX1 = cv2.convertScaleAbs(x1)
absY1 = cv2.convertScaleAbs(y1)

x2 = cv2.Sobel(img[:,:,1], cv2.CV_16S, 1, 0)
y2 = cv2.Sobel(img[:,:,1], cv2.CV_16S, 0, 1)

absX2 = cv2.convertScaleAbs(x2)
absY2 = cv2.convertScaleAbs(y2)

x3 = cv2.Sobel(img[:,:,2], cv2.CV_16S, 1, 0)
y3 = cv2.Sobel(img[:,:,2], cv2.CV_16S, 0, 1)

absX3 = cv2.convertScaleAbs(x3)
absY3 = cv2.convertScaleAbs(y3)

dst1 = cv2.addWeighted(absX1, 0.5, absY1, 0.5, 0)
dst2 = cv2.addWeighted(absX2, 0.5, absY2, 0.5, 0)
dst3 = cv2.addWeighted(absX3, 0.5, absY3, 0.5, 0)
dst = cv2.addWeighted(dst1, 0.5, dst2, 0.5, 0)
dst = cv2.addWeighted(dst, 0.666666, dst3, 0.333333, 0)

cv2.imshow("Result", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()