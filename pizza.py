from order import Order

class Pizza(Order):
    def __init__(self, dish_name: str, price: int) -> None:
        '''Instantiates a Pizza object'''
        super().__init__(dish_name, price)