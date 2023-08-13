import json
import os
from getpass import getpass
from colorama import Back , Style , Fore
class Course:
    def __init__(self):
        self.users = []
        self.load_users()
    
    def load_users(self):
        file_path = "registration.txt"
        if os.path.exists(file_path) and os.path.getsize(file_path) > 2:
            with open(file_path, "r", encoding="utf-8") as file:
                self.users = json.load(file)

    def save_users(self):
        with open("registration.txt", "w", encoding="utf-8") as file:
            json.dump(self.users, file)

class RegistrationCourse(Course):
    def __init__(self):
        super().__init__()

    def register(self):
        while True:
            user = input(Back.LIGHTBLACK_EX+"Enter your name: ")
            password = getpass(Back.LIGHTBLACK_EX+"Enter your password: ")
            print(Style.RESET_ALL)
            
            if 3 < len(user) < 15 and 3 < len(password) < 15:
                user_dict = {"user": user, "password": password}
                self.users.append(user_dict)
                self.save_users()
                print("You have been registered successfully.")
                break
            else:
                print(Fore.RED + "The username and password must be between 4 and 14 characters.")
                print(Style.RESET_ALL)

class LoginCourse(Course):
    def __init__(self):
        super().__init__()

    def login(self):
        while True:
            user_input = input(Back.LIGHTBLACK_EX+"Enter your name: ")
            password_input = getpass(Back.LIGHTBLACK_EX+"Enter your password: ")
            print(Style.RESET_ALL)
            
            for user in self.users:
                if user["user"] == user_input and user["password"] == password_input:
                    print(f"Hello {user['user']}, welcome to the Learn English program.")
                    os.system('clear')  
                    return
            print(Fore.RED+"Your username or password is incorrect. Please try again.")
            print(Style.RESET_ALL)

            
