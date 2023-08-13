class Product():
    def __init__(self,product_name,price:int,description:str,quantity:int=1) -> None:
        self.product_name = product_name
        self.quantity =quantity
        self.price = price
        self.description=description