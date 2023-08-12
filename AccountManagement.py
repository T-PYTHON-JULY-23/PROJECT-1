
class AccountManagement:

    def __init__(self, age:int, rent_money:float, fun_money:float, utility_money:float, insurance_money:float,
                  inflation:float ,debit:float ,debit_time:float, debit_payed:float, salary:float ):
       
    
        self.age = age

        self.rent_money = rent_money
        self.fun_money = fun_money
        self.utility_money = utility_money
        self.insurance_money = insurance_money
        self.debit = debit

        self.salary= salary
        self.inflation = inflation
        self.debit_time =debit_time
        self.debit_payed = debit_payed

    

    def CalculatYearSpending(self):
       Spending=  self.rent_money + self.fun_money + self.utility_money + self.insurance_money + self.debit_payed 

       return round(Spending,2)
       

    def EstimatingSpending(self):
         previous_year_spending = self.CalculatYearSpending()
         additional_sales =  previous_year_spending * self.inflation
         forecasted_nextyear = additional_sales + previous_year_spending

         return round(forecasted_nextyear,2)

    def DebitInfo(self):

        debit_monthly = self.debit/(self.debit_time*12) 

        debit_left= self.debit - self.debit_payed 
        
        debit_time_leftMonth= debit_left/debit_monthly

        debit_time_leftyear = debit_time_leftMonth/12

        print("Information on your Debit:\n ")
        print(f"The amount you will pay monthly: {round(debit_monthly,2)}\n")
        print(f"The amount left to pay: {round(debit_left,2)}\n")
        print(f"The time left to pay all your Debit: {round(debit_time_leftyear,1)}\n")



    def  TimeLeftRetirement(self):
       
       Retirementage = 60 - self.age
       
       print("Retirment averge age is 60 years.\n")
       print(f"You have {Retirementage}years left until Retirment\n")


    def SalaryCal(self):

        if round(raise_in_salaryPre,2)<1:
            print("You don't need a raise")
        else:
            print(f"You need {round(raise_in_salaryPre,2)}% raise in your salary to be able to afford your spending last year\n")


