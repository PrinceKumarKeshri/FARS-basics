# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 13:02:13 2021
@author: 0526p
"""
import cv2
import numpy as np
import face_recognition
import os
import datetime
import pytz
import csv

path = "C:/Users/0526p/.spyder-py3/ImageDisc"
path2 ='C:/Users/0526p/.spyder-py3/basics'
images = []
classNames = []
RollNo = []

myList = os.listdir(path)
mylist2 = os.listdir(path2)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    text = os.path.splitext(cl)[0]
    classNames.append(text.split('.')[0])
    RollNo.append(text.split('.')[1])

print(f'{classNames}\n{RollNo}')


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def createCSVFile(now3):

    path = f'C:/Users/0526p/.spyder-py3/basics/{now2}.csv'
    if i < 1:
        with open(path, 'w', newline='') as f:
            theWriter = csv.writer(f)
            theWriter.writerow(['Name', 'Roll No', 'Time', 'Mark'])

def markAttendance(name, roll):
    path = f'C:/Users/0526p/.spyder-py3/basics/{now2}.csv'
    
    with open(path, 'r+') as f:

        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            cv2.rectangle(img, (40, 20), (530, 60), (127, 255, 212), cv2.FILLED)
            cv2.putText(img, 'Attendance Already Marked', (50, 50),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            
        if name not in nameList:
            f.writelines(f"\n{name}, {roll}, {now1}, '+1'")
            cv2.rectangle(img, (40, 20), (390, 60), (127, 255, 212), cv2.FILLED)
            cv2.putText(img, 'Attendance Marked', (50, 50),cv2.FONT_HERSHEY_COMPLEX, 1, (230,20, 60), 2)


encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)
i = 0
while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            roll = RollNo[matchIndex]
            
            now = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            global now1, now2
            now1 = now.strftime('%I:%M:%S')
            now2 = now.strftime('%Y-%m-%d')
            

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 0), 2)
            cv2.rectangle(img, (x1, y2+4), (x2, y2+110), (255, 0, 0), cv2.FILLED)
            cv2.putText(img, name, (x1+10, y2+35), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, roll, (x1+8, y2+65),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
            cv2.putText(img, now1, (x1+8, y2+95),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

            currentDate = now2
            pathFind = f'{now2}.csv'
            
            if currentDate == now2:
                if pathFind in mylist2:
                    markAttendance(name, roll)
                    i = i+1
                if pathFind not in mylist2:
                    createCSVFile(now2)
                    markAttendance(name, roll)
                    mylist2.append(pathFind)
                    i = i+1

            elif currentDate != now2:
                createCSVFile(now2)
                markAttendance(name)
                i = 0
                currentDate = now2

            print(name,
                  '\n',
                  roll,
                  '\n',
                  now1,
                  '\n')
    
    cv2.imshow('Webcam', img)
    key = cv2.waitKey(10)
    if key == ord('f'):
        break
cap.release()
cv2.destroyAllWindows()
