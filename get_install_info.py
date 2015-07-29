# a simple script to get Arc install info from current computer
import arcpy
install = arcpy.GetInstallInfo()
for key in install:
    print "{0}: {1}".format(key, install[key])
