from user import *
from rich.console import Console
from plans import *
from art import *
from colorama import *
console = Console()
def account():
    check = True
    while check != False:
        from rich import print
        from rich.panel import Panel
        from rich.text import Text
        panel = Panel(Text("\nType L for Login, R to Register\n",justify="center",style="#75B13E"))
        print(panel)
        Login_Register = input()
        if Login_Register == "l" or Login_Register =="L":
            while check:
                with open('accountfile.txt', 'r') as f:
                    console.print("Enter your username: ",style="bold underline red on white")
                    username1 = input()
                    console.print("Enter your password: ",style="bold underline red on white")
                    password1 = input()
                    for line in f:
                        if("Username:"+username1+" Password:"+password1) == line.strip():
                            tprint("Welcome","block")
                            panel2 = Panel(Text("You want to subscribe or buy a book ? (Subscribe press '1' & Buy a book press '2')", justify="center",style="#75B13E"))
                            print(panel2)
                            ans = int(input())
                            if ans == 1:
                                Plans()

                            elif ans == 2:
                                ebooks()
                            check = False
                            break
                    else:
                        print("Username or password does not exist")
        else:
            Login_Register == "r" or Login_Register == "R"
            f = open("accountfile.txt","a+")
            username2 = input("~ Please enter your Username!\n")
            password2 = input("~ Please enter your password!\n")
            f.write(f"\nUsername:{username2} Password:{password2}\n")
            f.close()
            print("username and password has been made")
            panel2 = Panel(Text("You want to subscribe or buy a book ? (Subscribe press '1' & Buy a book press '2')", justify="center",style="#75B13E"))
            print(panel2)
            ans2 = int(input())
            if ans2 == 1:
                Plans()
            elif ans2 == 2:
                ebooks()
                            
            else:
                print("Wrong entry")
def Subsc():
    Subscribe = input("Welcome,\nType L for Login, R to Register\n")
    if Subscribe == "s" or Subscribe == "S":
        f = open("Subscribtion.txt","a+")
        username2 = input("~ Please enter your Username!\n")
        password2 = input("~ Please enter your password!\n")
        f.write(f"\nUsername:{username2} Password:{password2}\n")
        f.close()
        print("username and password has been made")
