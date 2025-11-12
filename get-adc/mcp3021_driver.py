import smbus
import time 

class MCP3021:
    def __init__(self,dynamic_range,verbose=False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address=0x4D
        self.verbose = verbose

    def deinit(self):
        self.bus.close()

    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte=data >>8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"принятые данные: {data}, Старший байт: {upper_data_byte:x}, младший байт: {lower_data_byte:x},число:{number}")
        return number
    def get_voltage(self):
        n=self.get_number()
        return (n/1023)*self.dynamic_range
# *self.dynamic_range

if __name__ == "__main__":
    try:
        dac=MCP3021(3.2)
        while True:
            try:
                # dac.set_voltage(voltage)
                # V=dac.sequential_counting_adc()
                # print(V)
                V=dac.get_voltage()
                print(V)
                time.sleep(1)

            except ValueError:
                print("error")
    finally:
        dac.deinit()