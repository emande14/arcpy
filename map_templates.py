#Department Map Templates
#Created 3/31/2016 by Edward Anderson
#Input: a source folder of .mxds
#Output: copies every .mxd in the source folder, updates old information with new, and exports a PDF

import arcpy
#SET WORKSPACE
arcpy.env.workspace="C:\\temp2"

#list all files in the workspace
files=arcpy.ListFiles()
#create an empty list to hold all mxds
mxdfiles=[]
for file in files:
    if file[-3:] == "mxd":
        mxdfiles.append(file)
    else:
        pass
#this prints a list of all mxds
print mxdfiles

#EDITS TO FOLLOW
#for each mxd, do the following:
for file in mxdfiles:
    mxdpath = "C:\\temp2\\"+file #CURRENT PATH
    newmxdpath = "C:\\PublicSafety\\"+file #NEW PATH NAME
    mxd = arcpy.mapping.MapDocument(mxdpath)
    dataframe = arcpy.mapping.ListDataFrames(mxd, "Mainframe")[0]

#Add NEW layers
    layer2 = arcpy.mapping.Layer(r"\\nairobi\GSxxTEAM\GIS\GIS Data Warehouse\Layers\Transportation Networks and Models\County Roads.lyr")
    arcpy.mapping.AddLayer(dataframe, layer2, "TOP")

    layer1 = arcpy.mapping.Layer(r"\\nairobi\GSxxTEAM\GIS\GIS Data Warehouse\Layers\Transportation Networks and Models\County Road Labels.lyr")
    arcpy.mapping.AddLayer(dataframe, layer1, "TOP")

#First, make sure new layers are turned off, so they don't draw when someone opens the mxd (they take awhile)
#Then, remove the NCompass layers
    layers_in_map = arcpy.mapping.ListLayers(mxd)
    for lyr in layers_in_map:
        if lyr.name == "County Road Labels":
            lyr.visible = False
            print "road labels.visible = false (a good thing)"
            arcpy.RefreshTOC()
        elif lyr.name == "County Roads":
            lyr.visible = False
            print "roads.visible = false (a good thing)"
            arcpy.RefreshTOC()
        elif lyr.name == "NCOMPASS_ROADS - CSAH CR Label":
            arcpy.mapping.RemoveLayer(dataframe, lyr)
            print "NCOMPASS_ROADS - CSAH CR Label layer... REMOVED"
        elif lyr.name == "NCOMPASS_ROADS - Shields":
            arcpy.mapping.RemoveLayer(dataframe, lyr)
            print "NCOMPASS_ROADS - Shields layer... REMOVED"
        elif lyr.name == "NCompass Group Layer":
            arcpy.mapping.RemoveLayer(dataframe, lyr)
            print "NCompass Group Layer... REMOVED"

#This next block makes sure the new road layers don't show up in the existing legend element
    legend = arcpy.mapping.ListLayoutElements(mxd,"LEGEND_ELEMENT")[1]
    for lyr in legend.listLegendItemLayers():
        if lyr.name == "County Road Labels":
            legend.removeItem(lyr)
            print "Removed road symbols from legend"
        elif lyr.name == "County Roads":
            legend.removeItem(lyr)
            print "Removed roads from legend"

#Change the text Public Works to Public SAFETY.
    textlist = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")
    for textitem in textlist:
        if textitem.text == "<BOL>County</BOL> <_BOL>Public Works</_BOL>":
            textitem.text = "<BOL>County</BOL> <_BOL>Public Safety</_BOL>"
            print "Text changed to Public Safety"
        else:
            pass

#Save the changes to a new path, but same mxd name
    mxd.saveACopy(newmxdpath)
    print "New mxd saved."
    mxd2 = arcpy.mapping.MapDocument(newmxdpath)

#Export PDFs
    pdffilename = file[:-4]+".pdf"
    pdffilepath = "C:\\PublicSafety\\"+pdffilename
    arcpy.mapping.ExportToPDF(mxd2, pdffilepath)
    print pdffilename+" generated."

#Delete any locks
    del mxd, mxd2
