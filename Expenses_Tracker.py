import json
import matplotlib.pyplot as plt
from colorama import Fore, Back, Style

class ExpensesTracker :
    def __init__(self) -> None:
        self.load_expense_data() 

        
    #1 This function will add and save catagory and amount to json file
    def add_expenses (self , catagory , amount , today): 
        self.expenses.append({'Catagory': catagory , 'Amount':amount , 'date':today}) # store dictionary inside list
        with open("data.json", 'w') as file:
            json.dump(self.expenses, file, indent=4, default=str)
            file.close()
        print(Fore.LIGHTCYAN_EX+"Expense added successfully!")


    #2 This function will return the maximum amount value entered 
    def highest_expenses(self):
        with open("data.json", 'r') as json_file:
         expenses_data = json.load(json_file)
        return max(expenses_data, key=lambda expense: expense['Amount'])


    #3 This function will return the minimum amount value entered
    def lowest_expenses (self):
        with open("data.json", 'r') as json_file:
         expenses_data = json.load(json_file)
        return min(expenses_data, key=lambda expense: expense['Amount'])  


    #4 This function will return the total of amount value
    def total_expenses(self):
        with open ("data.json","r")as json_file:
         expenses_data = json.load(json_file)
        return sum(expense['Amount'] for expense in expenses_data )    
    

    #5 This function will return the avrage of amount value
    def avrage_expenses(self):
        total_Expenses = self.total_expenses()
        return total_Expenses / 2
    
    #6 This function will read data from "data.json" file 
    def load_expense_data(self):
        with open("data.json", 'r') as file:
         self.expenses = json.load(file )


    #7 This function will print a chart depending on the amount and date
    def plot_expense_trends(self,filename):
            with open(filename, 'r') as file:
                expense_data = json.load(file)
            dates = [expense['date'] for expense in expense_data]
            amounts = [expense['Amount'] for expense in expense_data]

            plt.figure(figsize=(10, 6))
            plt.plot(dates, amounts, marker='o')
            plt.xlabel('date')
            plt.ylabel('Expense Amount')
            plt.title('Expense Trends Over Time')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
               

    #8 This function will print 'Catagory' and 'Amount'
    def print_category_and_amount_from_json(self):
        with open("data.json", 'r') as json_file:
                expenses_data = json.load(json_file)
                for expense in expenses_data:
                    category = expense.get('Category')
                    amount = expense.get('Amount')
                    date= expense.get('date')
                    print(Fore.LIGHTCYAN_EX+f"{expense['Catagory']} : $ {expense['Amount']} {expense['date']}")
    

             

