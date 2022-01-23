# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 19:14:47 2021

@author: 0526p
"""
import csv



path = 'C:/Users/0526p/.spyder-py3/basics/test.csv'

def newColumn():

    rowList = []    
    with open(path, 'r') as f:
    
        thereader = csv.reader(f)
        for row in thereader:
            rowList.append(row)
    #with open(path, 'w') as f:
    #    pass

    with open(path, 'w') as f:
        
        fwriter= csv.writer(f)
        for i in rowList:
            if rowList.index(i) == 0:
                i.append('mark')
            #else:
                #i.append(0)
            fwriter.writerow(i)

newColumn()
with open(path, 'r') as f:
    freader=csv.reader(f)
    j=0
    for i in freader:
        print(f'row {j+1}: {i}')
        j = j+1