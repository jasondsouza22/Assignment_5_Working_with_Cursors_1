import arcpy
import os

gdb_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\Assignments\Assignment_5_Working_with_Cursors_1\ProProject_Cursors\ProProject_Cursors.gdb"
fc_name = "MajorAttractions"
fc_path = os.path.join(gdb_path,fc_name)

field_list = ["NAME","ADDR"]


with arcpy.da.SearchCursor(fc_path,field_list) as search_cursor:
    for row in search_cursor:
        print("Major Attraction {} was established in {}".format(row[0],row[1]))

print("Process completed")
