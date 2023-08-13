from course import *
from datetime import date 
from users import *
import os
from colorama import Back , Style , Fore
from art import *

  
        

def display_courses ():
    list_courses=["Beginner","Elementray","Intermediate","Advance"] 
    print(Fore.LIGHTGREEN_EX+f"In this program there are 4 levels  {list_courses}") 
    print(Style.RESET_ALL)
    

def welcome():
    registration_course = RegistrationCourse()
    login_course = LoginCourse()

    print(text2art("Welcome",font="block"))
    user=input(Back.LIGHTYELLOW_EX+"\t\tDo you want to login ?")
    print(Style.RESET_ALL)
    if user.lower()=="yes":
        login_course.login() 
        return True
    
    elif user.lower()=="no":
      print("\nThis program has many lessons to develop your English!")
      user=input(Back.LIGHTYELLOW_EX+"\t\nDo you want to registration ?") 
      print(Style.RESET_ALL)
      if user.lower()=="yes":
              os.system('clear')   
              registration_course.register()
              return True
      else :
          return False
              