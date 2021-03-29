import requests
import json
from typing import List, Dict

from src.key import Key
from src.utils import UrlBundler




if __name__ == "__main__":

    # initialize basic object
    myKey = Key()
    myBundler = UrlBundler()
    myStorage = Storer()

    # initialize my requester
    myReq = Requester(myBundler, myKey)


    # get projects metadata
    projMeta = myReq.getAllProjectsMeta()
    projMeta_processed = Parser.parseProjectMeta(projMeta)
    myStorage.insert(projMeta_processed)
