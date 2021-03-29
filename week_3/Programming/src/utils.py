
class UrlBundler():
    """
        Url library for the project.
    """
    base_url = r"https://iot.epa.gov.tw"
    getProjects: str = base_url + r"/iot/v1/project"
    getDevicesOfProj: str = base_url + r"/iot/v1/device"


    # url = r"https://iot.epa.gov.tw/iot/v1/device"
    #         aa = requests.request("GET", url, headers={"CK":'PKX74K3Z4E5XBZE5UR'})
    #         print(aa.text)


class Storer():
    """
        Storing processed data from Parser
    """
    storage = {}
    def insert(self, data, name: str):
        self.storage[name] = data


class Key():
    """
        key class for api authentication
    """
    key: str = 'AK39R4UXH52FXA9CPA'