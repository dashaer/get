import smbus

class MCP4725:
    def __init__(self,dynamic_range,address=0x61,verbose=True):
        self.bus=smbus.SMBus(1)
        self.address=address
        self.wm=0x00
        self.pds=0x00

        self.verbose=verbose
        self.dynamic_range=dynamic_range


        # GPIO.setmod(GPIO.BCM)
        # GPIO.setup(self.gpio_bits, GPIO.OUT, intentional=0)

    def deinit(self):
        self.bus.close()
    
    def set_number(self,number):
        if not isinstance(number,int):
            print("на вход ЦАП можно подавать только целые числа")

        if not(0<= number<=4095):
            print("число выходит за разрядность MCP4752 (12 бит)")

        first_byte = self.wm | self.pds | number >>8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number} , отправленные по I2C данные: [0x{(self.address<<1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")

    def set_voltage(self,voltage):
        DR=self.dynamic_range
        if not(0.0<= voltage <= DR):
            print(f"напряжение выходит за динамический диапазон ЦАП (0.00 - {DR:.2f} B)")
            print("устанавливаем 0.0 B")
            return 0
        self.set_number(int((voltage/DR)*4095))



if __name__ == "__main__":
    try:
        dac=MCP4725(5.1)
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввли не число. Попробуйте еще раз\n")

    finally:
        dac.deinit()