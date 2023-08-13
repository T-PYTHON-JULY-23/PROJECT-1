from main import welcome,display_courses
from course import *
from users import *
from exam import placement_test,take_courses




try:
    if welcome():
        display_courses()
        if placement_test():
            take_courses()
        else:
            print(Fore.LIGHTCYAN_EX+"See you next time!")
            print(Style.RESET_ALL)
except Exception as e:
    print("An error occurred:", e)
