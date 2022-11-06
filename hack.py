from rich.progress import track
from rich.console import Console
from time import sleep
import time
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint , colored
from pyfiglet import figlet_format
from datetime import date
import getpass

console = Console()

cprint(figlet_format('HYBRID CONSOLE!', font='starwars'))

cprint(figlet_format('IRIS ONLINE', font='starwars'))



console.log(f"[green]WELCOME USER REKKUSU_9799[/green]")
today = date.today()
print("Today's date:", today)
time.sleep(1)
password=getpass.getpass(prompt="Password:",stream=None)
time.sleep(1)
console.log(f"[green]IRIS:[/green]Hello Sir")
rekkusu = colored("Rekkusu :", "red")
input(rekkusu)
time.sleep(1)
console.log(f"[green]IRIS:[/green]What can I do for You")
input(rekkusu)
time.sleep(1)
def scrape_data():
    sleep(0.1)

for _ in track(range(100), description='[green]Searching Suitable Ports... '):
    scrape_data()

datas = [1,2,3,4,5]
with console.status("[bold green]Entering Port ID...") as status:
    while datas:
        data = datas.pop(0)
        sleep(1)
        console.log(f"[green]Finish Port Scanning[/green] {data}")
    
    console.log(f'[bold][red]Done!')
time.sleep(1)
console.log(f"[green]IRIS:[/green]Sir, Entry succesful")
print("")
input(rekkusu)
time.sleep(1)
trg=str(input("Enter target Name Id:"))

for _ in track(range(100), description='[green]Scraping data'):
    scrape_data()

for _ in track(range(100), description='[green]Data Analysis'):
    scrape_data()

print("Target Found,Establishing Port connection")
a1=1
while(a1<6):
    print("FAILED!")
    print("Establishing Port...")
    a1=a1+1
    time.sleep(0.8)

print("Failed to force Entry")
print("Trying backdoor Entry")

for _ in track(range(100), description='[green]Neural Schema Analog Reading'):
    scrape_data()

print("Backdoor Entry Sucessful")
print("Entered in target:",trg,"'s backdoor...")

datas = [1,2,3,4,5]
with console.status("[bold green]Scraping data...") as status:
    while datas:
        data = datas.pop(0)
        sleep(1)
        console.log(f"[green]Finish scraping data[/green] {data}")
    
    console.log(f'[bold][red]Done!')

datas1 = [1,2,3,4,5]
with console.status("[bold green]Scraping data...") as status:
    while datas1:
        data = datas1.pop(0)
        sleep(1)
        console.log(f"[blue]Analysing Neural schema[/blue] {data}")
    
    console.log(f'[bold][red]Failed!')
    console.log(f'[bold][blue]retrying...')

for _ in track(range(100), description='[green]Retrying Neural Attack'):
    scrape_data()


datas = [1,2,3,4,5]
with console.status("[bold green]Scraping data...", spinner='aesthetic') as status:
    while datas:
        data = datas.pop(0)
        sleep(1)
        console.log(f"[green]Finish Neural controls scraping[/green] {data}")
    
    console.log(f'[bold][red]Done!')

console.log(f"[green]IRIS:[/green]Sir, System Failed to decipher hash codes")
console.log(f"[green]IRIS:[/green]Target:",trg,"seems to be advance technology")
console.log(f"[green]IRIS:[/green]Can not break FIREWALL ID:548/nano4G6FHJ&")
input(rekkusu)
time.sleep(1)
console.log(f"[green]IRIS:[/green]OK,SIR")

for _ in track(range(100), description='[green]Force System Exit'):
    scrape_data()

console.log(f"[green]IRIS:[/green]FORCE EXIT SUCESSFUL")  
console.log(f"[green]IRIS:[/green]Anything else sir")
ans = str(input(rekkusu))
time.sleep(1)
if ans in ['n', 'no']:
    console.log(f"[green]IRIS:[/green]Ok, Good Day Sir.")

else:
    console.log(f"[green]IRIS:[/green]There is a Good news, Sir")
    input(rekkusu)
    time.sleep(1)
    console.log(f"[green]IRIS:[/green]Your New York Account Has Benefit of [green]+7.2 %[/green]")
    time.sleep(0.8)
    console.log(f"[green]IRIS:[/green]Your current balance is:[green]$ 2341.54[/green]")
    input(rekkusu)
    time.sleep(1)
    console.log(f"[green]IRIS:[/green]Ok, Good Day Sir.")
    time.sleep(2)




