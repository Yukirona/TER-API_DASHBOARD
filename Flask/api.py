import imp
from BDCOM import INDICS_BDCOM, POP_T1, FAM_G1
from RP import CS1_8_2018,  FAM_G5, ANEMR2, LOG_G2



def init_FAMG1():
    
    data = INDICS_BDCOM()
    POPT0 = FAM_G1(data)

    return(POPT0)

def init_POPT1():
    
    data = INDICS_BDCOM()
    POPT1 = POP_T1(data)

    return(POPT1)

def init_FAMG5():

    data = CS1_8_2018()
    FAMG5 = FAM_G5(data)
    
    return(FAMG5) 

def init_LOGG2():

    data = ANEMR2()
    LOGG2 = LOG_G2(data)
    
    return(LOGG2) 