# Streams within 100 feet of roads script
# Created 7/8/2015 by Eddie Anderson
# GIS671A

# Scenario:
# The State EPA is concerned about potential hydrocarbon and road salt runoff into
# the state's streams and rivers. They would like to explore the possibility of installing
# water quality monitoring stations on streams and rivers that flow within 100' of any roadway.

# Methodology:
# create a 100 foot buffer of all roads
# clip all streams within this buffer
# explode multipart features of streams

# Note:
# this script assumes the user is storing their data in the following location:
# C:\temp2
# Data for this script was obtained from the MN Geospatial Commons
# The data was clipped to Rock County, Minnesota for brevity as the actual file size for the entire state would have been 60mb 

# load the arcpy site package
import arcpy
arcpy.env.overwriteOutput = True

# assign shapefiles to variables
roads = "C:/temp2/roads.shp"
streams = "C:/temp2/streams.shp"
roads_buff = "C:/temp2/output/roads_buff.shp"
streams_c = "C:/temp2/output/streams_c.shp"
streams_expl = "C:/temp2/output/streams_expl.shp"
buffer_dist = "100 feet"

# first, buffer the roads 100'
# then clip the streams using the roads buffer
# finally, explode multipart features of the clipped streams
# printing messages will allow us to see messages generated from running the script

arcpy.MakeFeatureLayer_management(roads,"feature_roads")
arcpy.Buffer_analysis("feature_roads",roads_buff,buffer_dist)
arcpy.Clip_analysis(streams,roads_buff,streams_c)
arcpy.MultipartToSinglepart_management(streams_c,streams_expl)
print arcpy.GetMessages()
