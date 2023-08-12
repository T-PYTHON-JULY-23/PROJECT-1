from training_course import Training 
import training_course as TC
from art import *
from colorama import Fore, Back, Style

def student_registration_course(cours_list, list_user, infromation_list, training_course):
    #This function allows the user to register in courses: 
    infromation_list=[]
    list_user=[]
    while True:
        user_registration= input(Fore.WHITE+"\nTo view courses press 1, to register press 2, to view your recordings press 3, to exit the program press 4: ")
        if user_registration.strip() == '1':
             for c in cours_list:
                print(Fore.BLUE+"\n",c.courses())
                print('*'*15)

        elif user_registration.strip() == '2':
            chooes_user_cours = input(Fore.WHITE+"\nChoose the course you want: ")
            #Checks the course entered by the user if it exists or not
            if chooes_user_cours.strip().title() in cours_list:
                #Checks if it has been previously registered or not
                if chooes_user_cours.strip().title() in list_user:
                    name=infromation_list[0]
                    email=infromation_list[1]
                    phone_number=infromation_list[2]
                    print(Fore.RED+"You are registered")
                else:
                  #User information
                    if infromation_list == []:
                        name = input("\nEnter yuor name: ")
                        infromation_list.append(name)
            
                        email =input("Enter your email: ")
                        try:
                            if email.index("@gmail"):
                                infromation_list.append(email)
                        except:
                            email=input("Enter your email again with @: ")
                            infromation_list.append(email)
                        

                        phone_number =input("Enter phone number: ")
                        while len(phone_number) > 10  or  len(phone_number) < 10 :
                            phone_number =input("\nPlease enter your phone number again:")
                        infromation_list.append(phone_number)

                    else:
                        name=infromation_list[0]
                        email=infromation_list[1]
                        phone_number=infromation_list[2]
                    t1= Training(name , int(phone_number), email)
                    training_course.add(t1)
                    print(f"yuor name is: {t1.name} your email is: {t1.email} your number phone: {t1.phone_number}\n" )
                    list_user.append(chooes_user_cours)
                    print(Fore.MAGENTA+"You have been registered successfully")  
            else: 
                print(Fore.RED+"The course not found!!")



        elif user_registration == '3':
                for i in list_user[:]:
                    print(Fore.YELLOW+'\n',i)
                

            #to exit the program
           
        elif user_registration == '4':
                print(Fore.LIGHTGREEN_EX+"\nthank you for using the  program, come back again soon\n")
                break
        else:
             print(Fore.RED+"Please choose from 1-4")
