# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 23:10:00 2021

@author: 0526p
"""
#import os
import csv
#import pandas as pd
import numpy as np
path = 'C:/Users/0526p/.spyder-py3/basics/2021-09-03.csv'

with open(path, 'r') as read_obj:
    column = csv.reader(read_obj, delimiter = ',')
    
    #n = np.array(column)
    
    #print(n[0])
    col = []
    
    for c in column:
        
        col.append(c)
print(col[0][-1])