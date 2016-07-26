mxd = arcpy.mapping.MapDocument("CURRENT")
dataframe = arcpy.mapping.ListDataFrames(mxd, "Mainframe")[0]
legend = arcpy.mapping.ListLayoutElements(mxd)
print dataframe
print legend
