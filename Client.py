
from AccountManagement import AccountManagement

def ClientInfo():

    clientlist=[]
    userAge = debit_time = 0 
    rent = salary = utility = funMoney = insurance = debit = debit_payed  =0.0
    inflation  = 0.005

    print('_'*30)
    print("\nPlease enter the following information:")
    print('_'*30)

    userAge = int(input("\nPlease enter your age: "))
    print('_'*10)
    rent = float(input("\nPlease enter the amout you pay for rent: "))
    print('_'*10)
    salary  = float(input("\nPlease enter your salary: "))
    print('_'*10)
    utility  = float(input("\nPlease enter the amout you pay for utility: "))
    print('_'*10)
    funMoney  = float(input("\nPlease enter the amout you set for fun: "))
    print('_'*10)
    insurance  = float(input("\nPlease enter the amout you pay for insurance: "))
    print('_'*10)
    debit  = float(input("\nPlease enter the total of your debit: "))
    print('_'*10)
    debit_time  = float(input("\nPlease enter the period you have to pay all your debit: "))
    print('_'*10)
    debit_payed  =float(input("\nPlease enter the amout you paid form the debit: "))

    clientlist = [userAge,rent,funMoney,utility,insurance,inflation,debit,debit_time,debit_payed,salary]

    return clientlist



def ClientInput():

    clientlist = ClientInfo()
    account = AccountManagement(clientlist[0],clientlist[1],clientlist[2],clientlist[3],clientlist[4],clientlist[5],clientlist[6],clientlist[7],clientlist[8],clientlist[9])
    try:  
        print('_'*30)
        UserChoese = input("\nPlease Choose from  number from the list below:\n1- To Calculat all Last Year Spending.\n2- To Estimate Next Year Spending.\n3- To Get Information On Your Debit.\n4- To Calculat How Many Years Left For Your Retirement.\n5- To Calculat The Needed Raise In Your Salary.\n6- To Exit The Programme.\n")
        if UserChoese == '1':
            print("All your last year spending: "+account.CalculatYearSpending()+"\n")
        elif UserChoese == '2':
            print("Estimate all of next year spending: "+account.EstimatingSpending()+"\n")
        elif UserChoese == '3':
            account.DebitInfo()
        elif UserChoese == '4':
            account.TimeLeftRetirement()
        elif UserChoese == '5':
            account.SalaryCal()
        elif UserChoese == '6':
            exit()    
    except Exception:
        print("Try Again!!\n")
        ClientInput()


    




ClientInput()