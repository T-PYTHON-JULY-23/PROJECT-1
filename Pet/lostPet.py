from colorama import Fore, Back, Style,init
from Pet.pet import *
init(autoreset=True)
lost=[]

class LostPet(Pet):
     def __init__(self,color:str , bread:str, type:str, gender:str, contact_info:str,place_lost:str,name:str)->None:
       super().__init__(color,bread,type,gender,contact_info)
       self.place_lost = place_lost
       self.name = name

    
     def lost_pets_list(self):
       
       lost_dict={"name":self.name,"color": self.color,"bread":self.bread,"type":self.type,"gender":self.gender,"contact_info":self.contact_info,"place_lost":self.place_lost}
       lost.append(lost_dict)
       return ("Lost pet report added! we hope you find your pet soon.")

     def view(self):
      lost_dict={"name":self.name,"color": self.color,"bread":self.bread,"type":self.type,"gender":self.gender,"contact_info":self.contact_info,"place_lost":self.place_lost}
      print("Name: {} Color: {} Bread: {} Type: {} Gender: {} Contact info: {} Place lost: {}".format( lost_dict["name"],lost_dict["color"], lost_dict["bread"],lost_dict["type"], lost_dict["gender"],lost_dict["contact_info"],lost_dict["place_lost"]))




         