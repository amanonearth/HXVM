from info import *
from choice import *

print("   Welcome!!\n Here are the options you can choose to begin with:\n 1. Get your system information\n 2. Get CPU information\n 3. Get RAM information\n 4. GET Disk Information\n 5. Get all information\n 6. Check Virtual Machine Compatibility\n")

homeopt = int(input("Please enter your option: "))

# Calling the function

if homeopt == 1:
    sysinfo()
if homeopt == 2:
    cpuinfo()
if homeopt == 3:
    raminfo()
if homeopt == 4:
    diskinfo()
if homeopt == 5:
    sysinfo()
    cpuinfo()
    raminfo()
    diskinfo()
if homeopt == 6:
    choicepy()
