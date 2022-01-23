# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:05:29 2021

@author: 0526p
"""
import os
import csv

path_1 = 'C:/Users/0526p/.spyder-py3'
path_2 = 'C:/Users/0526p/.spyder-py3/branch'

branch = ['Computer science', 'Electrical', 'Mechanical', 'Civil', 'Agriculture']
section = ['A', 'B', 'C', 'D', 'E', 'F']

def display_branch(path):
    print('Branch',
          '\t'*4,
          'New',
          'Remove',
          'Exit\n')
    for b in os.listdir(path):
        print(b)

def display_batch(path):
    print('Batch',
          '\t'*4,
          'New',
          'Remove',
          'Exit\n')
    for b in os.listdir(path):
        print(b)

def display_section(path):
    print('Section',
          '\t'*4,
          'New',
          'Remove',
          'Exit\n')
    for s in os.listdir(path):
        print(s)

def display_semester(path):
    print('Semester',
          '\t'*4,
          'New',
          'Remove',
          'Exit\n')
    for s in os.listdir(path):
        print(s)
    
def display_subject(path):
    print('subject',
          '\t'*4,
          'New',
          'Remove',
          'Exit\n')
    for s in os.listdir(path):
        print(s)

def branch_directory(path_1, path_2, branch, section):
    os.chdir(path_1)
    if 'branch' not in os.listdir(path_1):
        os.mkdir('branch')
        for b in branch:
            os.mkdir(path_2 +'/'+ b)
    display_branch(path_2)
    input_1 = input('Enter Your Option: ').capitalize()
    if input_1 == 'New':
        input_given = input('Enter New Branch Name: ').capitalize()
        os.mkdir(path_2+'/'+ input_given)
        display_branch(path_2)
        input_2 = input('Enter Branch Name: ').capitalize()
        batch_directory(path_2, input_2)
    elif input_1 == 'Remove':
        input_given = input('Enter Remove Branch Name: ').capitalize()
        os.removedirs(path_2 + '/' + input_given)
        display_branch(path_2)
        input_2 = input('Enter Branch Name: ').capitalize()
        batch_directory(path_2, input_2)
    elif input_1 in os.listdir(path_2):
        input_2 = input_1
        batch_directory(path_2, input_2)

def batch_directory(path_2, input_2):
    
    path_3 = path_2 + '/' + input_2
    os.chdir(path_3)
    display_batch(path_3)
    input_3 = input('Enter Your Option: ').capitalize()
    if input_3 == 'New':
        input_given = input('Enter New Batch Name: ').capitalize()
        os.mkdir(path_3 +'/'+ input_given)
        display_batch(path_3)
        input_4 = input('Enter Batch Name: ').capitalize()
        section_directory(path_3, input_4, section)
    elif input_3 == 'Remove':
        input_given = input('Enter Remove Batch Name: ').capitalize()
        os.removedirs(path_3 + '/' + input_given)
        display_batch(path_3)
        input_4 = input('Enter Batch Name: ').capitalize()
        section_directory(path_3, input_4, section)
    elif input_3 in os.listdir(path_3):
        input_4 = input_3
        section_directory(path_3, input_4, section)

def section_directory(path_3, input_4, section):
    path_4 = path_3 + '/' + input_4
    os.chdir(path_4)
    for s in section:
        if s not in os.listdir(path_4):
            os.mkdir(path_4 +'/'+ s)
        elif s in os.listdir(path_4):
            break
    display_section(path_4)
    input_5 = input('Enter Your Option: ').capitalize()
    if input_5 == 'New':
        input_given = input('Enter New Section Name: ').capitalize()
        os.mkdir(path_4+'/'+ input_given)
        display_section(path_4)
        input_6 = input('Enter Section Name').capitalize()
        semester_directory(path_4, input_6)
    elif input_5 == 'Remove':
        input_given = input('Enter Remove Section Name: ').capitalize()
        os.removedirs(path_4 + '/' + input_given)
        display_section(path_4)
        input_6 = input('Enter Section Name').capitalize()
        semester_directory(path_4, input_6)
    elif input_5 in os.listdir(path_4):
        input_6 = input_5
        semester_directory(path_4, input_6)

def semester_directory(path_4, input_6):
    
    path_5 = path_4 + '/' + input_6
    os.chdir(path_5)
    display_semester(path_5)
    input_7 = input('Enter Your Option: ').capitalize()
    if input_7 == 'New':
        input_given = input('Enter New Semester Name: ').capitalize()
        os.mkdir(path_5 +'/'+ input_given)
        display_semester(path_5)
        input_8 = input('Enter Semester Name: ').capitalize()
        section_directory(path_5, input_8)
    elif input_7 == 'Remove':
        input_given = input('Enter Remove Semester Name: ').capitalize()
        os.removedirs(path_5 + '/' + input_given)
        display_semester(path_5)
        input_8 = input('Enter Semester Name: ').capitalize()
        section_directory(path_5, input_8)
    elif input_7 in os.listdir(path_5):
        pass
        input_8 = input_7
        attendance_directory(path_5, input_8)

def attendance_directory(path_5, input_8):
    
    path_6 = path_5 + '/' + input_8
    display_subject(path_6)
    input_9 = input('Enter Your Option: ').capitalize()
    if input_9 == 'New':
        input_given = input('Enter New Subject Name: ').capitalize()
        path_7 = path_6 + '/' + input_given + '.csv'
        with open(path_7, 'w', newline='') as f:
            theWriter = csv.writer(f)
            theWriter.writerow(['Name', 'Roll No'])
        display_subject(path_6)
    elif input_9 == 'Remove':
        input_given = input('Enter Remove Subject Name: ').capitalize()
        path_8 = path_6 + '/' + input_given + '.csv'
        os.remove(path_8)
        display_subject(path_6)
        
branch_directory(path_1, path_2, branch, section)
