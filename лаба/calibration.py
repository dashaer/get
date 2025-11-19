import mcp3021_driver 
import adc_plot
import numpy as np
import smbus
import time 
import RPi.GPIO as GPIO

# # dac =r2r_adc.R2R_ADC(dynamic_range)
v=mcp3021_driver.MCP3021(5,True)


# voltage_values = []
# time_values = []
# duration = 20.0
# dynamic_range=5



# time_start=time.time()

# while time.time()-time_start < duration:
#     voltage_values.append(v.get_voltage())
#     time_values.append(time.time()-time_start)

# print(time_values)
# print(voltage_values)
# adc_plot.plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
# # adc_plot.plot_sampling_period_hist(time_values)


# data=np.column_stack((time_values,voltage_values))
# np.savetxt('col_120.csv', data, delimiter=',', fmt='%4f', header='время[c],напряжение[В]',comments='',encoding='utf-8') 

def f():
    voltage_values = []
    time_values = []
    duration = 15.0
    dynamic_range=5



    time_start=time.time()

    while time.time()-time_start < duration:
        voltage_values.append(v.get_voltage())
        time_values.append(time.time()-time_start)

    print(time_values)
    print(voltage_values)
    adc_plot.plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
    # adc_plot.plot_sampling_period_hist(time_values)


    data=np.column_stack((time_values,voltage_values))
    np.savetxt('exp_40_csv', data, delimiter=',', fmt='%4f', header='время[c],напряжение[В]',comments='',encoding='utf-8') 



GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.IN)
# GPIO.setup(self.comp_gpio,GPIO.IN)

while True:
    if GPIO.input(15)==0:
        f()
        # print(0)
        break
    else:
        print(1)

