from local_data import get_local_data
import pandas as pd
import json
from pathlib import Path

# - Function to retrieve the dataset contained in the BDCOM database

#/////////////////////////////////////////////////////////////////////////////#
def INDICS_BDCOM():
        #var initialization
        jeu_donnees = "BDCOM2018"
        croisement = "INDICS_BDCOM"
        modalités = "1"
        nivgeo = "COM"
        codgeo = "52448"

        wanted_data_BDCOM = get_local_data(jeu_donnees ,croisement ,modalités ,nivgeo ,codgeo)

        #base = Path('data_json')
        #jsonpath = base /  "wanted_data_BDCOM.json"
        #base.mkdir(exist_ok=True)
        #jsonpath.write_text(json.dumps(wanted_data_BDCOM))
        #print(type(wanted_data_BDCOM))

        return (wanted_data_BDCOM)
#/////////////////////////////////////////////////////////////////////////////#

# - Function to extract data from the json and create the POP_T1 array

#/////////////////////////////////////////////////////////////////////////////#
def POP_T1(wanted_data_BDCOM):
        # - extracting the data from the json
        pop1968 = (wanted_data_BDCOM['Cellule'][1]['Valeur'])
        pop1975 = (wanted_data_BDCOM['Cellule'][2]['Valeur'])
        pop1982 = (wanted_data_BDCOM['Cellule'][3]['Valeur'])
        pop1990 = (wanted_data_BDCOM['Cellule'][4]['Valeur'])
        pop1999 = (wanted_data_BDCOM['Cellule'][5]['Valeur'])
        pop2008 = (wanted_data_BDCOM['Cellule'][6]['Valeur'])
        pop2013 = (wanted_data_BDCOM['Cellule'][7]['Valeur'])
        pop2018 = (wanted_data_BDCOM['Cellule'][8]['Valeur'])
        # creating the POP_T1 tab
        table = [[ pop1968, pop1975, pop1982, pop1990, pop1999, pop2008, pop2013, pop2018]]
        df = pd.DataFrame(table, columns = ['1968', '1975', '1982', '1990', '1999', '2008', '2013', '2018'], index=['population'])
     


        return (df)
    
#/////////////////////////////////////////////////////////////////////////////#