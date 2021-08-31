# -*- coding: utf-8 -*-
"""
Extra Exercises
Strings - count the number of codons


Created on Tue Jun  1 08:30:10 2021

@author: john.hanks
"""


# Variables

folder_name = 'C:\\myfolder\\'  
file_type = '.csv'

################# Questions ##############

'''
Print a list of files to read using a for loop and string manipulation
'C:\\myfolder\\' Data1.csv
Data2.csv
Data3.csv
Data4.csv
Data5.csv
Data6.csv
Data7.csv
Data8.csv
Data9.csv
Data10.csv

'''

# Why is \\ (double backslash) needed?







################# Solutions ##############


for n in range(1,11):
    file_name = "Data" + str(n) + file_type
    print(folder_name+file_name)