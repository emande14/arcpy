#Sinuosity Index Calculator
#GIS671 Final Project
#Created 8/1/2015
#Author: Edward Anderson emande14@smumn.edu

#This script determines the sinuosity index of a polyline feature.
#Sinuosity is calculated by dividing a polyline's actual length by its
#Euclidean distance (shortest path) between starting and ending points.
#For example, a sinuosity index of 1 equals a straight line. Values larger 
#than 1 indicate a polyline's degree of curvature.
#A sinuosity index of 0 indicates a closed loop (equal starting and ending points).
#The calculated sinuosity index appears in a new field labled "SINUOSITY"

import arcpy, math
#arcpy.env.overwriteOutput = True

#USER INPUTS
infc = arcpy.GetParameterAsText(0)
outfc = arcpy.GetParameterAsText(1)
arcpy.MakeFeatureLayer_management(infc,"input_layer")
#Error handling: the feature class MUST be a polyline
#This is handled within the tool in ArcMap but kept here for reference
#Desc = arcpy.Describe(infc)
#if Desc.shapeType != "Polyline":
#    print "Error: Feature class must be type Polyline!"
#else:
#    print "Feature is type Polyline: Proceed."

#Error handling: the feature class MUST be a singlepart feature
arcpy.MultipartToSinglepart_management("input_layer",outfc)

#Create a new field to hold the Sinuosity Index
arcpy.AddField_management(outfc,"SINUOSITY","FLOAT")

#Create the update cursor
uCur = arcpy.da.UpdateCursor(outfc, ["SINUOSITY","SHAPE@"])
for row in uCur:
    #determine the actual length of the feature
    length = row[1].length
    #determine the x,y coordinates of the starting and ending points
    x1 = row[1].firstPoint.X
    x2 = row[1].lastPoint.X
    y1 = row[1].firstPoint.Y
    y2 = row[1].lastPoint.Y
    #Euclidean distance determined by Pythagorean Theorem
    euclidean = math.sqrt((x1-x2) **2 + (y1-y2) **2)
    #Error Handling: the following if-else statement exists to handle polyline
    #geometries that are closed loops, i.e. their starting and ending points
    #are the same. If this is the case, their sinuosity index is 0.
    if euclidean == 0 or length == 0:
        #assign a value of zero to the SINUOSITY field
        row[0] = 0
        #update the row with the sinuosity index
        uCur.updateRow(row)
    else:
        #sinuosity expression
        si = length/euclidean
        #assign the new sinuosity index to the SINUOSITY field
        row[0] = si
        #update the row with the sinuosity index
        uCur.updateRow(row)
#delete update cursor and row
del uCur, row
