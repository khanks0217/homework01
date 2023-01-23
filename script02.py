#Kris Hanks
#COE332 - Homework 2

import names

names8=[]
i = 0 #i counts names of length 8

while i in range(5):
    #Generate a name and store it in tempname
    tempname = names.get_full_name()
    #Check if tempname is 9 characters, including the space
    if len(tempname) == 9:
        print(tempname)
        #increase name count
        i+=1
