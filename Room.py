import colorama 
class Room:
    def __init__(self,) -> None:
        try:
            room_id=int(input("Enter Room id you would like to create: ".title()))
            room_capacity=int(input("Enter Room capacity: ".title()))
            
               
        except :

            raise Exception("Wrong value")
        if room_capacity <=0 :
            raise Exception("Room capacity must be more than 0 ")        
        self.set_room_id(room_id)

        self._room_capacity=room_capacity
        self.__student_in={}
        print(f"Room number {self._room_id} with capacity of {self._room_capacity} has been created\n")
        

    def set_room_id(self,id:int):
        if isinstance(id,int):
             self._room_id=id
        else:
            raise ValueError('INVALID INPUT')
    
    def add_student(self,id):
        x=False
        try :
            
            name=input('Enter Student name to add to the room : '.title())
            age=int(input('Enter Student age to add to the room: '.title()))
            if age <18 or age>50:
                x=True
                raise Exception('')
        except :
            if x:
                raise Exception("Age must be between 18 and 50")
            else:
                raise Exception("INVALID INPUT")
            

        if id in self.__student_in.keys():
            raise Exception("Student already in the Room".title())
        elif self._room_capacity == len(self.__student_in):
            raise Exception("Room is full".title())
        self.__student_in[id]={
            'name':name,
            'age':age
        }

    def get_room_id(self):
        return self._room_id
    
    def remove_student(self):
        try:
            id=int(input("Enter student id to remove : ").title())
        except :
            raise Exception("INVALID INPUT\n")
        if id in self.__student_in.keys():
            del self.__student_in[id]
        else:
            raise Exception("Stundet is not in the room ".title())

    def display_student(self):
        for key,value in self.__student_in.items():
            print(colorama.Fore.YELLOW,f"Student name ({value['name']}) ,id({key}) , age ({value['age']})")

    
    def get_len_student_in(self):
        return len(self.__student_in)

    def get_capacity(self):
        return self._room_capacity

    def get_student_ids(self):
        return self.__student_in.keys()
    

    

        

        
