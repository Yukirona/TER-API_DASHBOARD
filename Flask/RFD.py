from local_data import get_local_data
import pandas as pd

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

        #with open("wanted_data_RFD.json", "w") as outfile:
                #json.dump(wanted_data_RFD, outfile)

        #print(type(wanted_data_RFD))

        return (wanted_data_RFD)
#/////////////////////////////////////////////////////////////////////////////#
