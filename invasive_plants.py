# Invasive Plants Report Generator for User-Inputed County, MN
# Created 7/11/2015 by Eddie Anderson
#
# Generates a txt file report listing how many records exist for three different species of invasive plants:
# "Alyssum, Hoary", "Butter and Eggs", "Maple, Amur"
# NOTE: this script assumes the user is storing the InvasivePlants shapefile in the following path:
# C:\python\class3\Assignment_Data\InvasivePlants.shp
#
# SAMPLE TEXTFILE OUTPUT
# Location: Crow Wing County, MN
# Alyssum, Hoary:  3 records
# Butter and Eggs:  0 records
# Maple, Amur:  6 records

import arcpy
arcpy.env.overwriteOutput = True
# Get user input for name of desired Minnesota county
input_name = raw_input("Please enter a county name: ")
name_selection = "CTY_NAME = '"+input_name+"'"

# create a variable to reference the COUNTIES shapefile
counties = "C:/python/class3/Assignment_Data/MNCounties.shp"
arcpy.MakeFeatureLayer_management(counties, "county_layer")
# creates a selection of desired county
arcpy.SelectLayerByAttribute_management("county_layer", "NEW_SELECTION", name_selection)

# create a variable to reference the INVASIVES shapefile
invasives = "C:/python/class3/Assignment_Data/InvasivePlants.shp"
arcpy.MakeFeatureLayer_management(invasives, "invasives_layer")
# creates a selection of the invasives layer that fall w/in desired county
arcpy.SelectLayerByLocation_management("invasives_layer", "WITHIN", "county_layer")
# variables to hold the records count of the desired species
alyssum = 0
butter = 0
maple = 0
# make a search cursor, specifying the field name to be searched
sCur = arcpy.da.SearchCursor("invasives_layer", ["common_nam"])
# iterate through all the rows, keeping track of how many records of the invasives exist
for row in sCur:
    if row[0] == "Alyssum, Hoary":
        alyssum += 1
    elif row[0] == "Butter and Eggs":
        butter += 1
    elif row[0] == "Maple, Amur":
        maple += 1
print "Location: " + input_name + " County, MN"
print "Alyssum, Hoary: ",alyssum,"records"
print "Butter and Eggs: ",butter,"records"
print "Maple, Amur: ",maple,"records"
# delete search cursor and counter
del sCur, row

report = open("C:/python/Invasives_County_EA.txt","w") #this creates and opens text file in write mode
report.write("Location: "+input_name+" County, MN\nAlyssum, Hoary: "+str(alyssum)+" records\nButter and Eggs: "+str(butter)+" records\nMaple, Amur: "+str(maple)+" records")
report.close() # this closes the text file
