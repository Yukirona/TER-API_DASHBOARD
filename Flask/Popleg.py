from local_data import get_local_data
import pandas as pd
import json
from pathlib import Path

# - Function to retrieve the dataset contained in the BDCOM database

#/////////////////////////////////////////////////////////////////////////////#
def IND_POPLEGALES_2018():
        #var initialization
        jeu_donnees = "POPLEG2018"
        croisement = "IND_POPLEGALES"
        modalités = "1"
        nivgeo = "COM"
        codgeo = "52448"

        wanted_data_popleg = get_local_data(jeu_donnees ,croisement ,modalités ,nivgeo ,codgeo)

        base = Path('data_json')
        jsonpath = base /  "wanted_data_popleg_2018.json"
        base.mkdir(exist_ok=True)
        jsonpath.write_text(json.dumps(wanted_data_popleg))

        #print(type(wanted_data_popleg))

        return (wanted_data_popleg)
#/////////////////////////////////////////////////////////////////////////////#
IND_POPLEGALES_2018()