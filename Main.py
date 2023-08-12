import PetsHome.pet as PH
from colorama import Fore, Back, Style
from termcolor import colored
import json




while True:
    text1 = colored('Welcome to Pets Home choose what wolud like to do: ', "light_grey", attrs=["reverse", "bold"])
    print(text1)
    text2 = colored("1-Add Pet to adoption \n2-Display Pet for Adoption\n3-Tips about Adoption\n4-Admin\n5-Exit from Pets Home","light_magenta", attrs=["blink"])
    print(text2)

    
    while True:
        try:
            user_choice = int(input("Your choice: "))

            if 1 <= user_choice <= 5: #user choose from 1 t0 5 or except message will show
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")



    if user_choice == 1:
        name_pet=input('Enter name of the pet : ')
        phone_number_owner =input('Enter the phone number of the owner : ')
        while  len(phone_number_owner)< 10 or len(phone_number_owner)>10 or not phone_number_owner.isdigit():
            print("the phone number must be 10 intigirs or valid number")
            phone_number_owner =input('Enter the phone number of the owner : ')

        city__owner = input('Enter the city : ')

        while True:
            try:
                gender_pet = int(input('1- Female\n2- Male\nChoose the gender of the pet: '))

                if gender_pet == 1:
                    gender_pet = "Female"
                    break
                elif gender_pet == 2:
                    gender_pet = "Male"
                    break
                else:
                    print("Please choose a valid number (1 or 2).")
            except ValueError:
                print("Please enter a numeric value.")


        age_pet = input('Enter the age of the pet: ')



        try:
            pet1= PH.Pet(name_pet,int(phone_number_owner),city__owner,gender_pet, age_pet) #create object from class Pet
            PH.add_pet(pet1)
        except Exception as e:
            print("Some thing is wrong try agin", e)
        else:
            print("the pet is added successfully!")
            print("\n")



    if user_choice == 2:

        if not PH.pets:  # Check if the pets list is empty
            print("There are no pets available for adoption.")
            print("/n")

        else:
            print("Do you want to adopt a pet? Enter 'yes' to adopt or 'no' to display the pet only.")
            while True:
                user_choice2 = input("Your answer: ")

                if user_choice2.lower() == "yes":

                    while True:
                        PH.disply_pets(None)
                        user_input3 = int(input("Please choose a number from the list: "))
                        if 0 <= user_input3 < len(PH.pets):
                            if not PH.pets[user_input3].is_adopted:
                                name_adoptioner = input("Please enter your name: ")
                                phone_number_adoptioner =input('Enter the phone number of the owner : ')
                                while  len(phone_number_adoptioner)< 10 or len(phone_number_adoptioner)>10 or not phone_number_adoptioner.isdigit():
                                    print("the phone number must be 10 intigirs or valid number")
                                    phone_number_adoptioner =input('Enter the phone number of the owner : ')

                                adptionerifo = PH.Adoptioner(name_adoptioner,int(phone_number_adoptioner), user_input3) #create object from class Adoptioner
                                PH.add_adoptioner(adptionerifo)
                                PH.adopt_pet(user_input3)

                                print("The pet is booked for you, you will receive a message contains information about pet!")
                                print("\n")
                                
                                break
                            else:
                                print("This pet is already was chosen. Please choose another pet.")
                                print("\n")
                        else:
                            print("Invalid selection. Please choose a valid number.")
                            print("\n")
                    break


                elif user_choice2.lower() == "no":
                    try:
                        PH.disply_pets(None)
                    except:
                        print("There are no pets to adopt.")
                        print("\n")
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    print("\n")




    tips = []
    with open("Adoption_Information.txt", "r") as file:
        tips = json.loads(file.read())
     
            
    if user_choice == 3:
        print("tips about adoption: ")
        for tip in tips:
            print(tip)



            
    if user_choice == 4:
        user_name = input('Please enter your username: ')
        password = input("Please enter your password: ")

        if user_name == 'Lenah123' and password == '12345@':
            text3 = colored("Welcome Admin!","light_grey",attrs=["reverse", "bold"])
            print(text3)
            text4 = colored("1- Display pit and adoptioner information\n2- Delete pet information\n3- Add tips about pet adoption\n4- Exit from admin account","light_red", attrs=["blink"])
            print(text4)
            while True:
                try:
                    admin_choice4 = int(input("Your choice: "))
                    if admin_choice4 == 1:
                        print("Pet avalible in programe:")
                        PH.disply_pets(None)
                        print("\n")
                        print("information of adoptioner:")
                        PH.display_adoptioner_information(adptionerifo)



                    elif admin_choice4 == 2:
                        try:
                            print("adoptioner information:")
                            PH.display_adoptioner_information(adptionerifo)
                            index_to_delete = int(input("Enter the index of the pet to delete: "))
                            PH.delete_pet(index_to_delete)

                        except Exception as e:
                            print("Something went wrong while deleting the pet:", e)


                    elif admin_choice4 == 3:
                        admin_input = input("Please provide the information you want to add: ")
                        tips.append(admin_input)
                        with open("Adoption_Information.txt", "w") as file:
                            file.write(json.dumps(tips))
                            print("The information is added successfully!")
                            print("\n")


                    elif admin_choice4== 4:
                        print("Thank you , see you agin 'admin'")
                        print("\n")
                        break

                    else:
                        print("Invalid choice. Please choose 1 or 2 or 3 or 4.")
                    
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
                
        else:
            print("The username or password is incorrect. Please try again!")
            print("\n")
            

             

    if user_choice == 5:
        print("Thank you for using the Pets Home!")
        break






            








        





