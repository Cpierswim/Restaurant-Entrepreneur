from order import Order
from pasta import Pasta
from pizza import Pizza 
from salad import Salad

class OrderFactory:
    
    PIZZA_NAME = "Cheese Pizza"
    PIZZA_PRICE = 11.99

    PASTA_NAME = "Spagetti"
    PASTA_PRICE = 9.99

    SALAD_NAME = "Chef's Salad"
    SALAD_PRICE = 8.99
 
    @staticmethod
    def create_order(type: str) -> Order:
        '''Returns a type of order matching the string provided
        
        type -- The type of order wanted

        Raises an exception if the type provided is not available
        '''
        type = type.lower()
        if type == "pizza":
            return Pizza(OrderFactory.PIZZA_NAME, OrderFactory.PIZZA_PRICE)
        elif type == "pasta":
            return Pasta(OrderFactory.PASTA_NAME, OrderFactory.PASTA_PRICE)
        elif type == "salad":
            return Salad(OrderFactory.SALAD_NAME, OrderFactory.SALAD_PRICE)
        raise Exception("Order type not found")