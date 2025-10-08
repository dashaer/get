import smbus

class MCP4725:
    def __init__(self,dynamic_range,addres=0x61,verbose=True):
        self.bus=smbus.SMBus(1)
        self.address=address
        self.wm=0x00
        self.pds=0x00

        self.verbose=verbose
        self.dynamic_range=dynamic_range

    def deinit(self):
        self.bus.close()
    
    def set_number(self,number):
        if not isinstance(number,int):
            print("на вход ЦАП можно подавать только целые числа")

        if not(0<= number<=4095):
            print("число выходит за разрядность MCP4752 (12 бит)")

        first_byte = self.wm | self.pds | number >>8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x64, first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number} , отправленные по I2C данные: [0x{(self.address<<1):02X}]\n")
