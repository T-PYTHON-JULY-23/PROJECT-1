from training_course import TrainingCours as TC
from training_course import Training
import training_course


cours_python = TC("Building Websites Using Python" , "the basics of the Python language\n and the basics of building websites using one of the most popular frameworks that help build integrated web pages ","23-09-2023" , "10:00AM-3:00PM" , 'Riyadh')
cours_java = TC("\nBuilding Websites Using Java" , "aims to develop and build web applications using the Spring boot framework.\n Where you can start your educational journey by learning the basics of the Java language","23-08-2023" , "10:00AM-3:00PM" , 'Riyadh')
cours_security = TC("\nInformation Security Program","aims to introduce basic units related to information security,\n familiarity with cyber challenges and threats, and advanced methods for protecting information privacy.","20-08-2023", "6:00PM-9:00PM","Riyadh")
cours_microsoft_power = TC("\nMicrosoft Power Platform Basics","A specialized training program for those wishing to obtain an accredited \nMicrosoft certificate in the field of Power Platform Fundamentals (PL-900).", "13-08-2023", "6:00PM-9:00PM", "Riyadh")
l= cours_python.name_course , cours_java.name_course ,cours_security.name_course ,cours_microsoft_power.name_course
cours_list=[cours_python, cours_java,cours_security, cours_microsoft_power]
list_user=[]
infromation_list=[]
 

def display_to_user():
    #This function shows the user the courses
    display = input("Do you want to view courses? answer: yes or no\n")
    if display == 'yes':
           for c in cours_list:
            print(c.courses())
            print('*'*15)

        

def user_add_course():
    #This function allows the user to register in courses: 
    while True:
        user_registration = input("Do you want to register in courses? answer: yes or no\n")
        if user_registration == 'yes':
            chooes_user_cours = input("Choose the course you want:\n")
            for course in cours_list:
                    if chooes_user_cours==course.name_course:
                        if chooes_user_cours in list_user:
                            print("You are already registered")
                            continue
                    
                        elif infromation_list == []:
                                    name = input("Enter yuor name:\n")
                                    email =input("Enter your email:\n")
                                    infromation_list.append(name)
                                    infromation_list.append(email)

                                    phone_number =input("Enter phone number:")
                                    while len(phone_number) > 10  or  len(phone_number) < 10 :
                                        phone_number =input("Please enter your phone number again:")
                                    infromation_list.append(phone_number)

                        else:
                            print(infromation_list)
                            name=infromation_list[0]
                            email=infromation_list[1]
                            phone_number=infromation_list[2]
                        t1= Training(name , int(phone_number), email)
                        training_course.add(t1)
                        print(f"yuor name is: {t1.name} your email is: {t1.email} your number phone: {t1.phone_number}" )
                        list_user.append(chooes_user_cours)
                        print("You have been registered successfully")

                    


        elif user_registration == 'no':
                ask_user= input("do you want to list your courses items? answer: yes or no\n")
                if ask_user == 'yes':
                        print(list_user[:])

                #to exit the program
                exit1 = input("Do you want exit program: answer:yes or no\n")
                if exit1== 'yes':
                    print("\nthank you for using the  program, come back again soon")
