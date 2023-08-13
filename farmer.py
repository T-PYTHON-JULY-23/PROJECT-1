
import GreenLand

class farmer():
    availablty=True
    def __init__(self, name , id,location) -> None:
        self.name=name
        self.id=id
        self.location=location
        

    def request_farmer(self):
        user_location = input("Enter your location (north, waist, east, or south): ")
        
        found_farmer = None
        for farmer in farmerlist:
            if farmer.location == user_location and farmer.availablty:
                found_farmer = farmer
                break
        if found_farmer:
            print("Farmers are available at", user_location)
            #GreenLand.basket.append(found_farmer)
            found_farmer.availablty = False
            # checkout function here 
        else:
            user_input = input("Sorry, our farmers are busy for now. Continue without? (yes or no): ")
            if user_input.lower() == "yes":
                # checkout() 
                print("OK, go ahead and checkout.")
            else:
                print("Sorry for that. We hope to see you again.")  

    
farmerlist=[farmer("Mohammed",900345, "north"),
farmer("mohanad",900225, "waist"),
farmer("ahmed",900345,"waist") ]



farmer.request_farmer(farmerlist)

      
