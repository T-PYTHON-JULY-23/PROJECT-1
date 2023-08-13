from tabulate import tabulate
from art import *
from art import *
from colorama import Fore, Back, Style
from art import tprint
from admin import *
from Subscription import *
from rich import print
from rich.panel import Panel
from rich.text import Text
class Ebookcaze:
    tprint("..............................BookCaze............................")
    def main():
        try:
            ch = 0
            while ch != 3:


                pan = Panel(Text(f"Enter {1} for Admin or Enter {2} for User", justify="center",style="#af00ff"))                
                print(pan)
                ch = int(input())
                if ch == 1:
                    admin()
                elif ch == 2:
                    account()
                elif ch == 3:
                    break  
        except ValueError:
            pass
def display():
    obj= Ebookcaze
    obj.main()

display()