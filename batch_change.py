#CREATED: 2017/05/23
#AUTHOR: EDDIE ANDERSON

import arcpy

#SET WORKSPACE
arcpy.env.workspace="C:\\temp"
arcpy.env.overwriteOutput = True

#CREATE A LIST OF ALL MXDS IN THE WORKSPACE
mxdfiles=arcpy.ListFiles("*.mxd")

#ENTER TEXT TO BE REPLACED
oldText = 'Inundation Area'     #CHANGE THIS
newText = 'Wetlands'            #CHANGE THIS

#ITERATE THROUGH ALL MXDS, CHANGING TEXT BLOCKS, LAYERS/LEGENDS AND FIGURE NUMBERS
for file in mxdfiles:
    mxdPath = "C:\\temp\\"+file
    mxd = arcpy.mapping.MapDocument(mxdPath)
    #mxd = arcpy.mapping.MapDocument("CURRENT")
#TEXT BLOCKS
    for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
        elm.text = elm.text.replace(oldText,newText) 
#TOC LAYERS & LEGENDS
    for lyr in arcpy.mapping.ListLayers(mxd):
        lyr.name = lyr.name.replace(oldText,newText)
        arcpy.RefreshTOC()      #THIS REFRESHES TABLE OF CONTENTS
        arcpy.RefreshActiveView()   #THIS REFRESHES LAYOUT (LEGENDS)    
        print lyr.name
#FIGURE NUMBERS
    for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
        if 'FIGURE ' in elm.text:
            oldFigText = elm.text
            splitOldFigText = oldFigText.split()
            newNumber = int(splitOldFigText[1])+1
            elm.text = 'FIGURE ' + str(newNumber)
            arcpy.RefreshActiveView()   #THIS REFRESHES LAYOUT
            print elm.text
    mxd.save()
    del mxd
