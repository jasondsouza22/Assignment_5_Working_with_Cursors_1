import arcpy
import os

gdb_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\Assignments\Assignment_5_Working_with_Cursors_1\ProProject_Cursors\ProProject_Cursors.gdb"
fc_name = "MajorAttractions"
fc_path = os.path.join(gdb_path, fc_name)
xy = ["NAME", "SHAPE@X", "SHAPE@Y"]

with arcpy.da.SearchCursor(fc_path, xy) as s_cursor:
    for row in s_cursor:
        n, x, y = row[0], row[1], row[2]
        print("Coordinates of {}: ({}, {})".format(n, x, y))

print("Process Completed")

