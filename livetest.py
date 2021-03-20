import rich
from rich import print
from rich.text import Text
from socket import create_connection
from umodbus import conf
from umodbus.client import tcp

def bits(number: int = 0):
    ''' Devuelve los bits de un registro modbus (2 bytes)
    '''
    for i in range(16):
        yield (number >> i) & 1

sconspos = 'OPM1 OPM2 FCT VLoad Fault Warn Op_En Enable Ref Still FolErr Mov Teach MC ACK Halt'
cconcpos = 'OPM1 OPM2 Lock - Reset Brake Stop Enable - Clear Teach JogN JogP Hom Start Halt'
bits_text = sconspos.split()
sconspos_textos = [f'{b:^6}' for b in bits_text]
bits_text = cconcpos.split()
cconcpos_textos = [f'{b:^6}' for b in bits_text]

class LamaTest(object):
    S_HALT = C_HALT = 0b0000000000000001
    S_ACK = C_START = 0b0000000000000010
    S_MC = C_HOM = 0b0000000000000100
    S_TEACH = C_JOGP = 0b00000000000001000
    S_MOV = C_JOGN = 0b0000000000010000
    S_FOLERR = C_TEACH = 0b0000000000100000
    S_STILL = C_CLEAR = 0b0000000001000000
    S_REF = C_NULL = 0b0000000010000000
    S_ENABLED = C_ENABLE = 0b0000000100000000
    S_OPEN = C_STOP = 0b0000001000000000
    S_WARN = C_BRAKE = 0b0000010000000000
    S_FAULT = C_RESET = 0b0000100000000000
    S_VLOAD = C_NULL2 = 0b0001000000000000
    S_FCT = C_LOCK = 0b0010000000000000
    S_OPM1 = C_OPM1 = 0b0100000000000000
    S_OPM2 = C_OPM2 = 0b1000000000000000
        
    def __init__(self, client_ip, client_port):
        #super(Lama, self).__init__(*args)
        #incluir argumentos para inicializar la lama modbusTCP, IP:port
        self._input_regs = [0, 0, 0, 0]  # SPOS SCON
        self._output_regs = [0, 0, 0, 0]  # CPOS CCON
        self.position = 0
        self.ip = client_ip
        self.port = client_port

    def __str__(self) -> str:
        global sconspos_textos, cconcpos_textos
        me_sconspos = ''
        me_cconcpos = ''
        for i,bit in enumerate(bits(self._input_regs[0])):
            if bit:
                me_sconspos += f'[bright_white]{sconspos_textos[i]}[/]'
            else:
                me_sconspos += f'[blue]{sconspos_textos[i]}[/]'
        for i,bit in enumerate(bits(self._output_regs[0])):
            if bit:
                me_cconcpos += f'[bright_white]{cconcpos_textos[i]}[/]'
            else:
                me_cconcpos += f'[blue]{cconcpos_textos[i]}[/]'
        me_position = self.position
        me_str = f'SCONSPOS:{me_sconspos}\n'+f'CCONCPOS:{me_cconcpos}\n'+f'POS:{me_position}'
        return me_str

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value: int):
        self._position = value
        self._output_regs[1] = value << 8

        # Get the status bits
    def is_HALT(self) -> bool:
        return bool(self._input_regs[0] & LamaTest.S_HALT) 

    def is_ACK(self) -> bool:
        return bool(self._input_regs[0] & LamaTest.S_ACK)

    def is_MC(self) -> bool:
        return bool(self._input_regs[0] & LamaTest.S_MC)

    def is_TEACH(self) -> bool:
        return bool(self._input_regs[0] & LamaTest.S_TEACH)
    
    def is_MOV(self) -> bool:
        return bool(self._input_regs[0] & LamaTest.S_MOV)
    
    def is_FOLERR(self) -> bool:
        return bool(self._input_regs[0] & LamaTest.S_FOLERR)

    def is_STILL(self) -> bool:
        return bool(self._input_regs[0] & LamaTest.S_STILL)
    
    def is_REF(self) -> bool:
        return bool(self._input_regs[0] & LamaTest.S_REF)

    def is_ENABLED(self) -> bool:
        return bool(self._input_regs[0] & LamaTest.S_ENABLED)

    def is_OPEN(self) -> bool:
        return bool(self._input_regs[0] & LamaTest.S_OPEN)

    def is_WARN(self) -> bool:
        return bool(self._input_regs[0] & LamaTest.S_WARN)

    def is_FAULT(self) -> bool:
        return bool(self._input_regs[0] & LamaTest.S_FAULT)

    def is_VLOAD(self) -> bool:
        return bool(self._input_regs[0] & LamaTest.S_VLOAD)

    def is_FCT(self) -> bool:
        return bool(self._input_regs[0] & LamaTest.S_FCT)

    def is_OPM1(self) -> bool:
        return bool(self._input_regs[0] & LamaTest.S_OPM1)

    def is_OPM2(self) -> bool:
        return bool(self._input_regs[0] & LamaTest.S_OPM2)

    # Set bits for operation
    def set_bit(self, bit_to_set: int, bit_value: bool):
        # HALT START
        if bit_value:
            self._output_regs[0] |= bit_to_set
        else:
            self._output_regs[0] &= ~bit_to_set
            
    def set_HALT(self, setbit: bool) -> None:
        self.set_bit(LamaTest.C_HALT, setbit)

    def set_START(self, setbit: bool) -> None:
       self.set_bit(LamaTest.C_START, setbit)
       
    def set_HOM(self, setbit: bool) -> None:
        self.set_bit(LamaTest.C_HOM, setbit)

    def set_JOGP(self, setbit: bool) -> None:
        self.set_bit(LamaTest.C_JOGP, setbit)

    def set_JOGN(self, setbit: bool) -> None:
        self.set_bit(LamaTest.C_JOGN, setbit)

    def set_TEACH(self, setbit: bool) -> None:
        self.set_bit(LamaTest.C_TEACH, setbit)

    def set_CLEAR(self, setbit: bool) -> None:
        self.set_bit(LamaTest.C_CLEAR, setbit)

    def set_ENABLE(self, setbit: bool) -> None:
        self.set_bit(LamaTest.C_ENABLE, setbit)

    def set_STOP(self, setbit: bool) -> None:
        self.set_bit(LamaTest.C_STOP, setbit)

    def set_BRAKE(self, setbit: bool) -> None:
        self.set_bit(LamaTest.C_BRAKE, setbit)

    def set_RESET(self, setbit: bool) -> None:
        self.set_bit(LamaTest.C_RESET, setbit)

    def set_LOCK(self, setbit: bool) -> None:
        self.set_bit(LamaTest.C_LOCK, setbit)

    def set_OPM1(self, setbit: bool) -> None:
        self.set_bit(LamaTest.C_OPM1, setbit)

    def set_OPM2(self, setbit: bool) -> None:
        self.set_bit(LamaTest.C_OPM2, setbit)
    
    def set_clear(self) -> None:
        self._output_regs=[0,0,0,0]
    
    def read(self, client):
        message = tcp.read_holding_registers(slave_id=1, starting_address=0, quantity=4)
        print(type(message))
        print(message)
        response = tcp.send_message(message, client)
        print(type(response))
        print(response)
        self._input_regs=response
    
    def write(self, client):
        message = tcp.write_multiple_registers(slave_id=1, starting_address=0, values=self._output_regs)    
        print(type(message))
        print(message)
        response = tcp.send_message(message, client)
        print(type(response))
        print(response)
            
    def move_to_pos(self, pos: int) -> int:
        # activate pos
        self.set_clear()
        self.position = pos
        self.set_ENABLE(True)
        self.set_STOP(True)
        with create_connection(address=(self.ip, self.port)) as con:
            self.read(con)
            print(Text.from_markup(str(self)))            
            self.write(con)
            print(Text.from_markup(str(self)))            
            self.read(con)
            print(Text.from_markup(str(self)))            
            self.set_ENABLE(False)
            self.write(con)
            print(Text.from_markup(str(self)))            
            self.read(con)
            print(Text.from_markup(str(self)))            
            #while not self.is_HALT():
            #    await self.read(con)
    
    

lama_1 = LamaTest('192.168.25.101', 502) #init 192.168.25.101:502   
print(Text.from_markup(str(lama_1)))
lama_1.move_to_pos(1)