from local_data import get_local_data
import pandas as pd
import json
from pathlib import Path

# - Function to retrieve the dataset contained in the BDCOM database

#/////////////////////////////////////////////////////////////////////////////#
def INDICS_ETATCIVIL_2020():
        #var initialization
        jeu_donnees = "GEO2020RFD2019"
        croisement = "INDICS_ETATCIVIL"
        modalités = "1"
        nivgeo = "COM"
        codgeo = "52448"

        wanted_data_RFD = get_local_data(jeu_donnees ,croisement ,modalités ,nivgeo ,codgeo)

        #base = Path('data_json')
        #jsonpath = base /  "wanted_data_RFD.json"
        #base.mkdir(exist_ok=True)
        #jsonpath.write_text(json.dumps(wanted_data_RFD))

        #print(type(wanted_data_RFD))

        return (wanted_data_RFD)
#/////////////////////////////////////////////////////////////////////////////#
INDICS_ETATCIVIL_2020()