import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self,gpio_bits,dynamic_range,verbose= False):
        self.gpio_bits=gpio_bits
        self.dynamic_range=dynamic_range
        self.verbose=verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits,GPIO.OUT,initial=0)

    def deinit(self):
        GPIO.output(self.gpio_bits,0)
        GPIO.cleanup()

    def set_number(self,number):
        number_bin=[int(e) for e in bin(number)[2:].zfill(8)]
        for i in range(8):
            GPIO.output(self.gpio_bits[i],int(number_bin[i]))
        # print(num_bin)

    def set_voltage(self,voltage):
        DR=self.dynamic_range
        if not(0.0<= voltage <= DR):
            print(f"напряжение выходит за динамический диапазон ЦАП (0.00 - {DR:.2f} B)")
            print("устанавливаем 0.0 B")
            return 0
        # print(int(voltage/DR *255))
        self.set_number(int((voltage / DR)*255))



if __name__ == "__main__":
    try:
        dac=R2R_DAC([26,20,19,16,13,12,25,11],3.15,True)
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввли не число. Попробуйте еще раз\n")

    finally:
        dac.deinit()