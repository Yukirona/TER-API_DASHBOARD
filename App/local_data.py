
from urllib import response
import requests
from requests.structures import CaseInsensitiveDict
import json
import Api_token
from Api_token import get_api_token


url = "https://api.insee.fr/donnees-locales/V0.1/donnees/geo-SEXE-AGE15_15_90@GEO2020RP2017/COM-52448.all.all"


headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer 4959af37-942b-3c37-bf14-0fafa5b18a15"


response = requests.get(url, headers=headers)

content = response.content.decode("utf-8")


jcontent = json.loads(content)

with open("test_output.json", "w") as outfile:
    json.dump(jcontent, outfile)

#check new data type
print(type(jcontent))
#print(response.status_code)

#print(response.content)

print(jcontent)