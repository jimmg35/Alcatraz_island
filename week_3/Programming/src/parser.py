import requests
import json
from typing import List, Dict

class Parser():
    """
        Parser for parsing the content derived from Requester
    """
    @staticmethod
    def parseProjectMeta(projMeta: List[Dict]) -> Dict:
        output = {}
        for i in projMeta:
            keys = [k["key"] for k in i["projectKeys"]]
            output[str(i["id"])] = {"name":i["name"], "keys":keys}
        return output