#Kris Hanks
#COE332 - Homework 1

import names

diffnames = []
namelen=[]
i = 0
while i in range(5):
    tempname = names.get_full_name()
    if tempname not in diffnames:
        print( tempname, len(tempname), sep = ', ')
        diffnames.append(tempname)
        i +=1


