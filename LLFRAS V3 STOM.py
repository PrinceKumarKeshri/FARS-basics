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
        #che=0
        csvList = []
        for l in theReader:
            #try these
            #che =l[-1]
            #break
            csvList.append(l)
    #return che
    #2. think another way for finding last enrty date
    return csvList[0][-1]

def fillStudentNameAndRoll(name, roll, getInput):
    path = f'C:/Users/0526p/.spyder-py3/basics/{getInput}.csv'
    
    with open(path, 'r+') as f:

        myDataList = csv.reader(f)
        rollList = []
        # think for another way for searchihg roll in rollList
        for line in myDataList:
            if line != []:
                rollList.append(line[1])
        #print(rollList)
        if roll in rollList:
            if checkDate == now2:
                markAttendance(getInput, roll)
        elif roll not in rollList:
            f.writelines(f"{name},{roll}")
            addNewData(getInput)
        #according to me alread add collumn is test print here

def addNewData(getInput):
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
                #i.append('mark')
                pass
            else:
                i.append(0)
            fwriter.writerow(i)
    
    #with open(path, 'w', newline='') as f:
     #   theWriter = csv.writer(f)
      #  if checkDate == now2:
       #     theWriter.writerow([0])
    
    
        #with open(input_file, 'r') as read_obj, \
         #   open(output_file, 'w', newline='') as write_obj):
          #  csv_reader = reader(read_obj)
           # csv_writer = writer(write_obj)
            #for row in csv_reader:
             #   #we can also append without using lambda
              #  transform_row(row, csv_reader.line_num)
               # csv_writer.writerow(row)

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
                i.append('Date')
    
            fwriter.writerow(i)
    
    #with open(path, 'r+') as f:
     #   theWriter = csv.writer(f)
      #  theWriter.writerow([now2])
    #headerNewColumn=now2
    #defaultText = 0
    #addNewDate(path, path,
                         #lambda row, line_num:
                          #   row.append(headerNewColumn) if line_num == 1 else row.append(defaultText))



def markAttendance(getInput, roll):
    
    
    
    #defaultText = now1
    path = f'C:/Users/0526p/.spyder-py3/basics/{getInput}.csv'
    
    with open(path, 'r+') as f:
        myDataList = csv.reader(f)
        rollList = []
        dateList = []
        for line in myDataList:
            if line != []:
                rollList.append(line[1])
                dateList.append(line[-1])
        indexPosition = rollList.index(roll)
        value = dateList[indexPosition]

        
    #with open(path, 'r') as f:
     #   reader = csv.reader(f, delimiter =',')
      #  csvList = []
       # for col in reader:
        #    csvList.append(col)
    #value = 0
    #try these: value = rollList.index(roll)
    #for i in range(len(csvList)):
     #   if csvList[i][1] == roll:
      #      value = i
       #     break
        
    #check = csvList[value][-1]  
    #try to check without roll
    if value == 0:
        # Try these :
        #addNewDateAttendance(getInput, getInput,
         #                lambda row, line_num:
          #                   row.append(headerNewColumn) if line_num == 1 else row.append(defaultText))
        dateList[indexPosition] = now1
        cv2.rectangle(img, (40, 20), (390, 60), (127, 255, 212), cv2.FILLED)
        cv2.putText(img, 'Attendance Marked', (50, 50),cv2.FONT_HERSHEY_COMPLEX, 1, (230,20, 60), 2)
    elif value != 0:
        cv2.rectangle(img, (40, 20), (530, 60), (127, 255, 212), cv2.FILLED)
        cv2.putText(img, 'Attendance Already Marked', (50, 50),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

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
                global checkDate
                if pathFind in mylist2:
                    checkDate = columnCheck(getInput)
                    
                if pathFind in mylist2:
                    if checkDate == now2:
                        fillStudentNameAndRoll(name, roll, getInput)
                        #if rollExist == 'Exist':    
                        markAttendance(getInput, roll)
                        
                    elif checkDate != now2:
                        makeNewHeader(getInput)
                        addNewData(getInput)
                        fillStudentNameAndRoll(name, roll, getInput)
                        markAttendance(getInput, roll)
                
                elif pathFind not in mylist2:
                    createSectionCsvFile(getInput)
                    makeNewHeader(getInput)
                    fillStudentNameAndRoll(name, roll, getInput)
                    markAttendance(getInput, roll)
                    mylist2.append(pathFind)
                    
    
                print(name,
                      '\n',
                      roll,
                      '\n',
                      now1,
                      '\n',
                      now2)
        
        cv2.imshow('Webcam', img)
        key = cv2.waitKey(10)
        if key == ord('f'):
            break

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
    input_2 = input('Enter New Section Name: ').capitalize()
    
 #   clear_output()
    capture(input_2)        
elif input_1 == 2:
    filesList = os.listdir(path2)
    for f in filesList:
        file = os.path.splitext(f)[1]
        if file == '.csv':
            print(os.path.splitext(f)[0])
    input_3 = input('Enter Section: ')
 #   clear_output()
    capture(input_3)
    
#cap.release()
#cv2.destroyAllWindows()
