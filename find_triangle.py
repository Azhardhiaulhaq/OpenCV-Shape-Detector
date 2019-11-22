import numpy as np
import cv2 

img = cv2.imread('2dshape3.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(imgray, (5,5),0)
ret, thresh = cv2.threshold(imgray,127,255,1)
contours, h  = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour,True),True)
    if(len(approx)==3):
        print(approx)
        cv2.drawContours(img,[contour],0,(0,0,255),3)
        print("---------------")
    elif(len(approx)==4):
        print("sisi 4")
        print(approx)
        cv2.drawContours(img,[contour],0,(0,0,255),3)
        print("---------------")
# i=0
# print(contours[0])
# approx = cv2.approxPolyDP(contours[0], 0.01*cv2.arcLength(contours[0],True),True)
# print(str(len(approx)))
# cv2.drawContours(img,contours[0],0,(0,255,0),3)
# for contour in contours:
#     dst = cv2.cornerHarris(contour,2,3,0.04)
    # lines = cv2.HoughLinesP([contours[1]],1,np.pi/180,80,minLineLength=50,maxLineGap=5)
    # for line in lines :
    #     print(line[0])
    # approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour,True),True)
    # if len(approx) == 4:
    #     lines = cv2.HoughLinesP([approx],1,np.pi/180,80,minLineLength=50,maxLineGap=5)
    #     for line in lines :
    #         print(line[0])
    #     print("Nilai i :" + str(i))
    #     print(approx)
    #     print("---------")
    #     cv2.drawContours(img,[contours[i]],0,(0,0,255),3)
    #     cv2.putText(img,"Nilai i = " + str(i),(approx.ravel()[0],approx.ravel()[1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
    # else :
    #     print("################")
    # i = i + 1

cv2.imshow('Image', img)
cv2.imshow('Image GRAY', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()