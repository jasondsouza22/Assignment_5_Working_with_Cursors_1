import arcpy
import os

gdb_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\Assignments\Assignment_5_Working_with_Cursors_1\ProProject_Cursors\ProProject_Cursors.gdb"
fc_name = "MajorAttractions"
fc_path = os.path.join(gdb_path,fc_name)

Post_1970 =[]

field_list = ["NAME","ESTAB"]

search_cursor = arcpy.da.SearchCursor(fc_path,field_list)

for row in search_cursor:
    if row[1] > 1970:
        Post_1970.append(row[0])

names = " | ".join(Post_1970)
print("Major Attractions Established After 1970:")
print(names)






