# Sinuosity
import arcpy, math
arcpy.env.overwriteOutput = True
fc = "C:/python/final/streams.shp"
sCursor = arcpy.da.SearchCursor(fc, ["SHAPE@"])

for line in sCursor:
    length = line[0].length
    x1 = line[0].firstPoint.X
    x2 = line[0].lastPoint.X
    y1 = line[0].firstPoint.Y
    y2 = line[0].lastPoint.Y
    #Euclidean distance determined by pythagorean theorem
    euc_d = math.sqrt((x1-x2) **2 + (y1-y2) **2)
    si = length/euc_d
    print round(si,2)
    
del sCursor