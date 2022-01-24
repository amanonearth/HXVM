import platform
import psutil
import shutil
import numpy as np


# System Information

comp_name = platform.node()
mach_type = platform.machine()
proc_type = platform.processor()
plat_type = platform.platform()
op_system = platform.system()
op_system_release = platform.release()
op_system_ver = platform.version()


# CPU Usage

phy_cores = str(psutil.cpu_count(logical=False))
log_cores = str(psutil.cpu_count(logical=True))
cpu_freq_current = str(psutil.cpu_freq().current / 1000)
cpu_util_current = str(psutil.cpu_percent(interval=1))


# RAM Usage

ram_total = round(psutil.virtual_memory().total/1000000000, 2)
ram_avail = round(psutil.virtual_memory().available/1000000000, 2)
ram_used = round(psutil.virtual_memory().used/1000000000, 2)
ram_usage = psutil.virtual_memory().percent

ram_total_str = str(ram_total)
ram_avail_str = str(ram_avail)
ram_used_str = str(ram_used)
ram_usage_str = str(ram_usage)


# Disk Information

disk_total = shutil.disk_usage("/").total // (2**30)
disk_used = shutil.disk_usage("/").used // (2**30)
disk_free = shutil.disk_usage("/").free // (2**30)

disk_total_str = str(disk_total)
disk_used_str = str(disk_used)
disk_free_str = str(disk_free)

# Functions to get information

def sysinfo():
    print(f"Your Computer Name is : " + comp_name)
    print(f"Your Operating System is : " + op_system)
    print(f"Your Operating System Version is : " + op_system_ver)

def cpuinfo():
    print(f"Total Number of Physical Cores : " + phy_cores)
    print(f"Total Number of Logical Cores : " + log_cores)
    print(f"Current CPU Frequency : " + cpu_freq_current + " GHz")
    print(f"Current CPU Utilisation : " + cpu_util_current + "%")

def raminfo():
    print(f"Total RAM Installed : " + ram_total_str + " GiB")
    print(f"Total RAM Used : " + ram_used_str + " GiB")
    print(f"Current RAM Avaialable : " + ram_avail_str + " GiB")
    print(f"Current RAM Usage : " + ram_usage_str + "%")

def diskinfo():
    print(f"Total Disk Installed : " + disk_total_str + " GiB")
    print(f"Total Disk Used : " + disk_used_str + " GiB")
    print(f"Current Disk Avaialable : " + disk_free_str + " GiB")