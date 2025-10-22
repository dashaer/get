import r2r_adc
import time
import adc_plot

voltage_values = []
time_values = []
duration = 5.0


dynamic_range = 3.2

dac =r2r_adc.R2R_ADC(dynamic_range)

time_start=time.time()

while time.time()-time_start < duration:
    voltage_values.append(dac.sequential_counting_adc())
    time_values.append(time.time()-time_start)

print(time_values)
print(voltage_values)
adc_plot.plot_voltage_vs_time(time_values, voltage_values, dynamic_range)