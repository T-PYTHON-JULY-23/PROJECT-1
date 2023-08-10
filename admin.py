from training_course import TrainingCours as TC


information_admin = ("admain" , "2023")

print("are you admin")
check_admin= input("enter user name: ")
check_admin_password=input("enter password: ")


if check_admin == information_admin[0] and check_admin_password == information_admin[1]:
    print("Hello")
    new_cours=input("Do you want to add a new course?")
    if new_cours == 'yes':
    name1=input(" enter name course:")
    about2 = input("Enter about course:")
    date3 = input("enter date cours:")
    time4 = input("enter time course:")
    location5=input("enter location course:")
    

else:
    print("The username or password is incorrect")
