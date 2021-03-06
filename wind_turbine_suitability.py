#Wind Turbine Suitability
#Created 7/18/2015
#Author:Eddie Anderson
#GIS671

#note: I copied desired lines from this script and pasted
#them into python window in ArcMap. I did not run the script as is from PythonWin.

#import arcpy, set workspace
import arcpy
arcpy.env.workspace = "C:/python/A5Rasters/WindTurbine13.gdb"
#load all tools from Spatial Analyst module of arcpy site package
from arcpy.sa import *

#The Spatial Analyst extension is needed to run tools w/ rasters
#check to make sure it is available
if arcpy.CheckExtension("spatial") == "Available":
    print "Spatial Analyst available!"
    #arcpy.CheckOutExtension("spatial")
    #arcpy.CheckInExtension("spatial")
else:
    print "Check your extensions!"

#determine correct names of rasters in the WindTurbine13 file geodatabase
rasterlist = arcpy.ListRasters()
for raster in rasterlist:
    print raster

#create raster objects in memory by referencing existing rasters in
#WindeTurbine13 file geodatabase
elev = arcpy.Raster("DEM30M")
landc = arcpy.Raster("LandCov")
windp = arcpy.Raster("WindPower")

#perform the SLOPE tool on the DEM
#we want the output slope in percent, not degrees, so use a z-value of 0.01
elslope = Slope(elev,"PERCENT_RISE",0.01)
#reclassify the slope raster, giving weight to flatter slopes
slpremap = RemapRange([[0,5,5],[5,12,3],[12,25,1],[25,100,-100]])
slpereclas = Reclassify(elslope,"VALUE",slpremap)
#save the reclassified raster as a new raster
slpereclas.save("slpe_re")

#reclass the landcover raster according to the specified values
landremap = RemapValue([[1,-100],[2,1],[3,3],[4,5],[5,3],[6,-100]])
landrecla = Reclassify(landc,"VALUE",landremap,"NODATA")
#save the reclassified raster as a new raster
landrecla.save("la_recl")

#reclass the windpower raster according to the specified values
windpremap = RemapValue([[2,1],[3,3],[4,5]])
windprecla = Reclassify(windp,"VALUE",windpremap,"NODATA")
#The wind power criterion is extra important. Its cell values should be
#multiplied by 2
windpmulti = windprecla * 2
#save the reclassified raster as a new raster
windpmulti.save("windpx2")

#create raster objects from our saved rasters, now residing in the geodatabase
rankedslope = arcpy.Raster("slpe_re")
rankedlc = arcpy.Raster("la_recl")
rankedwp = arcpy.Raster("windpx2")

#finally, sum the ranked scores from all three criteria to determine the best
#suitability for wind turbines
fin_suit = rankedslope+rankedlc+rankedwp
fin_suit.save("final")
