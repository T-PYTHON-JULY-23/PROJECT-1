from users.usersClasses import *
class AirlineSystem:
    def __init__(self):
        self.flights = []   # List to store flights
        self.employees = [] # List to store employees
        self.passengers=[]   # List to store passengers

    def add_flight(self, flight):
        self.flights.append(flight)

    def add_employee(self, employee):
        self.employees.append(employee)
        
    def add_passenger(self,passenger):
        self.passengers.append(passenger)

    def search_flights(self, source, destination):# Search for available flights based on source and destination.
        available_flights = []
        for flight in self.flights:
            if (flight.source).lower()== source.lower() and (flight.destination).lower() == destination.lower():
                available_flights.append(flight)  
        return available_flights # Returns a list of available flights.
    
    def reserve_seat(self, flight_number, seat_number,passenger):# Reserve a seat on a specific flight for a passenger.
        for flight in self.flights:
            if flight.flight_number == flight_number:
                return flight.reserve_seatt( seat_number,passenger) #Returns True if the seat is successfully reserved, False otherwise.
        return False

    def print_seat_status(self, flight_number):#Print the seat status for a specific flight.
        for flight in self.flights:
            if flight.flight_number == flight_number:
                flight.print_seat_status()
                return

    def search_employee(self,employee_id):# Search for an employee by their ID
       for employee in self.employees:
          if employee.employee_id == employee_id:
             found=True
             break
          else:
             found=False
       return found # Returns True if the employee is found, False otherwise.
    def search_employee_on_flight(self,employee_id):# Search for the flight of an employee based on their ID.
       for employee in self.employees:
          if employee.employee_id == employee_id:
             return employee.flight # Returns the flight object if found, None otherwise
           