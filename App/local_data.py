import requests
from requests.structures import CaseInsensitiveDict
import json
from Api_token import get_api_token



#function to generate the request to the API
def get_local_data(jeu_donnees ,croisement ,modalités ,nivgeo ,codgeo):
    token = get_api_token()

    url = "https://api.insee.fr/donnees-locales/V0.1/donnees/geo-"+croisement+"@"+jeu_donnees+"/"+nivgeo+"-"+codgeo+"."+modalités

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer "+token


    response = requests.get(url, headers=headers)
    ocontent = response.content 
    dcontent = response.content.decode("utf-8")
    jcontent = json.loads(dcontent)
    
    return (jcontent)