import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency=10.0
sampling_ferquency = 1000

try:
    dac=pwm.PWM_DAC(12,500,amplitude,True)
    while True:
        try:
            voltage = sg.get_sin_wave_amplitude(signal_frequency,time.time())
            dac.set_voltage(voltage)
        except ValueError:
            pass
finally:
    dac.deinit()
