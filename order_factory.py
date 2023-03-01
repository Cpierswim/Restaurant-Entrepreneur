from order import Order
from pasta import Pasta
from pizza import Pizza 
from salad import Salad
import constants
from helper import Helper

class OrderFactory:
    @staticmethod
    def create_order(type: str) -> Order:
        '''Returns a type of order matching the string provided
        
        type -- The type of order wanted

        Raises an exception if the type provided is not available
        '''
        type = type.lower()
        if type == Helper.OrderEnum.PIZZA.value:
            return Pizza(constants.PIZZA_NAME, constants.PIZZA_PRICE)
        elif type == Helper.OrderEnum.PASTA.value:
            return Pasta(constants.PASTA_NAME, constants.PASTA_PRICE)
        elif type == Helper.OrderEnum.SALAD.value:
            return Salad(constants.SALAD_NAME, constants.SALAD_PRICE)
        raise Exception("Order type not found")