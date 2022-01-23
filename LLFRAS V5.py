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
import pandas as pd
#from IPython.display import clear_output

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def createSectionCsvFile(getInput, path_6):
    path = path_6 + '/' + getInput+'.csv'
    with open(path, 'w', newline='') as f:
        theWriter = csv.writer(f)
        theWriter.writerow(['Name', 'Roll No'])                
    #print('New Section Created Successfully !')
    
def columnCheck(getInput, path_6):
    path = path_6 + '/' + getInput+'.csv'
    with open(path, 'r') as read_obj:
        theReader = csv.reader(read_obj, delimiter = ',')
        csvList = []
        for l in theReader:
            csvList.append(l)
    return csvList[0][-1]

def fillStudentNameAndRoll(name, roll, getInput, path_6):
    path = path_6 + '/' + getInput+'.csv'
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

def fill_blank_column(getInput, path_6):
    path = path_6 + '/' + getInput+'.csv'
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
            
def addNewData(getInput, path_6):
    path = path_6 + '/' + getInput+'.csv'
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
    
def makeNewHeader(getInput, path_6):
    path = path_6 + '/' + getInput+'.csv'
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
    
def markAttendance(getInput, roll, path_6):
    path = path_6 + '/' + getInput+'.csv'
    with open(path, 'r+') as f:
        myDataList = csv.reader(f)
        rowList  = []
        rollList = []
        dateList = []
        for line in myDataList:
            if line != []:
                rollList.append(line[1])
                dateList.append(line[-1])
                rowList.append(line)
        indexPosition = rollList.index(roll)
        value = dateList[indexPosition]
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
    
def capture(getInput, mylist2, path_6):
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
                now2_string = f'{now2}'
                global checkDate
                if pathFind in mylist2:
                    checkDate = columnCheck(getInput, path_6)
                    
                if pathFind in mylist2:
                    if checkDate == now2_string:
                        return_New_roll = fillStudentNameAndRoll(name, roll, getInput, path_6)
                        if return_New_roll:
                            fill_blank_column(getInput, path_6)
                            addNewData(getInput, path_6)
                            markAttendance(getInput, roll, path_6)
                        else:
                            fill_blank_column(getInput, path_6)
                            addNewData(getInput, path_6)
                            markAttendance(getInput, roll, path_6)
                           
                    elif checkDate != now2_string:
                        makeNewHeader(getInput, path_6)
                        fill_blank_column(getInput, path_6)
                        fillStudentNameAndRoll(name, roll, getInput, path_6)
                        addNewData(getInput, path_6)
                        markAttendance(getInput, roll, path_6)
                
                elif pathFind not in mylist2:
                    createSectionCsvFile(getInput, path_6)
                    display_subject(path_6)
                    makeNewHeader(getInput, path_6)
                    fillStudentNameAndRoll(name, roll, getInput, path_6)
                    addNewData(getInput, path_6)
                    markAttendance(getInput, roll, path_6)
                    mylist2.append(pathFind)    
 
                print()
                print(faceDis)
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

        
def attendance_process(path_6):
    mylist2 = os.listdir(path_6)
    while True:
        input_10 = input('Enter Your Option: ').capitalize()
        input_11 = input_10 + '.csv'
        if input_10 == 'New':
            input_12 = input('Enter New Subject Name: ').capitalize()    
            if (input_12+'.csv') in os.listdir(path_6):
                print('File Already exists')
                attendance_directory(path_5, input_8)
            elif (input_12+'.csv')  not in os.listdir(path_6):
                capture(input_12, mylist2, path_6)        
            break
        elif input_10 == 'Remove':
            input_given = input('Enter Remove Subject Name: ').capitalize()
            if (input_given + '.csv') in os.listdir(path_6):
                path_8 = path_6 + '/' + input_given + '.csv'
                os.remove(path_8)
                attendance_directory(path_5, input_8)
            elif (input_given+'.csv') not in os.listdir(path_6):
                print('File Does not Exists')
                attendance_directory(path_5, input_8)
            break
        elif input_10 == 'Back':
            semester_directory(path_4, input_6)
            break
        elif input_10 == 'Exit':
            branch_directory(path_1, path_2, branch, section)
            break
        elif input_11 in os.listdir(path_6):
            capture(input_10, mylist2, path_6)
            break
        display_subject(path_6)
        print('\nPlease Enter One of The Above Values')
        
