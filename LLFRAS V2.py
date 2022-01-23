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
#from IPython.display import clear_output

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
    
def createSectionCsvFile(getInput):
    path = f'C:/Users/0526p/.spyder-py3/basics/{getInput}.csv'
    with open(path, 'w', newline='') as f:
        theWriter = csv.writer(f)
        theWriter.writerow(['Name', 'Roll No'])
    #print('New Section Created Successfully !')
    
def columnCheck(getInput):
    path = f'C:/Users/0526p/.spyder-py3/basics/{getInput}.csv'
    with open(path, 'r') as read_obj:
        theReader = csv.reader(read_obj, delimiter = ',')
        csvList = []
        for l in theReader:
            csvList.append(l)
    return csvList[0][-1]

def fillStudentNameAndRoll(name, roll, getInput):
    path = f'C:/Users/0526p/.spyder-py3/basics/{getInput}.csv'
    with open(path, 'r+') as f:

        myDataList = csv.reader(f)
        rollList = []
        for line in myDataList:
            if line != []:
                rollList.append(line[1])
        
        if roll not in rollList:
            f.writelines(f"{name},{roll}")
            New_roll = roll
            return New_roll
        
def addNewData(getInput):
    path = f'C:/Users/0526p/.spyder-py3/basics/{getInput}.csv'
    rowList = []
    with open(path, 'r') as f:
        thereader = csv.reader(f)
        for row in thereader:
            if row != []:
                rowList.append(row)
    len_of_first_index = len(rowList[0])
    with open(path, 'w') as f: 
        fwriter= csv.writer(f)
        for i in rowList:
            if rowList.index(i) == 0:
                pass
            else:
                if len(i) == len_of_first_index:
                    pass
                else:
                    i.append(0)
            fwriter.writerow(i)
    
def makeNewHeader(getInput):
    path = f'C:/Users/0526p/.spyder-py3/basics/{getInput}.csv'
    rowList = []
    with open(path, 'r') as f:
        thereader = csv.reader(f)
        for row in thereader:
            if row != []:
                rowList.append(row)

    with open(path, 'w') as f:
        fwriter= csv.writer(f)
        for i in rowList:
            if rowList.index(i) == 0:
                i.append(now2)
            fwriter.writerow(i)
    
def markAttendance(getInput, roll):
    path = f'C:/Users/0526p/.spyder-py3/basics/{getInput}.csv'
    with open(path, 'r+') as f:
        myDataList = csv.reader(f)
        rowList  = []
        rollList = []
        timeList = []
        for line in myDataList:
            if line != []:
                rollList.append(line[1])
                timeList.append(line[-1])
                rowList.append(line)
        indexPosition = rollList.index(roll)
        value = timeList[indexPosition]
    with open(path, 'w') as f:
        fwriter= csv.writer(f)
        
        if value == '0':
            for i in rowList:
                if rowList.index(i) == indexPosition:
                    i.remove('0')                    
                    i.append(now1)
                    print(i)
                    cv2.rectangle(img, (40, 20), (390, 60), (127, 255, 212), cv2.FILLED)
                    cv2.putText(img, 'Attendance Marked', (50, 50),cv2.FONT_HERSHEY_COMPLEX, 1, (230,20, 60), 2)
                fwriter.writerow(i)
        elif value != '0':
            cv2.rectangle(img, (40, 20), (530, 60), (127, 255, 212), cv2.FILLED)
            cv2.putText(img, 'Attendance Already Marked', (50, 50),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)    
            for i in rowList:
                fwriter.writerow(i)
    
def fill_blank_column(getInput):
    path = f'C:/Users/0526p/.spyder-py3/basics/{getInput}.csv'
    rowList = []
    with open(path, 'r+') as g:
        theReader = csv.reader(g)
        for r in theReader:
            if r != []:
                rowList.append(r)
    len_of_first_index = len(rowList[0])
    dateList = rowList[0][2:len_of_first_index]
    with open(path, 'w') as g:
        theWriter = csv.writer(g)
        for r in rowList:
            if rowList.index(r) == 0:
                pass
            elif len(r)<len_of_first_index:
                i = len(r)-2
                while dateList[i] != dateList[-1]:
                    r.append(0)
                    print(i)
                    i = i+1
            theWriter.writerow(r)
    
def capture(getInput):
    cap = cv2.VideoCapture(0)
    
    while True:
        global img
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
                now1 = now.strftime('%I:%M')
                now2 = now.strftime('%Y-%m-%d')
                
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 0), 2)
                cv2.rectangle(img, (x1, y2+4), (x2, y2+110), (255, 0, 0), cv2.FILLED)
                cv2.putText(img, name, (x1+10, y2+35), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                cv2.putText(img, roll, (x1+8, y2+65),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                cv2.putText(img, now1, (x1+8, y2+95),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                
                pathFind = f'{getInput}.csv'
                global now2_string
                now2_string = f'{now2}'
                global checkDate
                if pathFind in mylist2:
                    checkDate = columnCheck(getInput)
                    
                if pathFind in mylist2:
                    if checkDate == now2_string:
                        return_New_roll = fillStudentNameAndRoll(name, roll, getInput)
                        if return_New_roll:
                            fill_blank_column(getInput)
                            addNewData(getInput)
                            markAttendance(getInput, return_New_roll)
                        else:
                            fill_blank_column(getInput)
                            addNewData(getInput)
                            markAttendance(getInput, roll)
                        
                    elif checkDate != now2_string:
                        makeNewHeader(getInput)
                        fill_blank_column(getInput)       
                        fillStudentNameAndRoll(name, roll, getInput)
                        addNewData(getInput)
                        markAttendance(getInput, roll)
                
                elif pathFind not in mylist2:
                    createSectionCsvFile(getInput)
                    makeNewHeader(getInput)
                    fillStudentNameAndRoll(name, roll, getInput)
                    addNewData(getInput)
                    markAttendance(getInput, roll)
                    mylist2.append(pathFind)    
    
                print(name,
                      '\n',
                      roll,
                      '\n',
                      now1,
                      '\n',
                      now2,
                      '\n')
        
        cv2.imshow('Webcam', img)
        key = cv2.waitKey(10)
        if key == ord('f'):
            break
    cap.release()
    cv2.destroyAllWindows()



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

print(f'Student Names= {classNames}\n\nRoll No= {RollNo}\n')
print('Encoding of images is in progress.....\n\n')

encodeListKnown = findEncodings(images)
print('Encoding Complete!')
#clear_output()

print('Attendance:',
      '\n\tOptions',
      '\tBerif',
      '\n\t1\t\t\tMake new section',
      '\n\t2\t\t\tMark Attendance')
input_1 = int(input('Enter Your Option: '))
#clear_output()

if input_1 == 1:
    input_2 = input('Ente.r New Section Name: ').capitalize()    
 #   clear_output()
    capture(input_2)        
elif input_1 == 2:
    filesList = os.listdir(path2)
    for f in filesList:
        file = os.path.splitext(f)[1]
        if file == '.csv':
            print(os.path.splitext(f)[0])
    input_3 = input('Enter Section: ').capitalize()
 #   clear_output()
    capture(input_3)
    
#cap.release()
#cv2.destroyAllWindows()
