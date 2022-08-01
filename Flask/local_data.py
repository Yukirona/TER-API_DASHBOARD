import requests
from requests.structures import CaseInsensitiveDict
import json
from get_api_token import get_api_token
from ratelimit import limits, sleep_and_retry
from pathlib import Path
from encodings import utf_8
# 30 calls per minute
CALLS = 30
RATE_LIMIT = 60

@sleep_and_retry
@limits(calls=CALLS, period=RATE_LIMIT)
def check_limit():
    return

# - Function to generate the request to the API

#/////////////////////////////////////////////////////////////////////////////#

def get_local_data(jeu_donnees ,croisement ,modalités ,nivgeo ,codgeo):
    check_limit()
    #getting the token
    token = get_api_token()

    #building the request
    url = "https://api.insee.fr/donnees-locales/V0.1/donnees/geo-"+croisement+"@"+jeu_donnees+"/"+nivgeo+"-"+codgeo+"."+modalités

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer "+token

    #getting and formatting the wanted content
    response = requests.get(url, headers=headers)
    dcontent = response.content.decode("utf-8")
    jcontent = json.loads(dcontent)
    response.status_code = 404
    print(response.status_code)
    if response.status_code != 200:
        base = Path('data_json')
        name_of_file = "wanted_data_"+jeu_donnees+"_"+croisement+"_"+codgeo+".json"
        jsonpath = base /  name_of_file
        with Path(jsonpath).open(encoding="UTF-8") as source:
            jcontent = json.load(source)
       
        print(jcontent)
    return (jcontent)
 #/////////////////////////////////////////////////////////////////////////////#