from BDCOM import INDICS_BDCOM, POP_T1
from RP import AGE15_15_90, POP_T0
def init_POPT1():
    
    data = INDICS_BDCOM()
    POPT1 = POP_T1(data)

    return(POPT1)

def init_POPT0():
    
    data = AGE15_15_90()
    POPT1 = POP_T0(data)

    return()