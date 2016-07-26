import arcpy
#set workspace
arcpy.env.workspace="H:\\templates\\PublicSafety"

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

#for each mxd, do the following:
for file in mxdfiles:
    mxdpath = "H:\\templates\\PublicSafety\\"+file #CURRENT PATH
    newmxdpath = "H:\\templates\\PS\\"+file #NEW PATH NAME
    mxd = arcpy.mapping.MapDocument(mxdpath)
    #dataframe = arcpy.mapping.ListDataFrames(mxd, "Mainframe")[0]

    #Save the changes to a new path, but same mxd name
    #mxd.saveACopy(newmxdpath)
    #print "New mxd saved."
    #mxd2 = arcpy.mapping.MapDocument(newmxdpath)

    #Export PDFs
    pdffilename = file[:-4]+".pdf"
    pdffilepath = "H:\\templates\\PS\\"+pdffilename
    arcpy.mapping.ExportToPDF(mxd, pdffilepath)
    print pdffilename+" generated."

    #Delete any locks
    del mxd
