
import json
from local_data import get_local_data

jeu_donnees = "BDCOM2018"
croisement = "INDICS_BDCOM"
modalités = "1"
nivgeo = "COM"
codgeo = "52448"

wanted_data = get_local_data(jeu_donnees ,croisement ,modalités ,nivgeo ,codgeo)

print(wanted_data)

with open("wanted_data_BDCOM.json", "w") as outfile:
        json.dump(wanted_data, outfile)
