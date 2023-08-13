class Vehicle:
    def __init__(self, name, model_year, color):
        self.name = name
        self.model_year = model_year
        self.color = color

    def display_info(self):
        print("Vehicle Name: {} \nModel Year: {} \nColor: {}".format(
            self.name, self.model_year, self.color))


class Car(Vehicle):
    def __init__(self, name, model_year, color, daily_rent_price, monthly_rent_price):
        super().__init__(name, model_year, color)
        self.daily_rent_price = daily_rent_price
        self.monthly_rent_price = monthly_rent_price

    def display_info(self):
        super().display_info()
        print("Daily Rent Price: {} \nMonthly Rent Price: {}".format(
            self.daily_rent_price, self.monthly_rent_price))


class Motorcycle(Vehicle):
    def __init__(self, name, model_year, color, daily_rent_price):
        super().__init__(name, model_year, color)
        self.daily_rent_price = daily_rent_price
        

    def display_info(self):
        super().display_info()
        print("Daily Rent Price: {}".format(
            self.daily_rent_price))
    #_________________________________________________
        
# create sample data
car1 = Car("Toyota Camry", 2019, "Silver", 150, 1000)
car2 = Car("Honda Civic", 2020, "White", 100, 1200)
car3 = Car("Ford Mustang", 2021, "Red", 130, 1500)
motorcycle1 = Motorcycle("Suzuki Hayabusa", 2020, "Black", 130)
motorcycle2 = Motorcycle("Kawasaki Ninja", 2021, "Green", 135)
motorcycle3 = Motorcycle("Ford F-150", 2018, "Blue", 100 )

vehicles = [car1, car2, car3, motorcycle1, motorcycle2, motorcycle3]



#___________________________________________________________

def display_available_vehicles():
    """Displays the available vehicles along with their information."""
    print("Available Vehicles:")
    for i, vehicle in enumerate(vehicles):
        print(f"{i+1}. {vehicle.name} ({vehicle.model_year}) - {vehicle.color}")
        if isinstance(vehicle, Car):
            print(f"    Daily Rent Price: {vehicle.daily_rent_price}$ - Monthly Rent Price: {vehicle.monthly_rent_price}$")
        elif isinstance(vehicle, Motorcycle):
            print(f"    Daily Rent Price: {vehicle.daily_rent_price}$")

#________________________________________________________________________________ 



def rent_vehicle():
    #Allows the user to rent a vehicle.
    while True:
        vehicle_num = input("Enter the number of the vehicle you want to rent (or 'q' to quit): ")
        if vehicle_num.lower() == 'q':
           return
        else:
            break
    while True:
        rental_period = input("Enter the rental period (daily/monthly): ")
        if rental_period.lower() not in ["daily", "monthly"]:
            print("Invalid rental period. Please try again.")
        else:
            break
    while True:
        payment_method = input("Enter the payment method (credit card/cash): ")
        if payment_method.lower() not in ["credit card", "cash"]:
            print("Invalid payment method. Please try again.")
        else:
            break

    print(f"Payment method: {payment_method}")
    print(f"Rental period: {rental_period}")

#___________________________________________________________________ 

def search_vehicle():
    """Allows the user to search for a vehicle."""
    search_name = input("Enter the name of the vehicle you are looking for: ")
    found_vehicles = []
    for vehicle in vehicles:
        if search_name.lower() in vehicle.name.lower():
            found_vehicles.append(vehicle)
            
    if not found_vehicles:
        print("Sorry, no vehicles were found with the given name.")
        return
    print(f"Found {len(found_vehicles)} vehicles:")
    for i, vehicle in enumerate(found_vehicles):
        print(f"{i+1}. {vehicle.name} ({vehicle.model_year}) - {vehicle.color}")
    print()
    #_____________________________________________________

def request_vehicle():
    """Allows the user to request a vehicle if it is not available."""
    vehicle_name = input("Enter the name of the vehicle you want to request: ")
    vehicle_model_year = input("Enter the model year of the vehicle you want to request: ")
    vehicle_color = input("Enter the color of the vehicle you want to request: ")
    vehicle_type = input("Enter the type of the vehicle you want to request (car/motorcycle): ")
    while True:
        daily_rent_price = input("Enter the daily rent price ,Determine the expected rental price: ")
        try:
            daily_rent_price = int(daily_rent_price)
            break
        except ValueError:
            print("Invalid rent price. Please try again.")
    if vehicle_type.lower() == 'car':
        while True:
            monthly_rent_price = input("Enter the monthly rent price ,Determine the expected rental price: ")
            try:
                monthly_rent_price = int(monthly_rent_price)
                break
            except ValueError:
                print("Invalid rent price. Please try again.")
        vehicle = Car(vehicle_name, vehicle_model_year, vehicle_color, monthly_rent_price)
    elif vehicle_type.lower() == 'motorcycle':
        vehicle = Motorcycle(vehicle_name, vehicle_model_year, vehicle_color, daily_rent_price)
     
    else:
        print("Invalid vehicle type. Request failed.")
        return
    vehicles.append(vehicle)
    print("Request submitted successfully.")    
#___________________________________________________________________---


def search_color():
    
    color = input("Enter the color of the vehicle you want to request: ")
    vehicle_type = input("Enter the type of the vehicle you want to request (car/motorcycle): ")
    found_vehicle = None
    for vehicle in vehicles:
        if isinstance(vehicle, Car) and vehicle.color.lower() == color.lower() and vehicle_type.lower() == 'car':
            found_vehicle = vehicle
            break
        elif isinstance(vehicle, Motorcycle) and vehicle.color.lower() == color.lower() and vehicle_type.lower() == 'motorcycle':
            found_vehicle = vehicle
            break
        
    if found_vehicle:
        print(f"{found_vehicle.name} ({found_vehicle.model_year}) is available in {color} color.")
    else:
        print(f"Sorry, no {vehicle_type}s were found with the given color.")

   #_____________________________________________________________________________


















