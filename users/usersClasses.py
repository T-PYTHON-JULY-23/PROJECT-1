
class Employee:
    def __init__(self, employee_id, name,flight):
        self.employee_id = employee_id
        self.name = name
        self.flight=flight
        
       
class Traveler:
    def __init__(self, name,seat_number):
        self.name = name
        self.seat_number=seat_number