from info import *
from choice import *
from rich.console import Console
from rich.table import Table
import time
from rich import print
from rich.panel import Panel
from rich.progress import Progress

def banner():
    print(r"""
     _   ___  ____     ____  __         _   _ 
    | | | \ \/ /\ \   / /  \/  | __   _/ | / |
    | |_| |\  /  \ \ / /| |\/| | \ \ / / | | |
    |  _  |/  \   \ V / | |  | |  \ V /| |_| | - Check your host compatibility for VMs
    |_| |_/_/\_\   \_/  |_|  |_|   \_/ |_(_)_|
    """)
    print(Panel("Copyright of Aman Srivastava, 2022\nhttps://amanonearth.github.io\nhttps://amanonearth.medium.com ", title="Welcome", subtitle="Thank you"))

def main():

    homeopt = int(input("Please enter your option: "))

    if homeopt == 1:
        with Progress() as progress:
            task01 = progress.add_task("[green]Gathering System Information...", total=100)
            while not progress.finished:
                progress.update(task01, advance=0.7)
                time.sleep(0.02)
        sysinfo()
    if homeopt == 2:
        with Progress() as progress:
            task02 = progress.add_task("[green]Gathering CPU Information...", total=100)
            while not progress.finished:
                progress.update(task02, advance=0.9)
                time.sleep(0.02)
        cpuinfo()
    if homeopt == 3:
        with Progress() as progress:
            task03 = progress.add_task("[green]Gathering RAM Information...", total=100)
            while not progress.finished:
                progress.update(task03, advance=0.6)
                time.sleep(0.02)
        raminfo()
    if homeopt == 4:
        with Progress() as progress:
            task04 = progress.add_task("[green]Gathering Disk Information...", total=100)
            while not progress.finished:
                progress.update(task04, advance=0.5)
                time.sleep(0.02)
        diskinfo()
    if homeopt == 5:
        with Progress(transient=True) as progress:
            task1 = progress.add_task("[green]Gathering System Information...", total=100)
            task2 = progress.add_task("[green]Gathering CPU Information...", total=100)
            task3 = progress.add_task("[green]Gathering RAM Information...", total=100)
            task4 = progress.add_task("[green]Gathering Disk Information...", total=100)
            while not progress.finished:
                progress.update(task1, advance=0.7)
                progress.update(task2, advance=0.9)
                progress.update(task3, advance=0.6)
                progress.update(task4, advance=0.5)
                time.sleep(0.02)
        allinfo()
    if homeopt == 6:
        choicepy()
    if homeopt >= 7:
        print(Panel.fit("[red]Your choosen option is not a valid input.\nPlease try again with valid input."))

if __name__ == "__main__":
    banner()
    print("\n")
    table = Table()
    table.add_column("S. No.")
    table.add_column("Option", style="green")
    table.add_row("1", "Get your System Information")
    table.add_row("2", "Get CPU Information")
    table.add_row("3", "Get RAM Information")
    table.add_row("4", "GET Disk Information")
    table.add_row("5", "Get All information mentioned above")
    table.add_row("6", "Check Virtual Machine Compatibility")
    console = Console()
    console.print(table)
    main()