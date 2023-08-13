from Bookcaze import *
from datetime import datetime
from user import *
from rich import print
from art import tprint
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
console = Console()
Subs = [
                   {"Month":1,"Price SR":19.99},
                   {"Month":3,"Price SR":29.99},
                   {"Month":6,"Price SR":59.99},
                   {"Month":12,"Price SR":89.99},
              
        ]
tempsubs = []
def Plans():
    check = True
    while check != False:
        p1 = Panel(Text("Choose your plan 😄 ! (month '1' - 3 months '3' - 6 months '6' 12 months '12')",justify="center",style="#75B13E"))
        print(p1)
        print(tabulate(Subs, headers="keys", tablefmt="mixed_outline"))
        choose_plan = int(input())
        if choose_plan == 1 or choose_plan == 3 or choose_plan == 6 or choose_plan == 12:
                for s in Subs:
                    if s["Month"] == choose_plan :
                        if s in tempsubs:
                            print("Can't add more than one!")
                        else:
                            tempsubs.append(s)
                            print(tabulate(tempsubs, headers="keys", tablefmt="mixed_outline"))


                        while check:
                            now = datetime.now()
                            ff = open("subscribers.txt","a+")
                            console.print("~ Please Enter your Username to subscribe!\n",style="bold underline red on white")
                            username2 = input()
                            console.print("~ Please Enter your password!\n",style="bold underline red on white")
                            password2 = input()
                            ff.write(f"\nUsername:{username2} Password:{password2}\nTime:{now}\n")
                            ff.close()
                            acc = open("accountfile.txt","a+")
                            acc.write(f"\nUsername:{username2} Password:{password2}\nTime:{now}\n")
                            acc.close()
                            tprint("Welcome   to   BookCaze")
                            print(tabulate(bookcaze, headers="keys", tablefmt="mixed_outline"))
                            OurEbooks()
                            check = False
                            break