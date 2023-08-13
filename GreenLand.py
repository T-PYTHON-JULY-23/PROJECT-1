from farmer import request_farmer
indoor_plant= {
    "Rubber trees":{ 
    "price": 55,
    "quntity":10 },

"Spider Plant":{
    "price":34,
    "quntity":10},

"Peace Lily":{
    "price":34,
    "quntity":10},

"English Ivy":{
    "price":44,
    "quntity":10},

"Elephant Ear":{
    "price":77,
    "quntity":10}}

outdoor_plant= {
    "Hosta":{ 
    "price":57 ,
    "quntity":10},

"Hydrangea":{
    "price":70,
    "quntity":10},

"Lavender":{
    "price":44,
    "quntity":10},

"Stonecrop":{
    "price":50,
    "quntity":10}}


def display_plants():
    
        git_outdoor_plant= lambda x: print(f"Outdoor plant in our Green Land: {outdoor_plant.keys()}")
        git_outdoor_plant(outdoor_plant)
        git_indoor_plant= lambda x: print(f"Indoor plant in our Green Land is:{indoor_plant.keys()}")
        git_indoor_plant(indoor_plant)
   

display_plants()

basket = []
def git_plant():
    print("Welcome to Green Land")

    while True:
        
        user_choice = input("Which plant do you want? Indoor, outdoor, or exit: ") 
        if user_choice.isdigit():
             raise Exception("No numbers only string")
                  
        if user_choice == "exit":
            break
        elif user_choice.lower() == "indoor":
            for key, value in indoor_plant.items():
                print(key, value)

            plant_name = input("Enter the name of the indoor plant or type 'outdoor' to switch: ")
            if plant_name in indoor_plant:
                basket.append(plant_name)
                basket.append(indoor_plant[plant_name]['price'])
                indoor_plant[plant_name]['quntity']-=1

            else:
                print("Invalid plant name. Please try again.")
        elif user_choice.lower() == "outdoor":  # هنا ماكان فيه قوسين بعد lower
            for key, value in outdoor_plant.items():
                print(f"{key}. {value}")

            plant_name = input("Enter the number of the outdoor plant or type 'indoor' to switch: ")
            if plant_name in outdoor_plant:
                basket.append(outdoor_plant[plant_name]['price'])
                basket.append(plant_name)
                outdoor_plant[plant_name]['quntity'] -= 1 
            else:
                print("Invalid plant number. Please try again.")
        else:
            print("Invalid choice. Please select 'indoor', 'outdoor', or 'exit'.")
    if user_choice=="exit" and len(basket)!=0:
                user_choice=input("Do you want farmer? y or n ")
                if user_choice=="y":
                    request_farmer()
                else:
                    print("Thank you for visiting Green Land. Have a great day!")

        
    print("Thank you for visiting Green Land. Have a great day!")

    return basket


print(git_plant())