def display_branch(path):
    print('Branch',
          '\t'*4,
          'New',
          'Remove\n')
    for b in os.listdir(path):
        print(b)

def display_batch(path):
    print('Batch',
          '\t'*4,
          'New',
          'Remove',
          'Back',
          'Exit\n')
    for b in os.listdir(path):
        print(b)

def display_section(path):
    print('Section',
          '\t'*4,
          'New',
          'Remove',
          'Back',
          'Exit\n')
    for s in os.listdir(path):
        print(s)

def display_semester(path):
    print('Semester',
          '\t'*4,
          'New',
          'Remove',
          'Back',
          'Exit\n')
    for s in os.listdir(path):
        print(s)
    
def display_subject(path):
    print('Subject',
          '\t'*4,
          'New',
          'Remove',
          'Back',
          'Exit\n')
    for s in os.listdir(path):
        print(s)

def encoding_section(path_9, image_directory_section):
    global encodeListKnown, classNames, RollNo
    
    path_10 = path_9 + '/' + image_directory_section
    images = []
    classNames = []
    RollNo = []
    
    myList = os.listdir(path_10)

    for cl in myList:
        curImg = cv2.imread(f'{path_10}/{cl}')
        images.append(curImg)
        text = os.path.splitext(cl)[0]
        classNames.append(text.split('.')[0])
        RollNo.append(text.split('.')[1])
    temporary = path_9 + '/' + 'temp'
    with open(temporary, 'w', newline='') as f:
        theWriter = csv.writer(f)
        theWriter.writerow(['Name', 'Roll No'])
        for n, r in zip(classNames, RollNo):
            theWriter.writerow([n, r])
            
    show_name_roll = pd.read_csv(temporary)
    print('\nList of Students:\n')
    print(show_name_roll)
    os.remove(temporary)
    
    print('\nEncoding of images is in progress.....\n\n')
    encodeListKnown = findEncodings(images)
    print('Encoding Complete!\n\n')
    
def branch_directory(path_1, path_2, branch, section):
    global input_2, image_directory_branch
    
    os.chdir(path_1)
    
    if 'branch' not in os.listdir(path_1):
        os.mkdir('branch')
        for b in branch:
            os.mkdir(path_2 +'/'+ b)
    
    display_branch(path_2)
    while True:
            input_1 = input('Enter Your Option: ').capitalize()
            if input_1 == 'New':
                input_given = input('Enter New Branch Name: ').capitalize()
                if input_given in os.listdir(path_2):
                    print('File Already Exists')
                    branch_directory(path_1, path_2, branch, section)
                    
                elif input_given not in os.listdir(path_2):
                    os.mkdir(path_2+'/'+ input_given)
                    branch_directory(path_1, path_2, branch, section)
                break
            elif input_1 == 'Remove':
                input_given = input('Enter Remove Branch Name: ').capitalize()
                if input_given in os.listdir(path_2):
                    os.removedirs(path_2 + '/' + input_given)
                    branch_directory(path_1, path_2, branch, section)
                elif input_given not in os.listdir(path_2):
                    print("File Does Not Exists")
                    branch_directory(path_1, path_2, branch, section)
                break
            elif input_1 in os.listdir(path_2):
                image_directory_branch = input_1
                input_2 = input_1
                batch_directory(path_2, input_2, image_directory_branch)
                break
            display_branch(path_2)
            print('\nPlease Enter One of The Above Values')
        
def batch_directory(path_2, input_2, image_directory_branch):
    global path_3, input_4, image_directory_batch
    
    path_3 = path_2 + '/' + input_2
    os.chdir(path_3)
    display_batch(path_3)
    while True:
        input_3 = input('Enter Your Option: ').capitalize()
        if input_3 == 'New':
            input_given = input('Enter New Batch Name: ').capitalize()
            if input_given in os.listdir(path_3):
                print('File Already Exists')
                batch_directory(path_2, input_2, image_directory_branch)
            elif input_given not in os.listdir(path_3):
                os.mkdir(path_3 +'/'+ input_given)
                batch_directory(path_2, input_2, image_directory_branch)
            break
        elif input_3 == 'Remove':
            input_given = input('Enter Remove Batch Name: ').capitalize()
            if input_given in os.listdir(path_3):
                os.removedirs(path_3 + '/' + input_given)
                batch_directory(path_2, input_2, image_directory_branch)
            elif input_given not in os.listdir(path_3):
                print('File Does Not Exists')
                batch_directory(path_2, input_2, image_directory_branch)
            break
        elif input_3 == 'Back':
            branch_directory(path_1, path_2, branch, section)
            break
        elif input_3 == 'Exit':
            branch_directory(path_1, path_2, branch, section)
            break
        elif input_3 in os.listdir(path_3):
            image_directory_batch = image_directory_branch + '/' + input_3
            input_4 = input_3
            section_directory(path_3, input_4, section, image_directory_batch)
            break
        display_batch(path_3)
        print('\nPlease Enter One of The Above Values')

