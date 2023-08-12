import Expenses_Tracker
from datetime import datetime
from colorama import Fore, Back, Style
today=datetime.now()
tracker= Expenses_Tracker.ExpensesTracker() # creat object from ExpensesTracker class
print("\n")
welcome_txt="💵 Welcome to the Expenses Tracker!💵\n"
print(Fore.LIGHTCYAN_EX+welcome_txt.center(120))
second_message="This program helps you manage your expenses and gain insights into your spending habits..🫰\n"
print(second_message.center(120))
while True :
    third_message="💰~~~~~ Expense Tracker ~~~~~💰\n"
    print(Style.RESET_ALL+Fore.LIGHTCYAN_EX+third_message.center(120))
    print(Style.RESET_ALL+"1. ➕ Add Expense \n2. 📑 View Expenses \n3. ✨ Expense Statistics \n4. 📈 Graphical Chart for Expenses \n5. 🚫 Exit \n")
    
    choice = input("Enter your choice : (1-5)")
    if choice == '1' : # if the user inter number #1 
        try: # I use try..exception because if the user inter invalid input for amount 
            catagory = input ("Enter the expense category:")
            amount = float(input("Enter the expense amount: "))
            tracker.add_expenses(catagory,amount,today)
        except ValueError:
            print(Fore.LIGHTCYAN_EX+"❌ Invalid input. Amount should be a numeric value. ❌")
        
    elif choice == '2' : # if the user inter number #2
        print("~~~~~ Expenses ~~~~~")
        tracker.print_category_and_amount_from_json() # it will print all saved expenses with date and time 

    elif choice == '3':  # if the user inter number #3
        print("~~~~~ Expenses ~~~~~")
        total_expenses = tracker.total_expenses()
        avrage_expenses =  tracker.avrage_expenses()
        highest_expenses =  tracker.highest_expenses()
        lowest_expenses = tracker.lowest_expenses()
        # this block will print the all saved expenses in detailed 
        print(Fore.LIGHTCYAN_EX+f"the average expenses : $ {avrage_expenses}")
        print(f"the total expenses : ${total_expenses}")
        print(f"Highest Expense: {highest_expenses['Catagory']} - ${highest_expenses['Amount']}")
        print(f"Lowest Expense: {lowest_expenses['Catagory']} - ${lowest_expenses['Amount']}")
           


    elif choice == '4':  # if the user inter number #4
            print("~~~~~ Expenses ~~~~~")
            tracker.plot_expense_trends('data.json') # it will print a visualize of the expenses using interactive charts.

    elif choice =='5':  # if the user inter number #5
        forth_message="Thank you for using 'Expenses Tracker ' ...❤️   "
        fifth_message="Existing ..."
        print(Fore.LIGHTCYAN_EX+forth_message.center(120))
        print(Fore.LIGHTCYAN_EX+fifth_message.center(120))
        break

    else :
        print(Fore.LIGHTCYAN_EX+"❌ Invalid choice. Try again. ❌") # This message will appear if the user entered the wrong number(not between 1-5)
 