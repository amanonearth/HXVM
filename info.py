import platform
from xml.etree.ElementPath import ops
import psutil
import shutil
from rich.console import Console
from rich.table import Table


# System Information

comp_name = platform.node()
mach_type = platform.machine()
proc_type = platform.processor()
plat_type = platform.platform()


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
    print("\n")
    table = Table(title="System Information")
    table.add_column("Description")
    table.add_column("Value", style="green")
    table.add_row("Computer Name ", comp_name)
    table.add_row("Operating System ", plat_type)
    table.add_row("Machine Type", mach_type)
    table.add_row("Processor Type", proc_type)
    console = Console()
    console.print(table)
    print("\n")

def cpuinfo():
    print("\n")
    table = Table(title="CPU Information")
    table.add_column("Description")
    table.add_column("Value", style="green")
    table.add_row("Total Number of Physical Cores ", phy_cores)
    table.add_row("Total Number of Logical Cores ", log_cores)
    table.add_row("Current CPU Frequency ", cpu_freq_current + " GHz")
    table.add_row("Current CPU Utilisation ", cpu_util_current + "%")
    console = Console()
    console.print(table)
    print("\n")

def raminfo():
    print("\n")
    table = Table(title="RAM Information")
    table.add_column("Description")
    table.add_column("Value", style="green")
    table.add_row("Total RAM Installed ", ram_total_str + " GiB")
    table.add_row("Total RAM Used ", ram_used_str + " GiB")
    table.add_row("Current RAM Avaialable ", ram_avail_str + " GiB")
    table.add_row("Current RAM Usage ", ram_usage_str + "%")
    console = Console()
    console.print(table)
    print("\n")

def diskinfo():
    print("\n")
    table = Table(title="Disk Information")
    table.add_column("Description")
    table.add_column("Value", style="green")
    table.add_row("Total Disk Installed ", disk_total_str + " GiB")
    table.add_row("Total Disk Used ", disk_used_str + " GiB")
    table.add_row("Current Disk Avaialable ", disk_free_str + " GiB")
    console = Console()
    console.print(table)
    print("\n")

def allinfo():
    print("\n")
    table = Table(title="All Information")
    table.add_column("Description")
    table.add_column("Value", style="green")
    table.add_row("Computer Name ", comp_name)
    table.add_row("Operating System ", plat_type)
    table.add_row("Machine Type", mach_type)
    table.add_row("Processor Type", proc_type)
    table.add_row("Total Number of Physical Cores ", phy_cores)
    table.add_row("Total Number of Logical Cores ", log_cores)
    table.add_row("Current CPU Frequency ", cpu_freq_current + " GHz")
    table.add_row("Current CPU Utilisation ", cpu_util_current + "%")
    table.add_row("Total RAM Installed ", ram_total_str + " GiB")
    table.add_row("Total RAM Used ", ram_used_str + " GiB")
    table.add_row("Current RAM Avaialable ", ram_avail_str + " GiB")
    table.add_row("Current RAM Usage ", ram_usage_str + "%")
    table.add_row("Total Disk Installed ", disk_total_str + " GiB")
    table.add_row("Total Disk Used ", disk_used_str + " GiB")
    table.add_row("Current Disk Avaialable ", disk_free_str + " GiB")
    console = Console()
    console.print(table)
    print("\n")
