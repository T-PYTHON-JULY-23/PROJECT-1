from training_course import TrainingCours as TC
from colorama import Fore, Back, Style

def admin_operations(course_list:list,):
    information_admin = ("admin" , "2023")
    check_admin= input("\nEnter user name: ")
    check_admin_password=input("Enter password: ")

   
    if check_admin == information_admin[0] and check_admin_password == information_admin[1]:
        while True:
            new_cours=input(Fore.WHITE+"\nChoose 1 for add , 2 for delete , 3 To view courses press , 4 for exit: ")
            if new_cours == '1':
                name_course=input("\nEnter name course:")
                about = input("Enter about course:")
                date = input("Enter date cours:")
                time = input("Enter time course:")
                location=input("Enter location course:")
                new_course = TC(name_course, about, date,time,location)
                course_list.append(new_course)
                print(Fore.MAGENTA+"\nAdded successfully\n")

            elif new_cours == '2':
                try:
                    name_course=int(input("\nChoose the course index you want to delete: "))
                    del course_list[name_course]
                except ValueError :
                    print(Fore.RED+"\nHe entered the index with a number, not letters, try agin\n")
                except Exception as e:
                    print(e)
                else:
                    print(Fore.MAGENTA+"Deleted successfully\n")

            elif new_cours == '3':
                for c in course_list:
                    print(c.courses())
                    print('*'*15)

            elif new_cours == '4':
                print(Fore.LIGHTGREEN_EX+"\nthank you for using the  program, come back again soon\n")
                break


    else:
        print("The username or password is incorrect")
