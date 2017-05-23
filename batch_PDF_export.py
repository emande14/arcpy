#CREATED: 2017/05/23
#AUTHOR: EDDIE ANDERSON

import arcpy

#SET WORKSPACE
arcpy.env.workspace="C:\\temp"
arcpy.env.overwriteOutput = True

#CREATE A LIST OF ALL MXDS IN THE WORKSPACE
mxdfiles=arcpy.ListFiles("*.mxd")

#ITERATE THROUGH MXDS, EXPORTING PDFS
for file in mxdfiles:
    mxdPath = "C:\\temp\\"+file
    mxd = arcpy.mapping.MapDocument(mxdPath)
    pdfFileName = file[:-4]+".pdf"
    pdfFilePath = "C:\\temp\\"+pdfFileName
    arcpy.mapping.ExportToPDF(mxd, pdfFilePath)
    print pdfFileName+" generated."
    
#DELETE ANY LOCKS
    del mxd