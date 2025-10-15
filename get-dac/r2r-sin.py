import r2r_dac as r2r
# import numpy as np
import signal_generator as sg

import time

amplitude = 3.2
amplitude_new = 1
signal_frequency=10.0
sampling_ferquency = 1000

try:
    dac=r2r.R2R_DAC([16,20,21,25,26,17,27,22],amplitude,True)
    while True:
        try:
            voltage = sg.get_sin_wave_amplitude(signal_frequency,time.time())
            dac.set_voltage((amplitude_new/amplitude)*voltage)
        except ValueError:
            pass
finally:
    dac.deinit()
