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

# Copy and paste a line of data as the lineString variable value
lineString = "20624	29051	7/3/2003 14:45	B	0	33.84	-77.807	26.446	-41.968	2	0	-134	151	2	401 651134.7	0"

# Use the split command to parse the items in lineString into a list object
lineData = lineString.split()

# Assign variables to specfic items in the list
record_id = lineData[0]   # ARGOS tracking record ID
obs_date = lineData[2]   # Observation date
ob_lc = lineData[3]       # Observation Location Class
obs_lat = lineData[7]     # Observation Latitude
obs_lon = lineData[8]     # Observation Longitude

# Print information to the use
print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")
