import numpy as np 
import time
import sys
personr = open('countdata.csv', 'r')
persone = open('countdata.csv', 'a')
passwordr = open('passwords.csv', 'r')
passworde = open('passwords.csv', 'a')

#this will be changed to being an input from the website
username = raw_input("What is your username?")
#this will be changed to being an input from the website
password = raw_input("What is your password?")
sequence = str(username) + str(password)

#this will be changed to being an input from the website
num = raw_input("How many people are in your party?")
#this will be changed to being an input from the website
location = raw_input("What is the location you are travelling to?")
username = raw_input("What is your username?")
password = raw_input("What is your password?")

#login function, ensure that password username combination is correct
def validate_user(sequence):
    valid = False
    if sequence in passwordr.read():
        valid = True
    else:
        print("Your password and username combination does not exist.")
    return valid

def create_user(username, password):
    passworde.write(str(username) + "," + str(password) + "\n")

#adding information on the number of people in your group heading to a specific location
def add_count(num):
    if location in personr.read():
        for line in personr:
            if line.startswith(location):
                persone.write(',' + str(num))
    else:
        print("You did not enter a valid location, please return go to our location entry page.")
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
    
