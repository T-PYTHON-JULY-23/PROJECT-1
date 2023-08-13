from superMarket.checkout_bill import *
from superMarket.product import Product
from superMarket.display_search_product import *
from superMarket.shopping_cart import *
from superMarket.Design_CLI import style
from superMarket.state import update_state
from superMarket.manager import *



#Products
water = Product("water",1,"-Brand: Berain  ")
pepsi = Product("pepsi",2,"-Brand: MenaBev ")
kitkat = Product("kitkat",4,"-Brand:Nestale")
tea = Product("tea",10,"-Brand: Rabea      ")
rice=Product("rice",20,"-Brand: AlWalimah  ")
chips=Product("chips",2,"-Brand: Raja      ")
sauce=Product("sauce",4,"-Brand: Crystal   ")
sugar=Product("sugar",4,"-Brand: AlFares   ")










#Add Products
add_product(inventory,water)
add_product(inventory,kitkat)
add_product(inventory,pepsi)
add_product(inventory,tea)
add_product(inventory,sugar)
add_product(inventory,sauce)
add_product(inventory,chips)
add_product(inventory,rice)




manger()




tprint("Welcome   to   Supermarket\n","big")
while True:
    style()
    user_input=input("Enter the number option : ")
    if user_input == "1":
        print()
        display_inventory(inventory)

    elif user_input=="2":
        search_for_product=input("Enter the name of product do you want to see it : ")
        search_product(inventory,search_for_product) 

    elif user_input=="3":
        try:
            product1:str=input("Enter the name of the product do you want to add to Shopping cart : ").lower()
            quantity1=int(input("Enter the quantity : "))
            add_many_product_to_shopping_cart(inventory,product1,quantity1)
        except ValueError:
            print("Please write only the number in qunatity")

    elif user_input=="4":
        delete_product_from_Shopping_Cart()
    elif user_input=="5":
        tprint("Shopping Cart\n","chunky")
        Display_Shopping_Cart()

    elif user_input == "6":
        try:
            user_fname=input("first name : ")
            user_lname=input("last name : ")
            city=input("City : ")
            address=input("Address : ")
            phone=int(input("Phone number : "))
            ask_to_buy=input("Do you want to buy ! y/n")
            if ask_to_buy.lower()=="y":
                checkout(user_fname,user_lname,phone,city,address)
            else:
                break
            
        except ValueError:
            print("Please write only the number")

            
    elif user_input == "7":
        print()
        view_bill()
        print("\n\n")

    elif user_input=="8":
        update_state()
    elif user_input=="9":
        break
    
    else:
        print("You did't select a number, Please write the correct number.")
