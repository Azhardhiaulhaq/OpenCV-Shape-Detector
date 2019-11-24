import numpy as np
import cv2 
from clips import Environment, Symbol
import math

bangun = input("Masukkan bangun yang diinginkan :")
sisi = (int)(input("Masukkan jumlah sudut :"))

img = cv2.imread('2dshape3.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(imgray, (5,5),0)
ret, thresh = cv2.threshold(imgray,127,255,1)
contours, h  = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour,True),True)
    angle_list = []
    for i in range(0,approx.shape[0]):
            vertice1 = approx[i] - approx[(i-1) % approx.shape[0]]
            vertice2 = approx[i] - approx[(i+1) % approx.shape[0]]

            tempdot = vertice1[0].dot(vertice2[0])
            magnitude1 = np.linalg.norm(vertice1[0])
            magnitude2 = np.linalg.norm(vertice2[0])
            
            angle = math.degrees(np.arccos(tempdot/(magnitude1*magnitude2)))
            angle_list.append(angle)
    print(angle_list)

    if(len(approx)==sisi):
        print("sisi 3")
        print(approx)
        environment = Environment()
        environment.load('segitiga2.clp')
        for x in range(len(approx)) :
            a = str(approx[x][0][0])
            b = str(approx[x][0][1])
            c = str("(titik " + a + " " + b + ")")
            environment.assert_string(c)
        # for template in environment.templates():
        #     print(template)
        for agenda in environment.activations():
            print(agenda)
            environment.run()
            i = 0
            for fact in environment.facts():
                fakta = str(fact)
                print(fakta)
                if(bangun in fakta):
                    print(fakta)
                    cv2.drawContours(img,[contour],0,(0,0,255),3)
                    break
        print()
        print("---------------")
    elif(len(approx)==sisi):
        print("sisi 4")
        print(approx)
        environment = Environment()
        environment.load('segiempat.clp')
        sudut1 = angle_list[0]
        sudut2 = angle_list[1]
        sudut3 = angle_list[2]
        sudut4 = angle_list[3]
        environment = Environment()
        environment.load('segilima.clp')
        c = str("(sudut 1 " + sudut1 + ")")
        environment.assert_string(c)
        c = str("(sudut 2 " + sudut2 + ")")
        environment.assert_string(c)
        c = str("(sudut 3 " + sudut3 + ")")
        environment.assert_string(c)
        c = str("(sudut 4 " + sudut4 + ")")
        environment.assert_string(c)
        for agenda in environment.activations():
            print(agenda)
            environment.run()
            i = 0
            for fact in environment.facts():
                fakta = str(fact)
                print(fakta)
                if(bangun in fakta):
                    print(fakta)
                    cv2.drawContours(img,[contour],0,(0,0,255),3)
                    break
        print()
        print("---------------")
    elif(len(approx)==sisi):
        print("sisi 5")
        print(approx)
        sudut1 = angle_list[0]
        sudut2 = angle_list[1]
        sudut3 = angle_list[2]
        sudut4 = angle_list[3]
        sudut5 = angle_list[4]
        environment = Environment()
        environment.load('segilima.clp')
        c = str("(sudut 1 " + sudut1 + ")")
        environment.assert_string(c)
        c = str("(sudut 2 " + sudut2 + ")")
        environment.assert_string(c)
        c = str("(sudut 3 " + sudut3 + ")")
        environment.assert_string(c)
        c = str("(sudut 4 " + sudut4 + ")")
        environment.assert_string(c)
        c = str("(sudut 5 " + sudut5 + ")")
        environment.assert_string(c)
        for agenda in environment.activations():
            print(agenda)
            environment.run()
            i = 0
            for fact in environment.facts():
                fakta = str(fact)
                print(fakta)
                if(bangun in fakta):
                    print(fakta)
                    cv2.drawContours(img,[contour],0,(0,0,255),3)
                    break
        print()
        print("---------------")
    elif(len(approx)==sisi):
        print("sisi 6")
        # print(approx)
        # sudut1 = angle_list[0]
        # sudut2 = angle_list[1]
        # sudut3 = angle_list[2]
        # sudut4 = angle_list[3]
        # sudut5 = angle_list[4]
        # sudut6 = angle_list[5]
        # environment = Environment()
        # environment.load('segilima.clp')
        # c = str("(sudut 1 " + sudut1 + ")")
        # environment.assert_string(c)
        # c = str("(sudut 2 " + sudut2 + ")")
        # environment.assert_string(c)
        # c = str("(sudut 3 " + sudut3 + ")")
        # environment.assert_string(c)
        # c = str("(sudut 4 " + sudut4 + ")")
        # environment.assert_string(c)
        # c = str("(sudut 5 " + sudut5 + ")")
        # environment.assert_string(c)
        # c = str("(sudut 6 " + sudut6 + ")")
        # environment.assert_string(c)
        # for agenda in environment.activations():
        #     print(agenda)
        #     environment.run()
        #     i = 0
        #     for fact in environment.facts():
        #         fakta = str(fact)
        #         print(fakta)
        #         if(bangun in fakta):
        #             print(fakta)
        #             cv2.drawContours(img,[contour],0,(0,0,255),3)
        #             break
        cv2.drawContours(img,[contour],0,(0,0,255),3)
        print()
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