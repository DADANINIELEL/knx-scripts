import asyncio
from xknx import XKNX
#from xknx.devices import Fan 
from lama import LamaModbusTCP, LamaKNX

async main():
    xknx = XKNX(config='xknx.yaml', daemon_mode=True)
    lama_1 = LamaModbusTCP() #init 192.168.25.101:502   
    fan1 = Fan(xknx,
              'Lama1',
              group_address='5/0/226',
              group_address_state='5/0/237',
              #group_address_oscillation='1/2/3',
              #group_address_oscillation_state='1/2/4'
              device_updated_cb=lama1.updated_cb)
    
    #lama_1 = Lama    
