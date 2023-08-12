from training_course import TrainingCours as TC
import training_course
import user
from art import *
from admin import admin_operations
from colorama import Fore, Back, Style


wlcome=text2art("\n--------------Welcome to Tuwaiq Academy---------------\n", font="fancy65")
print (wlcome)

cours_python = TC("Building Websites Using Python" , "the basics of the Python language\n and the basics of building websites using one of the most popular frameworks that help build integrated web pages ","23-09-2023" , "10:00AM-3:00PM" , 'Riyadh')
cours_java = TC("Building Websites Using Java" , "aims to develop and build web applications using the Spring boot framework.\n Where you can start your educational journey by learning the basics of the Java language","23-08-2023" , "10:00AM-3:00PM" , 'Riyadh')
cours_security = TC("Information Security Program","aims to introduce basic units related to information security,\n familiarity with cyber challenges and threats, and advanced methods for protecting information privacy.","20-08-2023", "6:00PM-9:00PM","Riyadh")
cours_microsoft_power = TC("Microsoft Power Platform Basics","A specialized training program for those wishing to obtain an accredited \n Microsoft certificate in the field of Power Platform Fundamentals (PL-900).", "13-08-2023", "6:00PM-9:00PM", "Riyadh")
cours_list=[cours_python, cours_java,cours_security, cours_microsoft_power]
list_user=[]
infromation_list=[]

while True:
    print(Fore.WHITE+"Are you student , or admin: ")
    user_input = input(Fore.WHITE+"choose 1 for studen , 2 for admin , 3 for exit: ")
    if user_input == "1":
        user.student_registration_course(cours_list, list_user, infromation_list, training_course)
    elif user_input == "2":
        admin_operations(cours_list)
    elif user_input == "3":
        print(Fore.LIGHTGREEN_EX+"\nthank you for using the  program, come back again soon\n")
        break
    else:
        print(Fore.RED+"\nPlease choose 1, 2 or 3\n")

