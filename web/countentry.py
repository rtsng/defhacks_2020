import numpy as np 
import time
import sys
personr = open('countdata.csv', 'r')
persone = open('countdata.csv', 'a')
activeusere = open('activeuser.csv', 'a')
activeuserr = open('activeuser.csv', 'r')

#adding information on the number of people in your group heading to a specific location
def add_count(username, num):
    if location in personr.read():
        for line in personr:
            if line.startswith(location):
                addnum = True
                persone.write("," + str(username) + ' ' + str(num))
                split_line_data = line.split(",")
                userentry = split_line_data[-1]
    else:
        print("You did not enter a valid location, please return  to our location entry page.")
        sys.exit()

#finding the total number of people at a location
def location_count(location):
    if location in personr.read():
        for line in personr:
            if line.startswith(location):
                count_list = line.split(',')
                count_list_final = strip(str.strip, count_list)
                count_array = np.array(count_list_final)
                total_people = np.sum(a = count_array, dtype = int)
    else:
        print("This location is not currently listed in the database. Please enter it via our location entry page")
        sys.exit()
    return total_people

#sending a text if number of people is over ten
def over(location):
    population = total_people(location)
    if population >= 250:
        return True
    else:
        return = False

#not done
def remove_count(location, userentry):
    if location in personr.read() and userentry in personr.read():
        for line in personr:
            if line.startswith(location):
                line_remove_version = list(line)
                user_index = line_remove_version.index(userentry)
                del(line_remove_version[user_index])
