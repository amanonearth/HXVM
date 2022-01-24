from turtle import color
from rating import *
import time
from rich.progress import Progress
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt


def choicepy():
    vmnum = Prompt.ask("[+] How many Virtual Machines do you want to run on your system? ", choices=["1", "2", "3", "4", "5"])
    # vmnum = input("[+] How many Virtual Machines do you want to run on your system? ")
    vmnumint = int(vmnum)
    print("\n")
    if vmnumint <= 5:
        table = Table(title="Virtual Machines")
        table.add_column("S. No.")
        table.add_column("VM")
        table.add_row("1", "Kali Linux/Parrot OS")
        table.add_row("2", "Windows XP/7/8/10")
        table.add_row("3", "Ubuntu")
        table.add_row("4", "CentOS")
        table.add_row("5", "Android")
        console = Console()
        console.print(table)
        print("\n")
        # print(f"Please select any " + vmnum + " options:")
        print(Panel.fit(f"Please select any " + vmnum + " options:"))

        for i in range(0, vmnumint):
            if i == 0:
                opt1 = int(input("Option 1: "))
                if int(opt1) >= 6:
                    print(Panel.fit("[red]You provided the wrong input for choice 1.\n>>> Please try again with valid input."))
                    exit(0)
            if i == 1:
                opt2 = int(input("Option 2: "))
                if int(opt2) >= 6:
                    print(Panel.fit("[red]You provided the wrong input for choice 2.\n>>> Please try again with valid input."))
                    exit(0)
            if i == 2:
                opt3 = int(input("Option 3: "))
                if int(opt3) >= 6:
                    print(Panel.fit("[red]You provided the wrong input for choice 3.\n>>> Please try again with valid input."))
                    exit(0)
            if i == 3:
                opt4 = int(input("Option 4: "))
                if int(opt4) >= 6:
                    print(Panel.fit("[red]You provided the wrong input for choice 4.\n>>> Please try again with valid input."))
                    exit(0)
            if i == 4:
                opt5 = int(input("Option 5: "))
                if int(opt5) >= 6:
                    print(Panel.fit("[red]You provided the wrong input for choice 5.\n>>> Please try again with valid input."))
                    exit(0)         
            


        if vmnumint <= rating:
            with Progress() as progress:
                task01 = progress.add_task("[red]Getting system information...", total=100)
                while not progress.finished:
                    progress.update(task01, advance=0.7)
                    time.sleep(0.02)
            with Progress() as progress:
                task02 = progress.add_task("[red]Evaluating the system hardware...", total=100)
                while not progress.finished:
                    progress.update(task02, advance=0.9)
                    time.sleep(0.02)
            with Progress() as progress:
                task03 = progress.add_task("[red]Comparing the VM(s) requirement with your system...", total=100)
                while not progress.finished:
                    progress.update(task03, advance=0.7)
                    time.sleep(0.02)
            with Progress() as progress:
                task04 = progress.add_task("[magenta]Preparing the result...", total=100)
                while not progress.finished:
                    progress.update(task04, advance=0.5)
                    time.sleep(0.02)
            with Progress() as progress:
                task05 = progress.add_task("[green]Almost Done...", total=100)
                while not progress.finished:
                    progress.update(task05, advance=0.2)
                    time.sleep(0.002)
            print(Panel.fit(f"[green][*] You Can run " + vmnum + " Virtual Machine without any problem!!"))

            
        else:
            with Progress() as progress:
                task01 = progress.add_task("[red]Getting system information...", total=100)
                while not progress.finished:
                    progress.update(task01, advance=0.7)
                    time.sleep(0.02)
            with Progress() as progress:
                task02 = progress.add_task("[red]Evaluating the system hardware...", total=100)
                while not progress.finished:
                    progress.update(task02, advance=0.9)
                    time.sleep(0.02)
            with Progress() as progress:
                task03 = progress.add_task("[red]Comparing the VM(s) requirement with your system...", total=100)
                while not progress.finished:
                    progress.update(task03, advance=0.7)
                    time.sleep(0.02)
            with Progress() as progress:
                task04 = progress.add_task("[magenta]Preparing the result...", total=100)
                while not progress.finished:
                    progress.update(task04, advance=0.5)
                    time.sleep(0.02)
            with Progress() as progress:
                task05 = progress.add_task("[green]Almost Done...", total=100)
                while not progress.finished:
                    progress.update(task05, advance=0.2)
                    time.sleep(0.002)
            print(Panel.fit(f"\n[red][*] Your machine is not capable of running " + vmnum + " Virtual Machines!\n"))
            print(Panel.fit(f"[green][*] Recommendation: You can run " + ratingstr + " Virtual Machine(s) without any problem!!\n"))

    else:
        print(Panel.fit("[red]Your choosen option is not a valid input.\nPlease try again with valid input."))
