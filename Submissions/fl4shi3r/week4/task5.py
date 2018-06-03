import psutil , os
print('1.Memory Information\n2.Battery Information\n3.Network Statistics\n4.Processes\n5.CPU Information')
choice = int(input("Enter your choice: "))
dictn ={1:open('/proc/meminfo').read(),2:psutil.sensors_battery(),3:open('/proc/net/dev').read(),4:len(os.listdir('/proc')),5:open('/proc/cpuinfo').read()}
print(dictn[choice])
