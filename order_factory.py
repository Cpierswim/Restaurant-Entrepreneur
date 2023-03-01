from order import Order
from pasta import Pasta
from pizza import Pizza 
from salad import Salad
import constants

class OrderFactory:
    @staticmethod
    def create_order(type: str) -> Order:
        '''Returns a type of order matching the string provided
        
        type -- The type of order wanted

        Raises an exception if the type provided is not available
        '''
        type = type.lower()
        if type == "pizza":
            return Pizza(constants.PIZZA_NAME, constants.PIZZA_PRICE)
        elif type == "pasta":
            return Pasta(constants.PASTA_NAME, constants.PASTA_PRICE)
        elif type == "salad":
            return Salad(constants.SALAD_NAME, constants.SALAD_PRICE)
        raise Exception("Order type not found")