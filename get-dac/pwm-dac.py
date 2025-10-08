import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self,gpio_pin,pwm_ferequency,dynamic_range,verbose=False):
        self.gpio_bits=gpio_pin
        self.pwm_ferequency=pwm_ferequency
        self.dynamic_range=dynamic_range
        self.verbose=verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits,GPIO.OUT,initial=0)
        
        self.pwm=GPIO.PWM(self.gpio_bits,self.pwm_ferequency)
        self.pwm.start(0)




    def set_voltage(self,voltage):
        DR=self.dynamic_range
        if not(0.0<= voltage <= DR):
            print(f"напряжение выходит за динамический диапазон ЦАП (0.00 - {DR:.2f} B)")
            print("устанавливаем 0.0 B")
            return 0
        # self.set_number(int((voltage / DR)*255))
        
        duty_max=(voltage/self.dynamic_range)*100
        self.pwm.ChangeDutyCycle(duty_max)

    def deinit(self):
        self.pwm.stop()
        GPIO.output(self.gpio_bits,0)
        GPIO.cleanup()





if __name__ == "__main__":
    try:
        dac=PWM_DAC(12,500,3.2,True)
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввли не число. Попробуйте еще раз\n")

    finally:
        dac.deinit()