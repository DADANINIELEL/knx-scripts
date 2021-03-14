import asyncio

class Lama(object):
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
    
    def __init__(self, *args):
        super(Lama, self).__init__(*args)
        self._input_regs = [0, 0]  # SPOS SCON
        self._output_regs = [0, 0]  # CPOS CCON
        self.position = 0
     
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value: int):
        self._position = value
        self._output_regs[1] = value << 8
            
    # Get the status bits
    def is_HALT(self) -> bool:
        return bool(self._input_regs[0] & Lama.S_HALT) 

    def is_ACK(self) -> bool:
        return bool(self._input_regs[0] & Lama.S_ACK)

    def is_MC(self) -> bool:
        return bool(self._input_regs[0] & Lama.S_MC)

    def is_TEACH(self) -> bool:
        return bool(self._input_regs[0] & Lama.S_TEACH)
    
    def is_MOV(self) -> bool:
        return bool(self._input_regs[0] & Lama.S_MOV)
    
    def is_FOLERR(self) -> bool:
        return bool(self._input_regs[0] & Lama.S_FOLERR)

    def is_STILL(self) -> bool:
        return bool(self._input_regs[0] & Lama.S_STILL)
    
    def is_REF(self) -> bool:
        return bool(self._input_regs[0] & Lama.S_REF)

    def is_ENABLED(self) -> bool:
        return bool(self._input_regs[0] & Lama.S_ENABLED)

    def is_OPEN(self) -> bool:
        return bool(self._input_regs[0] & Lama.S_OPEN)

    def is_WA
    Lama.S_WARN)

    def is_FAULT(self) -> bool:
        return bool(self._input_regs[0] & Lama.S_FAULT)

    def is_VLOAD(self) -> bool:
        return bool(self._input_regs[0] & Lama.S_VLOAD)

    def is_FCT(self) -> bool:
        return bool(self._input_regs[0] & Lama.S_FCT)

    def is_OPM1(self) -> bool:
        return bool(self._input_regs[0] & Lama.S_OPM1)

    def is_OPM2(self) -> bool:
        return bool(self._input_regs[0] & Lama.S_OPM2)

    # Set bits for operation
    def set_bit(self, bit_to_set: int, bit_value: bool):
        # HALT START
        if bit_value:
            self._output_regs[0] |= bit_to_set
        else:
            self._output_regs[0] &= ~bit_to_set
            
    def set_HALT(self, setbit: bool) -> None:
        self.set_bit(Lama.C_HALT, setbit)

    def set_START(self, setbit: bool) -> None:
       self.set_bit(Lama.C_START, setbit)
       
    def set_HOM(self, setbit: bool) -> None:
        self.set_bit(Lama.C_HOM, setbit)

    def set_JOGP(self, setbit: bool) -> None:
        self.set_bit(Lama.C_JOGP, setbit)

    def set_JOGN(self, setbit: bool) -> None:
        self.set_bit(Lama.C_JOGN, setbit)

    def set_TEACH(self, setbit: bool) -> None:
        self.set_bit(Lama.C_TEACH, setbit)

    def set_CLEAR(self, setbit: bool) -> None:
        self.set_bit(Lama.C_CLEAR, setbit)

    def set_ENABLE(self, setbit: bool) -> None:
        self.set_bit(Lama.C_ENABLE, setbit)

    def set_STOP(self, setbit: bool) -> None:
        self.set_bit(Lama.C_STOP, setbit)

    def set_BRAKE(self, setbit: bool) -> None:
        self.set_bit(Lama.C_BRAKE, setbit)

    def set_RESET(self, setbit: bool) -> None:
        self.set_bit(Lama.C_RESET, setbit)

    def set_LOCK(self, setbit: bool) -> None:
        self.set_bit(Lama.C_LOCK, setbit)

    def set_OPM1(self, setbit: bool) -> None:
        self.set_bit(Lama.C_OPM1, setbit)

    def set_OPM2(self, setbit: bool) -> None:
        self.set_bit(Lama.C_OPM2, setbit)
    
    async def quitar_freno(self):
        #disable and disable brake
        self.set_ENABLE(False)
        self.set_BRAKE(False)
        await asyncio.sleep(1)
    
    async def move_to_pos(self, pos: int) -> int:
        # activate pos
        self.position = pos
        await asyncio.sleep(1)
        # enable
        # stop
        # is stop?
        # set start
        # is ack?
        # set start false
        # mc complete? 
        # return pos
        
    async def clear_error(self):
        await asyncio.sleep(1)
        
    

