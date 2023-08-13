###file contains classes and functions###


#list to save pets information
pets = []
#calss pet that has pet_name,gender_pet, phone_number,city,gender,age as atributes
class Pet:
    def __init__(self,pet_name:str,phone_number_owner:int,city:str,gender:str,age:int,pet_category:str) -> None:
        self.pet_name = pet_name
        self.pet_category = pet_category
        self.phone_number_owner = phone_number_owner
        self.city = city
        self.gender = gender
        self.age = age
        self.is_adopted = False
        pass





#function that add pet and save the pet to list      
def add_pet(pet:Pet):
    pets.append(pet)



#function that display pet for the user 
def disply_pets(pet:Pet):
    for index, p in enumerate(pets): #'p' short cut from 'pet' word
        print(f"{index} - [the name of pet is:{p.pet_name} -category is:{p.pet_category} -the phon number of owner is: {p.phone_number_owner} -city: {p.city} -gender of pet: {p.gender} -age of pet: {p.age}]-{'Not available to choose' if p.is_adopted else 'Available to choose'}]")



#function to adopt a pet by index and show if it chosen or not 
def adopt_pet(index):
    if 0 <= index < len(pets):
        if not pets[index].is_adopted:
            pets[index].is_adopted = True
            return True  # chosen successful
        else:
            print("This pet is already was chosen. Please choose another pet.")
    else:
        print("Invalid index.")
    return False  # chosen failed





#list for save the adoptioner information
adoptioner_inf = []


#class Adoptioner that has name_adoptione , phone_number_adoptioner, user_adopt as atributes
class Adoptioner:
    def __init__(self,name_adoptioner:str,phone_number_adoptioner:int,user_adopt:int) -> None:
        self.name_adoptioners = name_adoptioner
        self.phone_number_adoptioner = phone_number_adoptioner
        self.user_adopt = user_adopt

        pass




#function to add adoptioner information to list
def add_adoptioner(ado:Adoptioner): #'ado' short cut from 'adoptioner' word
    adoptioner_inf.append(ado)




#function to display adoptioner informatiom to the user
def display_adoptioner_information(ado):
    for index , adop in enumerate(adoptioner_inf):
        print(f"{index} - [the name is: {adop.name_adoptioners} -the phone number is: {adop.phone_number_adoptioner} -the choisen pet is: {adoptioner_inf[index].user_adopt}]")



# Function to delete a pet by index
def delete_pet(index):
    if 0 <= index < len(pets):
        deleted_pet = pets.pop(index)
        print(f"Pet '{deleted_pet.pet_name}' has been deleted successfully.")

        # Check if the pet was adopted and remove the adoptioner
        for adoptioner in adoptioner_inf:
            if adoptioner.user_adopt == index:
                adoptioner_inf.remove(adoptioner)
                print(f"Adoptioner '{adoptioner.name_adoptioners}' has been removed as the pet was adopted.")
                break  # Break after removing the first matching adoptioner
    else:
        print("Invalid index.")









    

    




    

    








        












'''
try:
if self.phone_numbr>10:
print("thr number must 10 intigers")
except:
Print(valueeroor)

'''