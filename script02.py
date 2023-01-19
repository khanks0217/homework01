#Kris Hanks
#COE332 - Homework 2

import names

names8=[]
i = 0 

while i in range(5):
    tempname = names.get_full_name()
    if len(tempname) == 9:
        print(tempname)
        i+=1
