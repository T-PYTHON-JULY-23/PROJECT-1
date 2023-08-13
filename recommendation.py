class about:
    def __init__ (self, name:str , rate:float ,range_ : int, best_selling:str , contact:int, location) -> None:
        self.name = name
        self.rate = rate
        self.range_ = range_
        self.best_selling = best_selling
        self.contact = contact
        self.location = location
    def details(self):
        return f"The Name of the Restaurant:  {self .name} and The rateing of the restaurant is:  {self.rate} the prices range from:   {self.range_}and the Best Selling is:  {self.best_selling}here is to contact with them!For more Datails:  {self.contact} here is the location:  {self.location}"
class entertaiment:
    def __init__(self, name:str , rate: float , contacct:int) -> None:
        self.name = name
        self.rate = rate
        self.contacct = contacct
    def details_2 (self):
        return f"The name of this wonderful entertainment place is:  {self.name} and the rateing of this wonderful place is:  {self.rate} to more Datails about this place contact with them!:  {self.contacct}"