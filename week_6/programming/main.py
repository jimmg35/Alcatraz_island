import requests 
import time
import hmac
import base64
from time import mktime
from hashlib import sha1
from datetime import datetime
from wsgiref.handlers import format_date_time


class Auth():

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_auth_header(self):
        xdate = format_date_time(mktime(datetime.now().timetuple()))
        hashed = hmac.new(self.app_key.encode('utf8'), ('x-date: ' + xdate).encode('utf8'), sha1)
        signature = base64.b64encode(hashed.digest()).decode()

        authorization = 'hmac username="' + self.app_id + '", ' + \
                        'algorithm="hmac-sha1", ' + \
                        'headers="x-date", ' + \
                        'signature="' + signature + '"'
        return {
            'Authorization': authorization,
            'x-date': format_date_time(mktime(datetime.now().timetuple())),
            'Accept - Encoding': 'gzip'
        }

app_id = '22a832f05a1a4b3bb6bb707aa15f9384'
app_key = 'zhTF7LhwFC8D_YR-m64jgFNpKtQ'

key = Auth(app_id, app_key)

