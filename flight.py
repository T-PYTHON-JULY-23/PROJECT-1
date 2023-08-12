
      
     

class Flight:
    def __init__(self, flight_number, source, destination, departure_time, arrival_time):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.seat_map = {
                     "A1":"","A2":"",#business clas
                     "A3":"","A4":"",
                     "B1":"","B2":"",#first class
                     "B3":"","B4":"",
                     "B5":"","B6":"",
                     "C1":"","C2":"",#Economy class
                     "C3":"","C4":"",
                     "C5":"","C6":"",
                     "C7":"","C8":""}
        self.reserved_seats = set()
  
    
    def reserve_seatt(self, seat_number,name):# Reserve a specific seat for a passenger.
        if seat_number in self.seat_map:#Check if the seat number exists .
            if seat_number in self.reserved_seats:#Check if the seat number is reserved .
                return False
            
            self.reserved_seats.add(seat_number)
            self.seat_map[seat_number]=name
            return True # Returns True if the seat is successfully reserved, False otherwise.

        return False

    def print_seat_status(self): # Print the status of each seat in the flight (reserved or unreserved).
        
        for seat_number in self.seat_map:
            if seat_number in self.reserved_seats:
                print(f"Seat {seat_number}: Reserved")
            else:
                print(f"Seat {seat_number}: Unreserved")

    def print_ticket(self, passenger, seat_number):# Print the ticket details for a passenger and their assigned seat.
        print("Ticket Details:")
        print(f"Flight Number: {self.flight_number}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Departure Time: {self.departure_time}")
        print(f"Arrival Time: {self.arrival_time}")
        print(f"Passenger: {passenger}")
        print(f"Seat Number: {seat_number}")
       
    def print_seats_passenger(self):# Print the list of seats and the corresponding passenger name (if reserved) for the flight.
         for seat_number in self.seat_map:
            if seat_number in self.reserved_seats:
                print (f"seat {seat_number} Reseved for {self.seat_map.get(seat_number)}")
            else:
                print(f"Seat {seat_number}  Unreserved")
            
        
         