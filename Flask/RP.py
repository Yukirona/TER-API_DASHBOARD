from local_data import get_local_data
import pandas as pd
import json
from pathlib import Path


def SEXE_AGE15_15_90_2018():

        jeu_donnees = "GEO2021RP2018"
        croisement = "SEXE-AGE15_15_90"
        modalités = "all.all"
        nivgeo = "COM"
        codgeo = "52448"

        wanted_data_RP = get_local_data(jeu_donnees ,croisement ,modalités ,nivgeo ,codgeo)

        base = Path('data_json')
        jsonpath = base /  "wanted_data_BDCOM_SEXE-AGE15_15_90_2018.json"
        base.mkdir(exist_ok=True)
        jsonpath.write_text(json.dumps(wanted_data_RP))
        
    
        return (wanted_data_RP)

def SEXE_AGE15_15_90_2013():
    
        jeu_donnees = "GEO2021RP2013"
        croisement = "SEXE-AGE15_15_90"
        modalités = "all.all"
        nivgeo = "COM"
        codgeo = "52448"

        wanted_data_RP = get_local_data(jeu_donnees ,croisement ,modalités ,nivgeo ,codgeo)

        base = Path('data_json')
        jsonpath = base /  "wanted_data_BDCOM_SEXE-AGE15_15_90_2013.json"
        base.mkdir(exist_ok=True)
        jsonpath.write_text(json.dumps(wanted_data_RP))
        print(type(wanted_data_RP))
    
        return (wanted_data_RP)

def SEXE_AGE15_15_90_2008():
    
        jeu_donnees = "GEO2021RP2008"
        croisement = "SEXE-AGE15_15_90"
        modalités = "all.all"
        nivgeo = "COM"
        codgeo = "52448"

        wanted_data_RP = get_local_data(jeu_donnees ,croisement ,modalités ,nivgeo ,codgeo)

        base = Path('data_json')
        jsonpath = base /  "wanted_data_BDCOM_SEXE-AGE15_15_90_2008.json"
        base.mkdir(exist_ok=True)
        jsonpath.write_text(json.dumps(wanted_data_RP))
        print(type(wanted_data_RP))
    
        return (wanted_data_RP)


test = SEXE_AGE15_15_90_2018()
test = SEXE_AGE15_15_90_2013()
test = SEXE_AGE15_15_90_2008()


  

 


