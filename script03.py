#Kris Hanks
#COE332 - Homework 1

import names

diffnames = [] #stores the different names

i = 0 #counts the number of diff names
while i in range(5):
    tempname = names.get_full_name()
    #check if its a different name
    if tempname not in diffnames:
        #print the name
        print( tempname, len(tempname), sep = ', ')
        #add the new name to the list
        diffnames.append(tempname)
        #increase count of names found
        i +=1


