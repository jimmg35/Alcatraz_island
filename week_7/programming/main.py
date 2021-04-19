
import arcpy 



in_Table = r"D:\Alcatraz_island\week_6\programming\myBikeData.csv"
x_coords = "LON"
y_coords = "LAT"
saved_Layer = r"nike_points"
coord_sys = r"C:\Users\Jim\Desktop\stuff\AAAAA.prj"

arcpy.management.XYTableToPoint(in_Table, saved_Layer,
                                x_coords, y_coords,
                                "#",coord_sys)
print("DONE")