def section_directory(path_3, input_4, section, image_directory_batch):
    global path_4, input_6
    
    path_4 = path_3 + '/' + input_4
    os.chdir(path_4)
    
    for s in section:
        if s not in os.listdir(path_4):
            os.mkdir(path_4 +'/'+ s)
        elif s in os.listdir(path_4):
            break
    display_section(path_4)
    while True:
        input_5 = input('Enter Your Option: ').capitalize()
        if input_5 == 'New':
            input_given = input('Enter New Section Name: ').capitalize()
            if input_given in os.listdir(path_4):
                print('File Already Exists')
                section_directory(path_3, input_4, section, image_directory_batch)
            elif input_given not in os.listdir(path_4):
                os.mkdir(path_4+'/'+ input_given)
                section_directory(path_3, input_4, section, image_directory_batch)
            break
        elif input_5 == 'Remove':
            input_given = input('Enter Remove Section Name: ').capitalize()
            if input_given in os.listdir(path_4):
                os.removedirs(path_4 + '/' + input_given)
                section_directory(path_3, input_4, section, image_directory_batch)
            elif input_given not in os.listdir(path_4):
                print('File Does Not Exists')
                section_directory(path_3, input_4, section, image_directory_batch)
            break
        elif input_5 == 'Back':
            batch_directory(path_2, input_2, image_directory_branch)
            break
        elif input_5 == 'Exit':
            branch_directory(path_1, path_2, branch, section)
            break
        elif input_5 in os.listdir(path_4):
            image_directory_section = image_directory_batch + '/' + input_5
            encoding_section(path_9, image_directory_section)   
            input_6 = input_5
            semester_directory(path_4, input_6)
            break
        display_section(path_4)
        print('\nPlease Enter One of The Above Values')

def semester_directory(path_4, input_6):
    global path_5, input_8
    
    path_5 = path_4 + '/' + input_6
    os.chdir(path_5)
    display_semester(path_5)
    while True:
        input_7 = input('Enter Your Option: ').capitalize()
        if input_7 == 'New':
            input_given = input('Enter New Semester Name: ').capitalize()
            if input_given in os.listdir(path_5):
                print('File Already Exits')
                semester_directory(path_4, input_6)
            elif input_given not in os.listdir(path_5):
                os.mkdir(path_5 +'/'+ input_given)
                semester_directory(path_4, input_6)
            break
        elif input_7 == 'Remove':
            input_given = input('Enter Remove Semester Name: ').capitalize()
            if input_given in os.listdir(path_5):
                os.removedirs(path_5 + '/' + input_given)
                semester_directory(path_4, input_6)   
            elif input_given not in os.listdir(path_5):
                print('File Does Not Exists')
                semester_directory(path_4, input_6)
            break
        elif input_7 == 'Back':
            section_directory(path_3, input_4, section, image_directory_batch)
            break
        elif input_7 == 'Exit':
            branch_directory(path_1, path_2, branch, section)
            break
        elif input_7 in os.listdir(path_5):
            pass
            input_8 = input_7
            attendance_directory(path_5, input_8)
            break
        display_semester(path_5)
        print('\nPlease Enter One of The Above Values')

def attendance_directory(path_5, input_8):
    path_6 = path_5 + '/' + input_8
    display_subject(path_6)
    attendance_process(path_6)
  
path_1 = 'C:/Users/0526p/.spyder-py3'
path_2 = 'C:/Users/0526p/.spyder-py3/branch'
path_9 = 'C:/Users/0526p/.spyder-py3/image folder'

branch = ['Computer science', 'Electrical', 'Mechanical', 'Civil', 'Agriculture']
section = ['A', 'B', 'C', 'D', 'E', 'F']

branch_directory(path_1, path_2, branch, section)
    
#cap.release()
#cv2.destroyAllWindows()

