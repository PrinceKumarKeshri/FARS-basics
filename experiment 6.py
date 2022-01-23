# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 21:04:58 2021

@author: 0526p
"""
import os
path = 'C:/Users/0526p/.spyder-py3'
input_1 = 'new directory'
os.chdir(path)
os.mkdir(input_1)
os.mkdir(path+'/'+input_1+'/'+'sub dir')

os.chdir('C:/Users/0526p/.spyder-py3/new directory')
os.chdir('C:/Users/0526p/.spyder-py3/new directory/sub dir')


#os.chdir('C:/Users/0526p/.spyder-py3')

#os.mkdir('new directory')
#os.chdir('new directory')
#os.mkdir('sub folder')
