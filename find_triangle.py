import numpy as np
import cv2 
from clips import Environment, Symbol
import math

bangun = input("Masukkan bangun yang diinginkan : ")
sisi = (int)(input("Masukkan jumlah sudut : "))

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

    if(sisi == 3 and len(approx) == 3):
        print("sisi 3")
        environment = Environment()
        environment.load('segitiga.clp')
        for x in range(len(approx)) :
            a = str(approx[x][0][0])
            b = str(approx[x][0][1])
            c = str("(titik " + a + " " + b + ")")
            environment.assert_string(c)

        for agenda in environment.activations():
            print(agenda)
            for fact in environment.facts():
                fakta = str(fact)
                print(fakta)
                if(bangun in fakta):
                    cv2.drawContours(img,[contour],0,(0,0,255),3)
                    break
                else:
                    environment.run(1)
        print()
        print("---------------")
    elif(sisi == 4 and len(approx) == 4):
        print("sisi 4")
        environment = Environment()
        environment.load('segiempat.clp')
        for x in range(len(approx)) :
            a = str(approx[x][0][0])
            b = str(approx[x][0][1])
            c = str("(titik " + str(x) + " " + a + " " + b + ")")
            environment.assert_string(c)

        for agenda in environment.activations():
            print(agenda)
            for fact in environment.facts():
                fakta = str(fact)
                print(fakta)
                if(bangun in fakta):
                    cv2.drawContours(img,[contour],0,(0,0,255),3)
                    break
                else:
                    environment.run(1)
        print()
        print("---------------")
    elif(sisi == 5 and len(approx) == 5):
        print("sisi 5")
        sudut1 = angle_list[0]
        sudut2 = angle_list[1]
        sudut3 = angle_list[2]
        sudut4 = angle_list[3]
        sudut5 = angle_list[4]
        environment = Environment()
        environment.load('segilima.clp')
        c = str("(sudut 1 " + (str)(sudut1) + ")")
        environment.assert_string(c)
        c = str("(sudut 2 " + (str)(sudut2) + ")")
        environment.assert_string(c)
        c = str("(sudut 3 " + (str)(sudut3) + ")")
        environment.assert_string(c)
        c = str("(sudut 4 " + (str)(sudut4) + ")")
        environment.assert_string(c)
        c = str("(sudut 5 " + (str)(sudut5) + ")")
        environment.assert_string(c)    

        for agenda in environment.activations():
            print(agenda)
            for fact in environment.facts():
                fakta = str(fact)
                print(fakta)
                if(bangun in fakta):
                    cv2.drawContours(img,[contour],0,(0,0,255),3)
                    break
                else:
                    environment.run(1)
        print()
        print("---------------")
    elif(sisi == 6 and len(approx) == 6):
        print("sisi 6")
        sudut1 = angle_list[0]
        sudut2 = angle_list[1]
        sudut3 = angle_list[2]
        sudut4 = angle_list[3]
        sudut5 = angle_list[4]
        sudut6 = angle_list[5]
        environment = Environment()
        environment.load('segienam.clp')
        c = str("(sudut 1 " + (str)(sudut1) + ")")
        environment.assert_string(c)
        c = str("(sudut 2 " + (str)(sudut2) + ")")
        environment.assert_string(c)
        c = str("(sudut 3 " + (str)(sudut3) + ")")
        environment.assert_string(c)
        c = str("(sudut 4 " + (str)(sudut4) + ")")
        environment.assert_string(c)
        c = str("(sudut 5 " + (str)(sudut5) + ")")
        environment.assert_string(c)
        c = str("(sudut 6 " + (str)(sudut6) + ")")
        environment.assert_string(c)

        for agenda in environment.activations():
            print(agenda)
            for fact in environment.facts():
                fakta = str(fact)
                print(fakta)
                if(bangun in fakta):
                    cv2.drawContours(img,[contour],0,(0,0,255),3)
                    break
                else:
                    environment.run(1)
        print()
        print("---------------")

cv2.imshow('Image', img)
cv2.imshow('Image GRAY', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()