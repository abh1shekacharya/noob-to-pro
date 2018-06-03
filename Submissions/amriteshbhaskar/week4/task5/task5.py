import platform
import psutil
import os
import math

pName = platform.uname()
print('Tell me Something about my System..')
print('\nYou are Using ' + pName.system + ' ' + pName.node + ' Operating System. which is having Processor ' + pName.processor)
print('and it is running on ' + platform.architecture()[0] + ' Architecture with ' + str(psutil.cpu_count()) + ' cores Active\n')

battery = psutil.sensors_battery()
print('What about Battery!??')
print('Your Battery is ' + str(math.floor(battery[0])) + '% Charged right now!')
if(battery[2] == True):
    print('and it\'s increasing too as your laptop is still charging!!')
    if(math.ceil(battery[0]) == 100):
        print('I think you should unplug your charger as your PC is full charged')
print()

mem = psutil.virtual_memory()
print('How much memory has been used??')
print(str(math.floor(mem.percent)) +'% of memory has been used.\n')

perc = str(psutil.cpu_percent())
print('Tell me some another stuff!!')
print('Current CPU usage is ' + perc + '%')
print('This Program takes about', end=' ')
print(psutil.Process(os.getpid()).memory_info().rss/float(2**20), end='')
print(' MiB of memory for running')