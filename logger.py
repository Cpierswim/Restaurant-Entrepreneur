from order import Order
import constants
import locale
from helper import Helper

class Logger:

    def __init__(self, transaction_count: int = 1, daily_sales: int = 0) -> None:
        '''Instantiates a Logger Object
        
        transaction_count -- Optional. The beginning transaction number for this log. Default is 1
        daily_sales -- Optional. The beginning sales value for the day. Default is 0
        '''
        self.transaction_count = transaction_count - 1
        self.daily_sales = daily_sales

    def log_transaction(self, order: Order, store_number: int, count: int) -> None:
        '''Logs a transaction to the constants.LOG_FILE_NAME
        
        order - The order to log
        store_number - The store number to include in the log
        '''
        self.transaction_count += 1
        self.daily_sales += order.price * count
        log_file = open(constants.LOG_FILE_NAME, "a")
        log_number_file = open(constants.LOG_TRANSACTION_COUNT_FILE_NAME, "w")
        price = locale.currency(order.price, grouping=True)
        daily_sales = locale.currency(self.daily_sales, grouping= True)
        log = f"Transaction {self.transaction_count}: Store Number: {store_number} dish: {order.dish_name.ljust(20)} price: {price.ljust(6)} count: {str(count).ljust(3)} total daily sales: {daily_sales}\n"
        log_file.write(log)
        log_number_file.write(str(self.transaction_count))
        log_file.close()
        log_number_file.close()

staring_log_number = Helper.get_starting_log_number()
logger = Logger(staring_log_number)