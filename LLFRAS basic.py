# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 01:28:58 2021

@author: 0526p
"""

import cv2
#import numpy as np
import face_recognition

imgDhruv = face_recognition.load_image_file('C:/Users/0526p/.spyder-py3/ImageDisc/dhruv.jpg')
imgDhruv = cv2.cvtColor(imgDhruv, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('C:/Users/0526p/.spyder-py3/ImageDisc/dhruv test.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgDhruv)[0]
encodeDhruv = face_recognition.face_encodings(imgDhruv)[0]
cv2.rectangle(imgDhruv,(faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

results = face_recognition.compare_faces([encodeDhruv], encodeTest)
faceDis = face_recognition.face_distance([encodeDhruv], encodeTest)
print(results, faceDis)

cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
cv2.imshow('Dhruv', imgDhruv)
cv2.imshow('Test image', imgTest)
cv2.waitKey(0)