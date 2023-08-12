
from Pet.pet import *

found = []
adopt =[]

class FoundPet(Pet):
    def __init__(self, color: str, bread: str, type: str, gender: str, contact_info: str, place_found: str) -> None:
        super().__init__(color, bread, type, gender, contact_info)
        self.place_found = place_found

    def found_pets_list(self):
        found_dict = {"color": self.color, "bread": self.bread, "type": self.type,
                      "gender": self.gender, "contact_info": self.contact_info, "place_found": self.place_found}
        found.append(found_dict)
        return ("Found pet report added!")

    def view(self):
        found_dict = {"color": self.color, "bread": self.bread, "type": self.type,
                      "gender": self.gender, "contact_info": self.contact_info, "place_found": self.place_found}
        print("Color: {} Bread: {} Type: {} Gender: {} Contact info: {} Place lost: {}".format(
            found_dict["color"], found_dict["bread"], found_dict["type"], found_dict["gender"], found_dict["contact_info"], found_dict["place_found"]))





