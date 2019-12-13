import numpy as np
import cv2
from clips import Environment, Symbol
import clips
import math
import time
import sys
import itertools


def processImage(filename):
    img = cv2.imread(str(filename))
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(imgray, (5, 5), 0)
    ret, thresh = cv2.threshold(imgray, 127, 255, 1)
    contours, h = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return img, imgray, contours


def findAngle(contour):
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    angle_list = []
    for i in range(0, approx.shape[0]):
        vertice1 = approx[i] - approx[(i-1) % approx.shape[0]]
        vertice2 = approx[i] - approx[(i+1) % approx.shape[0]]

        tempdot = vertice1[0].dot(vertice2[0])
        magnitude1 = np.linalg.norm(vertice1[0])
        magnitude2 = np.linalg.norm(vertice2[0])

        angle = math.degrees(np.arccos(tempdot/(magnitude1*magnitude2)))
        angle_list.append(angle)
    return approx, angle_list


def detectImage(sisi, approx, img, angle_list):
    listAgenda = []
    listFact = []
    isFound = False
    if(sisi == 3 and len(approx) == 3):
        print("sisi 3")
        environment = Environment()
        environment.load('segitiga.clp')
        for x in range(len(approx)):
            a = str(approx[x][0][0])
            b = str(approx[x][0][1])
            c = str("(titik " + a + " " + b + ")")
            environment.assert_string(c)

        while (not isFound):
            try:
                hit = next(itertools.islice(environment.activations(), 1))
                listAgenda.append(str(hit).strip('0      '))
                for fact in environment.facts():
                    fakta = str(fact)
                    listFact.append(fakta)
                    if(bangun in fakta):
                        cv2.drawContours(img, [contour], 0, (0, 0, 255), 3)
                        isFound = True
                if (not isFound):
                    listFact = []  # re inisialisasi listFact
                else:
                    return listAgenda, listFact, isFound
                environment.run(1)
            except Exception as e:
                break
        if(not isFound):
            return [], [], False

    elif(sisi == 4 and len(approx) == 4):
        print("sisi 4")
        environment = Environment()
        environment.load('segiempat.clp')
        for x in range(len(approx)):
            a = str(approx[x][0][0])
            b = str(approx[x][0][1])
            c = str("(titik " + str(x) + " " + a + " " + b + ")")
            environment.assert_string(c)

        while (not isFound):
            try:
                hit = next(itertools.islice(environment.activations(), 1))
                listAgenda.append(str(hit).strip('0      '))
                for fact in environment.facts():
                    fakta = str(fact)
                    listFact.append(fakta)
                    if(bangun in fakta):
                        cv2.drawContours(img, [contour], 0, (0, 0, 255), 3)
                        isFound = True
                if (not isFound):
                    listFact = []  # re inisialisasi listFact
                else:
                    return listAgenda, listFact, isFound
                environment.run(1)
            except Exception as e:
                print(e)
                break
        if(not isFound):
            return [], [], False

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

        while (not isFound):
            try:
                hit = next(itertools.islice(environment.activations(), 1))
                listAgenda.append(str(hit).strip('0      '))
                for fact in environment.facts():
                    fakta = str(fact)
                    listFact.append(fakta)
                    if(bangun in fakta):
                        cv2.drawContours(img, [contour], 0, (0, 0, 255), 3)
                        isFound = True
                if (not isFound):
                    listFact = []  # re inisialisasi listFact
                else:
                    return listAgenda, listFact, isFound
                environment.run(1)
            except Exception as e:
                print(e)
                break
        if(not isFound):
            return [], [], False

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

        while (not isFound):
            try:
                hit = next(itertools.islice(environment.activations(), 1))
                listAgenda.append(str(hit).strip('0      '))
                for fact in environment.facts():
                    fakta = str(fact)
                    listFact.append(fakta)
                    if(bangun in fakta):
                        cv2.drawContours(img, [contour], 0, (0, 0, 255), 3)
                        isFound = True
                if (not isFound):
                    listFact = []  # re inisialisasi listFact
                else:
                    return listAgenda, listFact, isFound
                environment.run(1)
            except Exception as e:
                print(e)
                break
        if(not isFound):
            return [], [], False


if __name__ == "__main__":
    bangun = input("Masukkan bangun yang diinginkan : ")
    sisi = (int)(input("Masukkan jumlah sudut : "))
    img, imgray, contours = processImage('Untitled2.png')
    listAgenda = []
    listFact = []
    isFound = False
    for contour in contours:
        approx, angle_list = findAngle(contour)
        if (sisi == len(approx)):
            templistAgenda, templistFact, tempisFound = detectImage(
                sisi, approx, img, angle_list)
            if (tempisFound):
                listAgenda = templistAgenda
                listFact = templistFact
                isFound = tempisFound
    print(listAgenda)
    print(listFact)
    print(isFound)
    cv2.imshow('Image', img)
    cv2.imshow('Image GRAY', imgray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
