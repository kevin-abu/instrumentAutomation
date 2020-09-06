import pyvisa, time

nom_tv = 3.3
min_tv = 2.7
max_tv = 3.6
RoomTemp = 25
ColdTemp= -40
HotTemp= 85
def init_psu(tv):
    agilent_psu.write('APPL %r, 0.010' %tv)
    agilent_psu.write('INIT')
    time.sleep(2)
    agilent_psu.write('OUTP OFF')

def init_thermonics(Set_Temp):
    airjet.write('SP%r' %Set_Temp)
    time.sleep(2)

rm = pyvisa.ResourceManager()
print (rm.list_resources())
#agilent_psu = rm.open_resource('GPIB1::1::INSTR')
airjet = rm.open_resource('GPIB1::15::INSTR')
init_thermonics(RoomTemp)
init_thermonics(ColdTemp)
init_thermonics(HotTemp)
#Nozzle_Temp = airjet.query('?TA')
#DUT_Temp = airjet.query('?TD')
#print (Nozzle_Temp)
#init_thermonics(SetPoint)
#init_psu(nom_tv)
#init_psu(min_tv)
#init_psu(max_tv)

"""
#Agilent 3633A
agilent_psu.write('APPL 3.3, 0.010')
agilent_psu.write('INIT')
time.sleep(2)
agilent_psu.write('OUTP OFF')
agilent_psu.write('APPL 2.7, 0.010')
agilent_psu.write('INIT')
time.sleep(2)
agilent_psu.write('OUTP OFF')
agilent_psu.write('APPL 3.6, 0.010')
agilent_psu.write('INIT')
time.sleep(2)
agilent_psu.write('OUTP OFF')
"""

"""
#GPIB1::15::INSTR -THERMONICS
        airjet = rm.open_resource('GPIB1::15::INSTR')
        Set_Temp = airjet.query('?SP25')
        Nozzle_Temp = airjet.query('?TA')
        DUT_Temp = airjet.query('?TD')
"""
"""Agilent 3646A 
agilent_psu.write('INSTrument:SELect OUTPut1') #select output1
agilent_psu.write('SOURce:VOLTage 0')
agilent_psu.write('SOURce:CURRent 0')
agilent_psu.write('APPL 3.3, 0.001')
agilent_psu.write('INIT')
"""