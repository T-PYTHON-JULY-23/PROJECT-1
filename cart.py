from tabulate import tabulate
from Bookcaze import *
from Subscription import *
import json
from datetime import datetime
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
console = Console()
def buyOrder():
    A = 0
    temp2=[]
    while A != 9:  
        print('[1] add to cart')
        print('[2] remove from cart')
        print('[3] display cart')
        console.print("Choose from the list: ",style="bold underline red on white")
        A = int(input())  
        if A==1:
            print(tabulate(bookcaze, headers="keys", tablefmt="mixed_outline"))
            buy_id = 0
            while buy_id != 9:
                buy_id = int(input("\nEnter Book ID: "))
                console.print("press 9 to EXIT: ",style="bold underline red on black")


                for d in bookcaze:
                    if d["Id"] == buy_id:
                        if d in temp2:
                            console.print("You Added this book!",style="bold underline red on black")
                        else:
                            temp2.append(d)
                            with open('cart.json','w') as f:
                                    myjson=json.dump(temp2, f,indent=4)
                    try:
                        total = 0
                        for p in temp2:
                            total += p["Price SR"]   
                            cart1 ={"Total Price":(f"\n=== {total} ===\n")}
                            cart2 = temp2.copy()
                            cart2.append(cart1)
                            
                    except KeyError:
                        pass
                        break  
                
                print(tabulate(temp2, headers="keys", tablefmt="mixed_outline"))
  
        elif A==2:
            remove_cart()
        elif A==3:
            display_cart()
            break
def remove_cart():
                        myjson = {}       
                        with open('cart.json','r') as f:
                            myjson =json.load(f)
                            k = int(input("Enter the Id: "))
                            for index, d in enumerate(myjson):
                                if d["Id"] == k:
                                    del myjson[index]
                        
                #f.seek(0)
                        with open('cart.json','w') as f:
                            json.dump(myjson,f,indent=4)
                        with open('cart.json','r') as f:
                            temp = json.load(f)
                        print(tabulate(temp, headers="keys", tablefmt="mixed_outline"))
def display_cart():
        with open('cart.json','r') as f:
            temp = json.load(f)
        total1=0
        for a in temp:
            total1 += a["Price SR"]   
            temp1 ={"Total Price":(f"\n=== {total1} ===\n")}
            cart2 = temp.copy()
            temp2 = temp.copy()
            temp2.append(temp1)
        print(tabulate(temp2, headers="keys", tablefmt="mixed_outline"))
        console.print("To check out press 1: ",style="bold underline red on white")
        q = int(input())
        if q == 1:
            
            tax = total1 * 0.15
            FinalPrice = tax + total1
            print("===================================Purchased successfully=============================")
            print(tabulate(temp2, headers="keys", tablefmt="grid"))
            panel = Panel(Text(f"Tax: {tax}", justify="center",style="#75B13E"))
            pane2 = Panel(Text(f"Total Pice include Tax {FinalPrice}", justify="center",style="#75B13E"))
            print(panel)
            print(pane2)
            now = datetime.now()
            panel1 = Panel(Text(f"Date: {now}", justify="center",style="#75B13E"))
            print(panel1)
            OurEbooks()
