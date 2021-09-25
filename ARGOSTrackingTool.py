#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Cal Oakley (daniel.oakley@duke.edu)
# Date:   Fall 2021
#--------------------------------------------------------------

#Ask the user for a date, specifying the format
user_date = "7/3/2003"

#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read the first line of the file
line_list = file_object.readlines()

#create 2 empty dictionary
date_dict = {}
coord_dict = {}

#Iterate through all lines in the the lineList
for lineString in line_list:
    if lineString[0] in ("#","u"):
        continue

    #Split the string into a list of data items
    lineData = lineString.split()
    
    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    # Move to the next line
    lineString = file_object.readline()

    #filter obs_lc = 1, 2, or 3
    if obs_lc in ('1', '2', '3'):
    
    #add items to date_dict & coord_dict dictionaries 
        date_dict[record_id] = obs_date
        coord_dict[record_id] = (obs_lat, obs_lon)

#reverse lookup line
user_date = input("Enter a date (M/D/YYYY):")

#Create an empty key list
matching_keys = []

#Loop through all key, value pairs in the date_dictionary
for the_key, the_value in date_dict.items():
    #See if the date (the value) matches the user date
    if the_value == user_date:
        matching_keys.append(the_key)

#Check that at least one key was returned; tell the user if not
if len(matching_keys) == 0:
    print("No observations recorded for {}".format(user_date))
else:

            #Reveal locations for each key in matching_keys
    for matching_key in matching_keys:
        obs_lat, obs_long = coord_dict[matching_key]
        print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat}, lon:{obs_lon} on {user_date}")
    

# Close the file
file_object.close()