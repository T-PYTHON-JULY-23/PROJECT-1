from art import *
from colorama import Fore, Back, Style, init
import json
from Pet.lostPet import *
from Pet.foundPet import *

lost_list = []
found_list = []
users = []
init(autoreset=True)
print(Fore.BLUE+text2art("Pet House"))


def login_(user: str, password: str):

    file = open("users.txt", "r", encoding="utf-8")
    for line in file.readlines():
        if line.find(user) != -1:
            print(Fore.GREEN+"Login successful!")
            return True

    else:
        print(Fore.RED+"Wrong username/password")
        return False


def sign_in(user_sign: str, password_sign: str):

    f = open("users.txt", "r", encoding="utf-8")
    for line in f.readlines():
        if line.find(user_sign) != -1:
            print("You already have an account")
            f.close()
            return False

        else:
            w_file = open("users.txt", "+a", encoding="utf-8")
            new_user = {"username": user_sign, "password": password_sign}
            users.append(new_user)
            contact = json.dumps(users)
            w_file.writelines(contact)
            w_file.close()
            print(Fore.GREEN+"Account created successfuly!")
            return True


def menu():

    while True:
        print("-"*10)
        print("   MENU")
        print("-"*10)
        print("View our services 'services'")
        print("Know more about us 'about'")
        print("Contact us 'contact' ")
        print("Logging out 'logout'\n ")

        menu_input = input("Enter your choice:")
        if menu_input == "services":
            services()
        elif menu_input == "about":
            print("We help pets that are used to living indoors with their owners get back home.\n"
                  "We enable people who lost their pets to publish a post about the lost pet containing all necessary\n"
                  "information so other people can help find it. Also, people who have found a pet wandering the streets\n"
                  "with no contact information on its collar can publish a post about the found pet so it can reach the owner.\n")

        elif menu_input == "contact":
            contact_us()
        elif menu_input == "logout":
            print(Fore.GREEN+"log out successful!\n")
            break
        else:
            print(Fore.RED, "Please select from the menu")


def contact_us():
    print("Please fill in the form and we will get back to you very soon!")
    while True:
        name = input("Name:")
        email = input("email:")
        message = input("Message:")
        if name.isalpha():
            if email.endswith("@gmail.com"):
                user_contact = {"email": email,
                                "name": name, "message": message}
                contact = json.dumps(user_contact)
                file = open("conact.txt", "a+", encoding="utf-8")
                file.write(contact+'\n')
                file.close()
                print(Fore.BLUE+"Thank You!\n")
                break
            else:
                print("Please provide a valid email!")

        else:
            print("Please provide a valid name! It must be all charecters.")


def services():
    print("-"*10)
    print(" Services")
    print("-"*10)
    print("Lost Pet 'L'")
    print("Found lost pet 'F'")
    services_input = input("Enter your choice:")

    if services_input.lower() == 'l':

        print("View lost pets 'v'")
        print("Start a new lost pet report 's'")
        lost_pet = input("Enter your choice:")

        if lost_pet == 's':
            print("--START REPORT--")
            name = input("Pet name:")
            color = input("Color:")
            type = input("Type:")
            gender = input("Gender:")
            bread = input("Bread:")
            contact_info = input("Contact info:")
            place_lost = input("Place lost:")

            lostpet = LostPet(color, bread, type, gender,
                              contact_info, place_lost, name)

            print(lostpet.lost_pets_list())
            lost_list.append(lostpet)

        elif lost_pet == 'v':
            tprint("Lost pets list")
            for pet in lost_list:
                pet.view()
        else:
            print("please enter your choice correctly!")

    elif services_input.lower() == 'f':

        print("View found pets 'v'")
        print("Start a found pet report 's'")
        found_pet = input("Enter your choice:")

        if found_pet == 's':
            print("--START REPORT--")
            color = input("Color:")
            type = input("Type:")
            gender = input("Gender:")
            bread = input("Bread:")
            contact_info = input("Contact info:")
            place_found = input("Place found:")

            foundpet = FoundPet(color, bread, type, gender,
                                contact_info, place_found)

            print(foundpet.found_pets_list())
            found_list.append(foundpet)

        elif found_pet == 'v':
            tprint("found pets list")
            for pet in found_list:
                pet.view()
        else:
            print("please enter your choice correctly!")

    else:
        print(Fore.RED, "Please select from the list")


while True:
    access = input("For login 'L' For Sign Up 'S':")
    try:
        if access == "exit":
            print("See You Later")
            break  

        elif access.upper() == 'L':
            user: str = input("Username:")
            password: str = input("Password:")
            if login_(user, password) == True:
                menu()
        elif access.upper() == 'S':
            user_sign: str = input("Enter a new username:")
            password_sign: str = input("Enter a new password:")
            if sign_in(user_sign, password_sign) == True:
                menu()

        else:
            raise TypeError(
                "Invalid. Please use 'L' for logging or 'S' for Signing up.")

    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
