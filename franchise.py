from logger import logger
from helper import Helper
from order_factory import OrderFactory
import constants



class Franchise:
    
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
        count = Franchise.__get_order_count()
        logger.log_transaction(order, self.location_number, count)

    def __get_order() -> str:
        '''Private method that computes and returns a valid order string
        '''
        while True:
            entry = input("\n" + constants.GET_ORDER_INPUT_COMMAND_STRING)
            entry = entry.strip().lower()
            for available_order in Helper.OrderEnum:
                if entry == available_order.value:
                    return entry
            print(constants.UNRECOGNIZED_SELECTION_OUTPUT_STRING + "\n")

    def __get_order_count() -> int:
        '''Unused private method for future use to get more than one of a single order'''
        while True:
            entry = input(constants.GET_COUNT_INPUT_COMMAND_STRING)
            entry = entry.strip().lower()
            try:
                return int(entry)
            except:
                print(constants.UNRECOGNIZED_COUNT_OUTPUT_STRING + "\n")