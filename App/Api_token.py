
from urllib import response
import requests
import json
import re
from requests.structures import CaseInsensitiveDict
def get_api_token():
        url = "https://api.insee.fr/token"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Basic MENBMmgyV2NreTBGcjRQeEJ2R2N2dFlIdFRzYTpGck9sVktrczJWX2VaV3V3cDAwR2l2eGNQOTBh"
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        data = "grant_type=client_credentials"


        response = requests.post(url, headers=headers, data=data)

        #print(response.status_code)

        content = response.content.decode("utf-8")
        content_splitted = content.split(",")
        list_access_token = [('access_token' in string)
                                for string in content_splitted]
        selected_content = [x for x, y in zip(
                content_splitted, list_access_token) if y]
        selected_content = selected_content[0]

        token = re.sub(':|"|}|{|access_token', "", selected_content)

        #print(token)

        return token

get_api_token()