class Order:
    def __init__(self, dish_name: str, price: int) -> None:
        '''Instantiates an Order object'''
        self.dish_name = dish_name
        self.price = price