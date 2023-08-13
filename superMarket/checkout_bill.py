from .product import Product
from art import tprint
import time 
import json
from tabulate import tabulate
import fileinput






def current_time():
    date_time=time.strftime("%Y-%m-%d %H:%M:%S")
    return date_time
  
                


# Total price of the products shopping cart
def total_of_price():
    with open("file_json.json","r")as file:
        data=json.load(file)
        total=0
        for index, d in enumerate(data["products"]):
            total+=d['total']
        return total
        
total:float=total_of_price()
tax = 0.15
tax:float = tax *total
total_tax = lambda x,y: x+y
result=total_tax(tax,total)


def checkout(user_fname,user_lname,phone,city,address):
    # to write product in json to the bill file 
    with open("bill.txt","w")as file:
        file.write(f"Date : {current_time()}")
        file.write(f"\n\nCustomer Name:{user_fname} {user_lname}\nCustomer Number:{phone}\nDelivery to: {city}-{address}\n\n")
        file.write(f"-PRODUCT-   -PRICE-     -QUANTITY-\n")
        file.close()
    with open("file_json.json","r")as file:
        data=json.load(file)
        for item in data["products"]:
            procudt_name=item['product_name']
            price=str(item['price'])
            quantity=str(item['quantity'])
            pl=(f"{procudt_name}          {price}            {quantity}\n")
            with open("bill.txt","a+") as f:
                f.write(pl)
        file.close()
    with open("bill.txt","a+")as file:
        file.write(f"\n\n\nThe Total of product: {total}\nDelivery price: {25}\nThe total: {total+25+10}\nThe total with tax : {(result+25+10)} \n\n State : pending")
        file.close()


def view_bill():
    with open("bill.txt", "r") as file:
        print(file.read())



