
from urllib import response
import requests
from requests.structures import CaseInsensitiveDict
import json
import Api_token
from Api_token import get_api_token
from local_data import get_local_data



wanted_data = get_local_data()

print(wanted_data)

with open("wanted_data_BDCOM.json", "w") as outfile:
        json.dump(wanted_data, outfile)
