import numpy as np
import time

def get_sin_wave_amplitude(freq, time_signal):
    d=(1+np.sin(2*np.pi*freq*time_signal))/2
    return d


def wait_for_sampling(sempling_ferquency):
    time.sleep(1/sempling_ferquency)
    return
