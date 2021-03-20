import asyncio
import os
#from xknx import XKNX
#from xknx.devices import Fan 
import rich
from rich import print
from rich.text import Text
import lama
from lama import LamaModbusTCP

async def show_status(lama):
    while True:
        await asyncio.sleep(0)
        os.system('clear')
        await asyncio.sleep(0)
        print(Text.from_markup(str(lama)))
        await asyncio.sleep(0)

async def main():
    #xknx = XKNX(config='xknx.yaml', daemon_mode=True)
    lama_1 = LamaModbusTCP('192.168.25.101', 502) #init 192.168.25.101:502   
    
    await lama_1.move_to_pos(6)
    await asyncio.sleep(5)
    await lama_1.move_to_pos(1)
    
    
    
    '''
    fan1 = Fan(xknx,
              'Lama1',
              group_address='5/0/226',
              group_address_state='5/0/237',
              #group_address_oscillation='1/2/3',
              #group_address_oscillation_state='1/2/4'
              device_updated_cb=lama1.updated_cb)
    
    #lama_1 = Lama    
    '''

if __name__ == "__main__":
    asyncio.run(main())