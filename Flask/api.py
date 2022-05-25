from BDCOM import INDICS_BDCOM, POP_T1
def init_dash():
    
    data = INDICS_BDCOM()
    tab = POP_T1(data) 

    return(tab)