# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 02:06:58 2021

@author: 0526p
"""
import csv



path = 'C:/Users/0526p/.spyder-py3/basics/test.csv'

with open(path, 'r') as f:

    thereader =f.readlines()
    column2=[]
    for r in thereader:
        if r!=['\n']:
            empty=r.split(',')
            #empty =[i for i in empty if i!=['\n']]
            print(empty)
            column2.append(empty[1])
    
print(column2)