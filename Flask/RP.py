from local_data import get_local_data
import pandas as pd
import json
from pathlib import Path






def CS1_8_2018():
    
        jeu_donnees = "GEO2021RP2018"
        croisement = "CS1_8"
        modalités = "all"
        nivgeo = "COM"
        codgeo = "52448"

        wanted_data_RP = get_local_data(jeu_donnees ,croisement ,modalités ,nivgeo ,codgeo)

        base = Path('data_json')
        jsonpath = base /  "wanted_data_CS1_8_2018.json"
        base.mkdir(exist_ok=True)
        jsonpath.write_text(json.dumps(wanted_data_RP))
        
    
        return (wanted_data_RP)


def FAM_G5(wanted_data_BDCOM):
        # - extracting and converting the data from the json
        
        nbpop = {}
        ratio = {}
        nbmen = float(wanted_data_BDCOM['Cellule'][9]['Valeur'])
        for i in range(1,9):  
                nbpop[i] = float(wanted_data_BDCOM['Cellule'][i+9]['Valeur'])
                ratio[i] = (nbpop[i]*100)/nbmen

             
      
        # - creating the FAM_G5 tab
        table = [[ ratio[1]],
                 [ ratio[2]],
                 [ ratio[3]],
                 [ ratio[4]],
                 [ ratio[5]],
                 [ ratio[6]],
                 [ ratio[7]],
                 [ ratio[8]]]
        df = pd.DataFrame(table, columns = ['%'], index=['Agriculteurs exploitants',
                                                         'Cadres et professions intellectuelles supérieures',	
                                                         "Artisans, commerçants, chefs d'entreprise",
                                                         'Professions intermédiaires',
                                                         "Employés",
                                                         'Ouvriers',
                                                         'Retraités',
                                                         'Autres personnes sans activité professionnelle',])

        print(df)
        df= [df.to_html(table_id= 'FAMG5')]
       
        return(df)

def ANEMR2():
    
        jeu_donnees = "GEO2021RP2018"
        croisement = "ANEMR2"
        modalités = "all"
        nivgeo = "COM"
        codgeo = "52448"

        wanted_data_RP = get_local_data(jeu_donnees ,croisement ,modalités ,nivgeo ,codgeo)

        base = Path('data_json')
        jsonpath = base /  "wanted_data_ANEMR2_2018.json"
        base.mkdir(exist_ok=True)
        jsonpath.write_text(json.dumps(wanted_data_RP))
        
    
        return (wanted_data_RP)

def LOG_G2(wanted_data_BDCOM):
        # - extracting and converting the data from the json
        
        nbpop = {}
        ratio = {}
        nbmlog = float(wanted_data_BDCOM['Cellule'][0]['Valeur'])
        for i in range(1,7):  
                nbpop[i] = float(wanted_data_BDCOM['Cellule'][i]['Valeur'])
                ratio[i] = (nbpop[i]*100)/nbmlog

             
      
        # - creating the FAM_G5 tab
        table = [[ ratio[1]],
                 [ ratio[2]],
                 [ ratio[3]],
                 [ ratio[4]],
                 [ ratio[5]],
                 [ ratio[6]]]
        df = pd.DataFrame(table, columns = ['%'], index=['Depuis moins de 2 ans',
                                                         'De 2 à 4 ans',	
                                                         "De 5 à 9 ans",
                                                         'De 10 à 19 ans',
                                                         "De 20 à 29 ans",
                                                         '30 ans ou plus',])


        print(df)
        df= [df.to_html(table_id= 'LOGG2')]
       
        return(df)