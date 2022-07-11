from BDCOM import INDICS_BDCOM, POP_T1, FAM_G1



def init_POPT0():
    
    data = INDICS_BDCOM()
    POPT0 = FAM_G1(data)

    return(POPT0)

def init_POPT1():
    
    data = INDICS_BDCOM()
    POPT1 = POP_T1(data)

    return(POPT1)