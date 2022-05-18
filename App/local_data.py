
from lib2to3.pgen2 import token
from urllib import response
import requests
from requests.structures import CaseInsensitiveDict
import json
import Api_token
from Api_token import get_api_token

def get_local_data():
    token = get_api_token()

    #url = "https://api.insee.fr/donnees-locales/V0.1/donnees/geo-SEXE-AGE15_15_90@GEO2020RP2017/COM-52448.all.all"
    url = "https://api.insee.fr/donnees-locales/V0.1/donnees/geo-INDICS_BDCOM@BDCOM2018/COM-52448.1"


    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer "+token


    response = requests.get(url, headers=headers)

    content = response.content.decode("utf-8")
    jcontent = json.loads(content)

    #with open("test_output.json", "w") as outfile:
        #json.dump(jcontent, outfile)

    #check new data type
        #print(type(jcontent))
    
    

    return (jcontent)