from superMarket.product import Product
from superMarket.display_search_product import *
from art import tprint



password ="1122"
name="naif"
def manger():
    ask_manegar=input("Are you manager ? press 'y' for yes and press 'n' for no : ")
    if ask_manegar=="y":
        manager_name=input("name: ")
        manager_password=input("password: ")
        if manager_name==name and manager_password==password:
            tprint("Welcome   Manager","chunky")
            
            def more_delete():
                ask_manegar_to_add_or_delete=input("Do want to delete item from supermaret app? y/n :")
                if ask_manegar_to_add_or_delete=="y":
                    manager_delete_product=input("Enter the prodcut name do want to delete to supermarket app: ")
                    del_product(inventory,manager_delete_product)
                    more_delete()
            more_delete()
                
        else:
            print("Manager Name and Password is incorrect.")