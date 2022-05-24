
import requests
import re
from requests.structures import CaseInsensitiveDict
import json

#function to get or generate the token to access the API
def get_api_token():
        url = "https://api.insee.fr/token"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Basic MENBMmgyV2NreTBGcjRQeEJ2R2N2dFlIdFRzYTpGck9sVktrczJWX2VaV3V3cDAwR2l2eGNQOTBh"
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        data = "grant_type=client_credentials"


        response = requests.post(url, headers=headers, data=data)
        dcontent = response.content.decode("utf-8")
        jcontent = json.loads(dcontent)
        token = (jcontent['access_token'])
        print(token)
        return(token)

get_api_token()