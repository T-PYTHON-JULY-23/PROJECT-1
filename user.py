from tabulate import tabulate
from cart import *
import json
from Bookcaze import *
from cart import *
from Bookcaze import *
def ebooks():
    choice = 0
    while choice !=8:
        print('[1] for display books')
        print('[2] for buy a book')
        print('[3] search for a book')
        print('[4] request a book')
        choice = int(input())
        if choice == 1:
            print(tabulate(bookcaze, headers="keys", tablefmt="mixed_outline"))
        elif choice == 2:
            buyOrder()
        elif choice == 3:
            print("Looking up for a book...")
            K = input("Enter Search Term: ")
            list_filtred = list(filter(lambda tag: tag['Title'] == K, bookcaze))
            print(tabulate(list_filtred, headers="keys", tablefmt="mixed_outline"))
        elif choice == 4:            
            d=[]
            new_Ganre = input("Enter Ganre : ")
            new_Title = (input("Enter Title : "))
            d = [{"Ganre": new_Ganre, "Title": new_Title}]
            with open("Requests.txt", "a+") as fp:
                    json.dump(d, fp)
