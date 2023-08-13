import json
from tabulate import tabulate
from .product import Product


# To add new product to json file
def add_json(new_data,filename='file_json.json'):
    with open(filename, "r+") as file:
        data = json.load(file)
        data["products"].append(new_data)
        file.seek(0)
        json.dump(data,file, indent= 4)


#-------To add products to shopping cart------
def add_many_product_to_shopping_cart(inventory,name:str,quantity:int=0):
    with open("file_json.json","r+") as file:
        data=json.load(file)
        for index, d in enumerate(data["products"]):
            if name == d["product_name"]:                    
                print("You have the item")
                break
        else:
            for product_name, product in inventory.items():
                if name == product.product_name:
                    y={
                    "product_name":product.product_name,
                    "price":product.price,
                    "quantity":quantity,
                    "description":product.description,
                    "total": product.price*quantity                 
                    }
                    add_json(y)


# Delete products from the Shopping cart
def delete_product_from_Shopping_Cart():
    my_json={}
    with open("file_json.json","r")as file:
        my_json=json.load(file)
        k=input("Enter the name do want delete from shopping cart : ").lower()
        for index, d in enumerate(my_json["products"]):
            if d["product_name"] == k:
              del my_json["products"][index]
    with open("file_json.json",'w') as f:
        json.dump(my_json,f,indent=4)

def Display_Shopping_Cart():
    with open("file_json.json","r")as file:
        data=json.load(file)
        print()
        info=data["products"]
        print(tabulate(info, headers='keys', tablefmt='rounded_outline'))