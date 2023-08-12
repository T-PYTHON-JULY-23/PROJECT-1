class CreditCard:
    def __init__(self,cardHolder:str,balance:float,cardNumber:int,expireDate:str,cvv:int) -> None:
        self.__cardHolder = cardHolder
        self.__balance = balance
        self.__cardNumber=cardNumber
        self.__expireDate=expireDate
        self.__cvv=cvv
    def get_cardHolder(self):
        return self.__cardHolder
    def get_balance(self):
        return self.__balance
    def get_cardNumber(self):
        return self.__cardNumber
    def get_expireDate(self):
        return self.__expireDate
    def get_cvv(self):
        return self.__cvv
    # def set_account_holder(self, account_holder:str):
    #     if isinstance(account_holder, str):
    #         self.__account_holder = account_holder
    #     else:
    #         raise ValueError("please input valid name")
    # def set_initial_balance(self, initial_balance:float):
    #     if isinstance(initial_balance, float):
    #         self.__initial_balance = initial_balance
    #     else:
    #         raise ValueError("please input valid balance")
    # def deposit(self,amount):
    #     newBlance = amount + self.__initial_balance
    #     self.__initial_balance = newBlance
    #     return f'updated balance: {self.__initial_balance}'
    def withdraw(self):
        newBlance = self.__balance - 8
        if newBlance >= 0:
            self.__balance = newBlance
            return 'Payment successful'
        else:
            return 'not enough balance'


# account1 = creditCard('Renad',5000,'','ll','kkk')
# print(account1.__dict__)
# print(account1.withdraw())
# print(account1.__dict__)
# print(account1.withdraw(5000.1))