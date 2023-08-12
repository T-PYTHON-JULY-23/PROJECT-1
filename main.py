from art import *
from colorama import*
#from passenger.passengerClass import Passengr
from flight import *
from airlineSystem import *
from users.usersClasses import *

print(Fore.LIGHTBLACK_EX +(text2art("     WELCOME",font='varsity')))
print(Fore.CYAN+(text2art("Tuwaiq Airlines",font='slant')))
print(Style.RESET_ALL)
#
system = AirlineSystem()

#Create Flight objects 
flight1 = Flight("F001", "New York", "London", "2023-08-10 08:00", "2023-08-10 14:00")
flight2 = Flight("F002", "London", "Paris", "2023-08-11 10:00", "2023-08-11 12:00")
flight3 = Flight("F003", "Jeddah", "Istanbul", "2023-08-15 01:00", "2023-08-16 06:00")
flight4 = Flight("F004", "Riyadh", "Seoul", "2023-09-11 07:00", "2023-09-12 16:00")
flight5 = Flight("F005", "Jeddah", "Geneva", "2023-11-5 05:00", "2023-11-6 03:00")
flight6 = Flight("F006", "London", "Paris", "2023-09-15 01:00", "2023-09-16 06:00")

# Add flights to the system
system.add_flight(flight1)
system.add_flight(flight2)
system.add_flight(flight3)
system.add_flight(flight4)
system.add_flight(flight5)
system.add_flight(flight6)

# Create Employee objects
employee1 = Employee("E001", "Ahmed Abdullah","F001")
employee2 = Employee("E002", "Ibrahim Mashaal","F004")
employee3 = Employee("E003", "Mohammed Hussein","F002")
employee4 = Employee("E004", "Sultan Saad","F006")

# Add employees to the system
system.add_employee(employee1)
system.add_employee(employee2)
system.add_employee(employee3)
system.add_employee(employee4)








while True:
 try: 
  users=input("For passenger services enter 'p', for employee services enter 'e',for save liste enter 's' for exit, enter 'x': ")
  if users.lower() !='p' and users.lower() != 'e' and users.lower() !='x'  and users.lower() !='s':
     raise ValueError("Error: the input should be a 'p' or 'e' or 'x'.") 
 except ValueError as error:
     print(error)
 if users.lower()=="p":
    # Passenger Services  
   while True:
    print("-"*20) 
    print("Choose from the list")
    print("1.search for a specific flight")
    print("2.view all flights")
    print("3.Ticket booking")
    print("4.Exit")
    Choose=input(" ")
    print("-"*20)
    if Choose =='1':
        try:
         departure_station = input("Please enter the departure station: ")
         destination = input("Please enter the destination: ")
         if departure_station.isdigit() or destination.isdigit(): #Check if either the departure station or destination contains digits
           raise ValueError("Error: Departure station and Destination should be a string.") ## Raise a ValueError if either value contains digits
        except ValueError as error:# Catch the ValueError and print the error message
             print(error)
        Specific_flight = system.search_flights(departure_station, destination)
        for flight in Specific_flight:
           print(f"Flight: ({flight.flight_number}), Departure station:{flight.source} , destination: {flight.destination} , Departure time: {flight.departure_time} , Arrival Time: {flight.arrival_time}") 
        if Specific_flight==[]:
            print("The flight does not exist ")
    elif Choose =='2':
       for flight in system.flights:
           print(f"Flight: ({flight.flight_number}), Departure station:{flight.source} , destination: {flight.destination} , Departure time: {flight.departure_time} , Arrival Time: {flight.arrival_time}") 
    
    elif Choose=="3":
        flight_number =input("Enter flight number:  ")
        for f in system.flights:# chea
                if f.flight_number == flight_number:
               
                 # Print all seat statuses
                 print(f"Seat status for flight {flight_number}:")
                 print("-"*20)
                 system.print_seat_status(flight_number)
                 print("-"*20)
                 # Reserve a seat on a flight
                 passenger = input("enter passenger name: ")
                 seat_number = input("enter seat number: ")
                 while True:
                  if system.reserve_seat(flight_number, seat_number,passenger):
                      print(f"Seat {seat_number} reserved successfully for {passenger} on flight {flight_number}!")
                      new_passenger=Traveler(passenger,seat_number)
                      system.add_passenger(new_passenger)# add to list 
                      # Print ticket for the reservedseat
                      choose=input(f" Display {passenger} ticket enter 'y' or enter 'no': ")
                      if choose=='y':
                        flight = None
                        for f in system.flights: #Bring the flight information 
                         if f.flight_number == flight_number:
                           flight = f
                           break

                        if flight is not None:
                         print("-"*20)
                         travelar = passenger
                         flight.print_ticket(passenger, seat_number)
                         print("-"*20)
                        break
                      elif choose=='n':
                          break
                           
                     
                  else:
                   print(f"Failed to reserve seat {seat_number} for {passenger} on flight {flight_number}.")
                   break
                 break           
        else:
          print("the flight not found ")
                    
      
   
    elif Choose=="4":
      break
 elif users.lower()=="e":
   employee_id=input("plesae enter id number: ")
   if system.search_employee(employee_id):# Check if the employee ID exists in the system
    print("-"*20) 
    print("welcom in Tuwaiq Airlines  ")
   
    while True:
     print("-"*20) 
     print("Choose from the list")
     print(f"1.View the registered flight number to the employee ({employee_id})")
     print(f"2.View recorded flight information for the employee ({employee_id})")
     print("3.View all seats and the names of their passengers")
     print("4.Exit")
     Choose=input()
     print("-"*20) 
     if Choose =='1':# Retrieve the flight number for the employee
        print(f"Employee {employee_id} is on flight {system.search_employee_on_flight(employee_id)}.")
     elif Choose=="2": # Retrieve flight information for the employee
         for flight in system.flights:
           if system.search_employee_on_flight(employee_id)==flight.flight_number:
            print(f"Flight -{flight.flight_number}- Departure station: {flight.source} , destination: {flight.destination} , Departure: {flight.departure_time} , Arrival: {flight.arrival_time}") 
     elif Choose=="3":# View all seats and the names of their passengers for a specific flight
        flight_number =input("enter flight number you want:  ")
        for f in system.flights:
                if f.flight_number == flight_number: 
                    f.print_seats_passenger()
                    break
        else:
                  print("the flight not found ")  
        
     elif Choose=="4":
       break
   else:
    print("sorry You are not registered as an employee of Tuwaiq Airlines")
 elif users.lower()=="s":
     # Open a file in write mode
    with open("users/employee.txt", "w") as file:
    # Write each element of the list to the file
     for employee in system.employees:
        file.write(f"Employee name: {employee.name},ID: {employee.employee_id},On flight: {employee.flight}\n")
     # Open a file in write mode
    with open("users/passenger.txt", "w") as file:
    # Write each element of the list to the file
     for passenger in system.passengers:
        file.write(f" Passenger name: {passenger.name}, seat: {passenger.seat_number}\n")
 elif users.lower()=='x':
     break 

