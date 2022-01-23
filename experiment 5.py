# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 02:32:36 2021

@author: 0526p
"""
import csv



path = 'C:/Users/0526p/.spyder-py3/basics/test.csv'

with open(path, 'r') as f:

    thereader =csv.reader(f)
    column2=[]
    i=1
    for r in thereader:
        print(f'row {i}: ',r)
        if r!=[]:
            column2.append(r[1])
        i=i+1
        
print()
print('column 2: ',column2)