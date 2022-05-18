
from cgi import print_directory
import json
from local_data import get_local_data
import pandas as pd

jeu_donnees = "GEO2021RP2018"
croisement = "SEXE-AGE15_15_90"
modalités = "all.all"
nivgeo = "COM"
codgeo = "52448"

wanted_data = get_local_data(jeu_donnees ,croisement ,modalités ,nivgeo ,codgeo)



with open("wanted_data_RP.json", "w") as outfile:
        json.dump(wanted_data, outfile)

print(type(wanted_data))


