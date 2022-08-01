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

        base = Path('data_json')
        name_of_file = "wanted_data_"+jeu_donnees+"_"+croisement+"_"+codgeo+".json"
        jsonpath = base /  name_of_file
        base.mkdir(exist_ok=True)
        jsonpath.write_text(json.dumps(wanted_data_BDCOM))
        print(type(wanted_data_BDCOM))

        return (wanted_data_BDCOM)
#/////////////////////////////////////////////////////////////////////////////#

# - Function to extract data from the json and create the POP_T1 array

#/////////////////////////////////////////////////////////////////////////////#
def POP_T1(wanted_data_BDCOM):
        # - extracting and converting the data from the json
        superficie =  float(wanted_data_BDCOM['Cellule'][0]['Valeur'])/100
        pop = {}
        flpop  = {}
        sup = {}
        for i in range(1,9):
                pop[i] = (wanted_data_BDCOM['Cellule'][i]['Valeur'])
                flpop[i] = float(wanted_data_BDCOM['Cellule'][i]['Valeur'])
                sup[i] = flpop[i]/superficie
            
        # - creating the POP_T1 tab
        table = [[ pop[1], pop[2], pop[3], pop[4], pop[5], pop[6], pop[7], pop[8]],
                 [sup[1], sup[2], sup[3], sup[4], sup[5], sup[6], sup[7], sup[8]]]
        df = pd.DataFrame(table, columns = ['1968', '1975', '1982', '1990', '1999', '2008', '2013', '2018'], index=['population',
                                                                                                                    'densité ( hab/km²) '])
       
        df= [df.to_html(table_id= 'POPT1')]
        

        return (df)
        
    
#/////////////////////////////////////////////////////////////////////////////#

def FAM_G1(wanted_data_BDCOM):
        # - extracting and converting the data from the json
        
        flnb  = {}
        flpop  = {}
        ratio = {}
        for i in range(1,9):  
                flnb[i] = float(wanted_data_BDCOM['Cellule'][i+8]['Valeur'])
                flpop[i] = float(wanted_data_BDCOM['Cellule'][i+40]['Valeur'])
                ratio[i] = flpop[i]/flnb[i]

               
      
        # - creating the POP_T1 tab
        table = [[ ratio[1], ratio[2], ratio[3], ratio[4], ratio[5], ratio[6], ratio[7], ratio[8]]]
        df = pd.DataFrame(table, columns = ['1968', '1975', '1982', '1990', '1999', '2008', '2013', '2018'], index=["Nombre moyen de résidents par habitation principale"])
        
        
        
        df = [df.to_html(table_id= 'FAMG1')]
       
        return(df)


data = INDICS_BDCOM()
