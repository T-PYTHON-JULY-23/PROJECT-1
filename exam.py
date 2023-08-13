from course import beginner_level,elementray_level,intermediate_level,advance_level
import os
from datetime import datetime, timedelta
from colorama import Back , Style , Fore

score = 0
level = ""
def placement_test ():
    global score
    global level
    print("you must take test to know level and continue .")
    print()
    ans = input(Back.LIGHTYELLOW_EX+"do you want to take the test ? ")
    print(Style.RESET_ALL)
    if ans.lower() == "yes" or ans.lower == "ok":
        os.system('clear')   
        print (Fore.LIGHTGREEN_EX+" This is test for determain your leve in english\n")
        print(Style.RESET_ALL)
        
        test=input("1- What’s .....  name?\n I\n you \n Your\n yours\n your answer is:")
        if test.lower() == "your":
            score+=1
        test=input("2- We’re Egyptions, We’re … Tanta\n for\n from \n to \n in\n your answer is: ")
        if test.lower() == "from":
            score+=1
        test=input("3- Jone’s …. nice and polite\n a\n from \n very\n an\n your answer is:")
        if test.lower() == "very":
            score+=1
        test=input("4- Mona ….. usually come by Taxi\n doesn’t\n isn’t \n don’t\n aren’t\n your answer is:")
        if test.lower() == "doesn’t":
            score+=1
        test=input("5- They ….. at club last night\n aren’t\n weren’t \n don’t\n didn’t\n your answer is:")
        if test.lower() == "weren’t":
            score+=1
        test=input("6- What …..you say?\n are\n have \n were\n did\n your answer is:")
        if test.lower() == "did":
            score+=1
        test=input("7- Where ….. to spend your holidays next summer?\n you are going\n are you going \n you will\n will you\n your answer is:")
        if test.lower() == "you are going":
            score+=1
        test=input("8- Seiko watches ….. in Japan\n are made\n made \n make\n are making\n your answer is:")
        if test.lower() == "make":
            score+=1
        test=input("9- If ….. I’ll tell him you called\n I’ll see him\n I see him \n I’d see him\n I saw him\n your answer is:")
        if test.lower() == "i see him":
            score+=1
        test=input("10- Why ….. crying?\n are you\n you are \n do you\n you do\n your answer is:")
        if test.lower() == "are you":
            score+=1
        if score >= 9 :
            level ="Advance"
            print(Fore.GREEN+f"your score is {score}\nyour level is {level}")
            print(Style.RESET_ALL)
        elif score >= 6:
            level ="Intermediate"
            print(Fore.GREEN+f"your score is {score}\nyour level is {level}")
            print(Style.RESET_ALL)
        elif score >= 3 :
            level="Elementray"
            print(Fore.GREEN+f"your score is {score}\nyour level is {level}")
            print(Style.RESET_ALL)
        else:
            level="Beginner"
            print(Fore.GREEN+f"your score is {score}\nyour level is {level}")
            print(Style.RESET_ALL)
        return True
    else:
        
        return False

def take_courses():
    global level
    user=input(Back.LIGHTYELLOW_EX+f"do you want to enroll in English course for {level} ?") 
    print(Style.RESET_ALL)
    os.system('clear')  
    if user.lower() == "yes" :  
        print("every level has 5 day's , please enter the number of day to show lesson of that day")
        print("1 ---> day 1")
        print("2 ---> day 2")
        print("3 ---> day 3")
        print("4 ---> day 4")
        print("5 ---> day 5")
        current_date = datetime.now()
        print(Fore.RED + "warning : the course is avilable for 5 days only !")
        print(Back.GREEN +"Current date:", current_date.strftime("%Y-%m-%d"))
        end_date = current_date + timedelta(days=5)
        print(f"End day : {end_date.strftime('%Y-%m-%d')}")
        print(Style.RESET_ALL)
        
        while True:
            day = int(input(Fore.LIGHTMAGENTA_EX+"enter the number of day : "))
            print(Style.RESET_ALL)
            if level == "Beginner":
                beginner_level(day)
            elif level == "Elementray":
                elementray_level(day)
            elif level == "Intermediate":
                intermediate_level(day)
            elif level == "Advance":
                advance_level(day)
            
            if day == 5:
                print(Back.LIGHTRED_EX+"\t\tThank you for complete the course")
                break
            elif day>5:
                os.system("clear")
                day = int(input(Fore.RED +"you entred wrong day!\nenter the number(1-5) of day : "))
                print(Style.RESET_ALL)
                
                
    elif user.lower() == "no":
       print(Fore.CYAN+"\t \t \t Thanks , I hope you have a great day ")
       print(Style.RESET_ALL)