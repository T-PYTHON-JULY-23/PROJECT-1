import json
from tabulate import tabulate
from art import *
from Bookcaze import *
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import print
def admin():
                    console = Console()
                    choice1 = 0
                    while choice1 !=4:
                        pan1 = Panel(Text("*** eBooks Manager ***", justify="center",style="#af00ff"))
                        print(pan1)                
                        console.print("1) Add New Book",style="bold green")
                        console.print("2) search a book",style="bold green")
                        console.print("3) show requests",style="bold green")
                        console.print("4) Quit",style="bold red")
                        choice1 = int(input())
                        if choice1 == 1:
                            console.print("Enter id:",style="bold underline red on white")
                            new_id = int(input())
                            console.print("Enter Ganre:",style="bold underline red on white")
                            new_Ganre = input()
                            console.print("Enter Title:",style="bold underline red on white")
                            new_Title = (input())
                            console.print("Enter Price:",style="bold underline red on white")
                            new_Price = int(input())
                            Newdict = {"Id": new_id, "Ganre": new_Ganre, "Title": new_Title, "Price SR": new_Price}
                            bookcaze.append(Newdict)
                            with open('bz.json','a+') as f:
                                    json.dump(bookcaze, f,indent=4)
                            print(tabulate(bookcaze, headers="keys", tablefmt="mixed_outline"))  
                        elif choice1 == 2:
                            console.print("Looking up for a book...",style="bold underline white on green")

                            console.print("Enter Search Term: ",style="bold underline red on white")
                            k = input()
                            list_filtred = list(filter(lambda tag: tag['Title'] == k, bookcaze))
                            print(tabulate(list_filtred, headers="keys", tablefmt="mixed_outline"))
                        
                        elif choice1 == 3:
                            f = open('Requests.txt','r')
                            UserRequest = f.read()
                            print(UserRequest)