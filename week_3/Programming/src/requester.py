import requests
import json
from typing import List, Dict

from src.utils import UrlBundler, Key



class Requester():
    """
        Requester for handling common task
    """
    def __init__(self, UB: UrlBundler, key: Key) -> None:
        self.UB: UrlBundler = UB
        self.Key: Key = key
    
    def getAllProjectsMeta(self) -> List[Dict]:
        response = requests.request("GET", 
                                    self.UB.getProjects, 
                                    headers={"CK":self.Key.key})
        return json.loads(response.text)

    def getDevicesOfProject(self, MyStorage):
        print()

        for i in list(MyStorage.storage["ProjectData"].keys()):
            keys = MyStorage.storage["ProjectData"][i]["keys"]
            for j in keys:

                response = requests.request("GET",
                                            self.UB.getDevicesOfProj,
                                            headers={"CK":j})
                print(response.text)