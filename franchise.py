from logger import logger
from enum import Enum
from order_factory import OrderFactory

class OrderEnum(Enum):
    PIZZA = "pizza"
    PASTA = "pasta"
    SALAD = "salad"

class Franchise:

    GET_ORDER_INPUT_COMMAND = "What would you like to order, pizza, pasta, or salad? "
    UNRECOGNIZED_SELECTION_OUTPUT = "Unable to recognize selection, please try again"
    GET_COUNT_INPUT_COMMAND = "How many would you like? "
    UNRECOGNIZED_COUNT_OUTPUT = "Unable to recognize number, please try again"
    
    def __init__(self, location_number: int) -> None:
        '''Instantiates a Franchise Object
        
        location_number = The store number
        '''
        self.location_number = location_number

    def place_order(self) -> None:
        '''Places an order and logs it to the log
        '''
        order_string = Franchise.__get_order()
        order = OrderFactory.create_order(order_string)
        #count = Franchise.__get_order_count()
        logger.log_transaction(order, self.location_number)

    def __get_order() -> str:
        '''Private method that computes and returns a valid order string
        '''
        while True:
            entry = input(Franchise.GET_ORDER_INPUT_COMMAND)
            entry = entry.strip().lower()
            for available_order in OrderEnum:
                if entry == available_order.value:
                    return entry
            print(Franchise.UNRECOGNIZED_SELECTION_OUTPUT + "\n")

    def __get_order_count() -> int:
        '''Unused private method for future use to get more than one of a single order'''
        while True:
            entry = input(Franchise.GET_COUNT_INPUT_COMMAND)
            entry = entry.strip().lower()
            try:
                return int(entry)
            except:
                print(Franchise.UNRECOGNIZED_COUNT_OUTPUT + "\n")