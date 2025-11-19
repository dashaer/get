import smbus
import time 
import RPi.GPIO as GPIO
import numpy as np

GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.IN)
# GPIO.setup(self.comp_gpio,GPIO.IN)

while True:
    if GPIO.input(15)==1:
        print (1)
    else:
        print(0)
time_values=[1,2,3]
voltage_values=[3,4,5]

# data=np.column_stack((time_values,voltage_values))
# print (data)
# np.savetxt('x.csv', data, delimiter=',', fmt='%4f', header='время[c],напряжение[В]',comments='',encoding='utf-8') 


# with open('col_20.csv','w') as f:
#     for i in data:
#         # print(i)
#         a,b=i
#         # print(a,b)
#         l=str(a)+','+str(b)
#         print(l)
#         f.write(l)
#         f.write('\n')
        
# # f=open('calibration.csv')
