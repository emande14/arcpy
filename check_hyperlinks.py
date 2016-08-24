# Created 8/24/16
# Iterates through a dbf of hyperlinks, testing to see which ones are active or broken
# If active, the field "EA_Review" is assigned value "ACTIVE"
# Else, the field is assigned value "BROKEN"

import arcpy, os, urllib2
arcpy.env.overwriteOutput = True

uCur = arcpy.da.UpdateCursor("D:\\temp\\not_online.dbf", ["DOC_LINK","EA_Review"])

for row in uCur:
    fullpath = row[0]
    try:
        hyper = urllib2.urlopen(fullpath)
        if hyper.code == 200:
            row[1] = "ACTIVE"
            uCur.updateRow(row)
            print str(hyper) + " ACTIVE"
        else:
            row[1] = "BROKEN"
            uCur.updateRow(row)
    except urllib2.HTTPError, e:
        row[1] = "BROKEN"
        uCur.updateRow(row)
        print str(hyper) + " BROKEN"
del uCur, row
