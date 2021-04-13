import requests 
import time
import hmac
import base64
from time import mktime
from hashlib import sha1
from datetime import datetime
from wsgiref.handlers import format_date_time
import json
import numpy as np 
import pandas as pd

from authen import Auth


app_id = '22a832f05a1a4b3bb6bb707aa15f9384'
app_key = 'zhTF7LhwFC8D_YR-m64jgFNpKtQ'
key = Auth(app_id, app_key)



# bike station data
response = requests.request("GET",
                            r"https://ptx.transportdata.tw/MOTC/v2/Bike/Station/Taipei?$format=JSON",
                            verify = False,
                            headers= key.get_auth_header())
total = []
my_index = []
for index, i in enumerate(json.loads(response.text)):
    total.append([i["StationUID"],
                  i["StationName"]["Zh_tw"],
                  i["StationPosition"]["PositionLat"],
                  i["StationPosition"]["PositionLon"],
                  i["BikesCapacity"]]) 
    my_index.append(index)
np_total = np.array(total)
data = pd.DataFrame(np_total, index=my_index, columns=["ID", "Name", "LAT", "LON", "CAP"])
data.to_csv("myBikeData.csv", encoding="utf-8-sig")






# Real time data
response = requests.request("GET",
                            r"https://ptx.transportdata.tw/MOTC/v2/Bike/Availability/Taipei?$format=JSON",
                            verify = False,
                            headers= key.get_auth_header())

total2 = []
my_id_2 = []
for index, i in enumerate(json.loads(response.text)):
    total2.append([i["StationUID"], i["ServiceAvailable"], i["AvailableRentBikes"], i["AvailableReturnBikes"], i["SrcUpdateTime"]])
    my_id_2.append(index)
    
np_total2 = np.array(total2)
data2 = pd.DataFrame(np_total2, index=my_id_2, columns = ["StationUID", "ServiceAvailable", "AvailableRentBikes", "AvailableReturnBikes", "SrcUpdateTime"])
data2.to_csv("myBikeData_slot.csv", encoding="utf-8-sig")


# my_list = ["A", "B", "C", "D", "E"]
    
# for index, i  in enumerate(my_list):
#     if index >= 3:
#         print(index, i)