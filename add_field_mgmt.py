import arcpy
from arcpy import env
env.workspace = r"H:\temp\partners.gdb\PartnerPts"

for fc in arcpy.ListFeatureClasses():
    arcpy.AddField_management(fc, "ZOWNER", "TEXT", field_length = 50)
    arcpy.AddField_management(fc, "ZTYPE", "TEXT", field_length = 15)
    arcpy.AddField_management(fc, "ZLOCATION", "TEXT", field_length = 15)
    arcpy.AddField_management(fc, "ZDATE", "TEXT", field_length = 15)
    print fc +" ADDED FIELD"

