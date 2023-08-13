from projec1 import *

def main():
    while True:
        print("Welcome to the rental store!")
        print("Please choose an option:")
        print("1. Display available vehicles")
        print("2. Rent a vehicle")
        print("3. Search for a vehicle")
        print("4. Request a specific color")
        print("5. Request a vehicle")
        
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_available_vehicles()
        elif choice == '2':
            rent_vehicle()
        elif choice == '3':
            search_vehicle()
        elif choice == '4':
            search_color()
        elif choice == '5':
            request_vehicle()    
        elif choice == '6':
           
            print("Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")
        print()
 
if __name__ == '__main__':
    main()
        

