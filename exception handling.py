# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 19:35:18 2021

@author: 0526p
"""
def number():
    while True:
        try:
            result = int(input('please provide number = '))
            if result == 2:
                print('yes')
                break
        except:
            print('Whoops! That is not a number')
            #continue
    #else:
     #   print('Thank You')jkl
      #  break
  
number()