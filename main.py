from Room import Room
import colorama
import names 

Roooom=[]        
x=None


def is_avaliable():
    if len(Roooom)==0:
        raise Exception("No rooms ".title())
def is_full(s):
    return s.get_len_student_in()==s.get_capacity()


while x!='exit':

    try: 
        print(colorama.Fore.BLUE ,'\nplease enter what you would like to do'.title())
        print(colorama.Fore.BLUE,'1-To make a room\n2-To add student to room\n3-to show student in one room\n4-to show all student in rooms\n5-To show rooms details\n6-To remove student from a room\n7-To search for a student\n8-To remove a room'.title())
        x=input(">>>")
        
        if x=='1':
            r=Room()
            is_there=False
            for i in Roooom:
                if r._room_id == i._room_id:
                    is_there=True
                    break
            
            if is_there:
                raise Exception("there is a Room with this ID")
                
            else:
                Roooom.append(r)
                print(colorama.Fore.GREEN,"Room created".title())


                
        elif x=='2':
            is_avaliable()
            try:
                step1_find_room=int(input("Enter Room ID you would like to add student to "))
            except:
                raise Exception("Wrong value ")
            is_there=False

            for i in Roooom:
                if step1_find_room == i._room_id:
                    if is_full(i):
                        raise Exception("Room is full")
                    try:
                        id=int(input("Enter student id to add to the room: ").title())
                    except:
                        raise Exception("Wrong value".title())
                    
                    for room in Roooom:
                        if id in room.get_student_ids():
                            raise Exception(f"Student with ID {id} is in room {room._room_id}")

                    i.add_student(id)
                    print(colorama.Fore.GREEN,"Student add".title())
                    is_there=True
            if not is_there:
                print(colorama.Fore.RED,"No Room with this ID ".title())

        elif x=='3':
            is_avaliable()
            try:
                step1_find_room=int(input("Enter Room ID you would like to see students in "))
                is_there=False
            except:
                raise Exception("Wrong Value ")
            for i in Roooom:
                if step1_find_room == i._room_id:
                    is_there=True  
                    if i.get_len_student_in() ==0:
                        print(colorama.Fore.MAGENTA ,"No Student in room ".title())
                    else:
                        i.display_student()
            if is_there==False:
                print(colorama.Fore.RED,'Room doesnt exit'.title())        
        elif x=='4':
            is_avaliable()

            for rooms in Roooom:
                if(rooms.get_len_student_in())==0:
                    print(colorama.Fore.LIGHTRED_EX,f"No student in room {rooms._room_id}\n")
                else:
                    print(colorama.Fore.MAGENTA,f'Students in room number {rooms._room_id}')
                    rooms.display_student()
        elif x=='5':
            is_avaliable()
            
            for i in Roooom:

                print(colorama.Fore.YELLOW,f"Room ID {i._room_id}, Room cpaacity {i.get_capacity()} number of student in room {i.get_len_student_in()}")

        elif x=='6':
                is_avaliable()
                try:
                    step1_find_room=int(input("Enter Room ID you would like to remove student from ".title()))
                    is_there=False
                except:
                    raise Exception("Wrong Value") 

                for i in Roooom:
                    if step1_find_room == i._room_id:
                        is_there=True
                        i.remove_student()
                        print(colorama.Fore.GREEN,"student removed ")
                        
                        
                if is_there==False:
                    print(colorama.Fore.RED,"Room doesnt exist")
        elif x=='7':
                is_avaliable()
                try:
                    id=int(input("Enter student id you want to search for : ").title())
                except:
                    raise Exception("Wrong value".title())
                founud=False
                for room in Roooom:
                    if id in room.get_student_ids():
                        print(colorama.Fore.MAGENTA,f"Studnet with ID {id} is in room {room._room_id}")
                        founud=True
                        break
                if founud==False:
                    raise Exception("Student doesnt exist")
        elif x=='8':
            is_avaliable()

            try:
                step1_find_room=int(input("Enter Room ID you would like to remove > ".title()))
                is_there=False
            except:
                raise Exception("Wrong Value")             
            
            for index , i in enumerate(Roooom):
                if step1_find_room ==i.get_room_id():
                    is_there=True
                    del Roooom[index]
            
            if is_there:
                print(colorama.Fore.GREEN,'Room removed ')
            else:
                raise Exception("Room Doesnt exist")
                

        elif x=='exit':
            print("Thank you and BEY  ! ")
            break
        else:
            raise Exception("INVLID INPUT")

         
                      
                        


    except Exception as e :
        print(colorama.Fore.RED,e)
