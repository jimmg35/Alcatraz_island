import os
from os import listdir
#import arcpy 

data_path = r"D:\Alcatraz_island\week_8\data"
output_path = r"D:\Alcatraz_island\week_8\output"

# XY table to point * 38
for i in listdir(data_path):
    path = os.path.join(data_path, i)
    filename = "device_point_{}.shp".format(i[i.index('_') + 1 : i.index('.')])
    out_path = os.path.join(output_path, filename)
    arcpy.management.XYTableToPoint(path,
                                    out_path,
                                    'lon', 'lat',
                                    '#',
                                    arcpy.SpatialReference(4326))
    print("{} complete".format(i))


# Merge 38 point
my_list = []
for i in listdir(output_path):
    suffix = ".shp"
    if i.endswith(suffix):
        my_path = os.path.join(output_path, i)
        my_list.append(my_path)

arcpy.management.Merge(my_list, os.path.join(output_path, "total_device_point.shp"))



# User input point
import pandas as pd 
input_x = 121.5
input_y = 25
data = pd.DataFrame({
        "lat": [input_y],
        "lon": [input_x]
    })
data.to_csv("my_point.csv")


# convert user input into point layer
arcpy.management.XYTableToPoint(r"D:\Alcatraz_island\week_8\script\my_point.csv",
                                os.path.join(output_path, "my_pnt.shp"),
                                'lon', 'lat',
                                '#',
                                arcpy.SpatialReference(4326))

# making buffer depends on user input 
arcpy.analysis.Buffer(r"D:\Alcatraz_island\week_8\output\my_pnt.shp", 
                        r"D:\Alcatraz_island\week_8\output\my_buffer.shp",
                        "10000")

# clip feature 
arcpy.analysis.Clip(r"D:\Alcatraz_island\week_8\output\total_device_point.shp",
                    r"D:\Alcatraz_island\week_8\output\my_buffer_2.shp",
                    r"D:\Alcatraz_island\week_8\output\result.shp")



