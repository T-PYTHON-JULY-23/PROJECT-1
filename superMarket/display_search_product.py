from tabulate import tabulate
from .product import Product
from art import tprint








inventory = {}


#------to add product to the inventory------
def add_product(inventory:dict,product:Product):
    if product.product_name == inventory:
        print("You have a product")
    else:
        inventory[product.product_name] = product 

def del_product(library:dict, product:Product):
    if product in library:
        del library[product] 



# to display all product in the inventory
def display_inventory(inventory):
    count=1
    tprint("Menu","chunky")
    for product_name, product in inventory.items():
        table=[[count,product.product_name,product.price,product.description]]
        count+=1
        headers=[" ","Product","Price","description"]
        tab=tabulate(table,headers,tablefmt="rounded_outline")
        print(tab)







# Search for the product
def search_product(inventory,name:str):
    for product_name, product in inventory.items():
        if name == product.product_name:
            table=[[product.product_name,product.price,product.description]]
            headers=["Product","Price","description"]
            tab=tabulate(table,headers,tablefmt="rounded_outline")
            print(tab)