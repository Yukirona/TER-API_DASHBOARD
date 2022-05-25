import requests
from requests.structures import CaseInsensitiveDict
import json
from Api_token import get_api_token



# - Function to generate the request to the API

#/////////////////////////////////////////////////////////////////////////////#
def get_local_data(jeu_donnees ,croisement ,modalités ,nivgeo ,codgeo):

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
    
    return (jcontent)
 #/////////////////////////////////////////////////////////////////////////////#