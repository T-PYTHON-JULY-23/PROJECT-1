import GreenLand


class Farmer:
    id = 0
    name = None
    location = None
    available = True

    def __init__(self, name, id, location) -> None:
        self.name = name
        self.id = id
        self.location = location


farmerlist = [Farmer("Mohammed", 900345, "north"),
              Farmer("mohanad", 900225, "west"),
              Farmer("ahmed", 900345, "west")]


def request_farmer():
    user_location = input("Enter your location (north, west, east, or south): ")

    found_farmer = None
    for farmer in farmerlist:
        if farmer.location == user_location and farmer.available:
            found_farmer = farmer
            break
    if found_farmer:
        print("Farmers are available at", user_location)
        print("Farmer name and id: {}[{}]".format(farmer.name, farmer.id))
        GreenLand.basket.append(f"*a farmer service with {farmer.name} ")
        found_farmer.available = False
        # checkout function here
    else:
        user_input = input("Sorry, our farmers are busy for now. Continue without? (yes or no): ")
        if user_input.lower() == "yes":
            # checkout()
            print("OK, go ahead and checkout.")
        else:
            print("Sorry for that. We hope to see you again.")

