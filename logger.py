from order import Order
#from franchise import Franchise

class Logger:

    LOG_FILE_NAME = "log.txt"

    def __init__(self, transaction_count: int = 1, daily_sales: int = 0) -> None:
        '''Instantiates a Logger Object
        
        transaction_count -- Optional. The beginning transaction number for this log. Default is 1
        daily_sales -- Optional. The beginning sales value for the day. Default is 0
        '''
        self.transaction_count = transaction_count - 1
        self.daily_sales = daily_sales

    def log_transaction(self, order: Order, store_number: int) -> None:
        '''Logs a transaction to the Logger.LOG_FILE_NAME
        
        order - The order to log
        store_number - The store number to include in the log
        '''
        self.transaction_count += 1
        self.daily_sales += order.price
        log_file = open(Logger.LOG_FILE_NAME, "a")
        log = f"Transaction {self.transaction_count}: Store Number: {store_number} dish: {order.dish_name} price: {order.price} total daily sales: {self.daily_sales}\n"
        log_file.write(log)
        log_file.close()

    def clear_log() -> None:
        '''Clears the log at Logger.LOG_FILE_NAME
        '''
        log_file = open(Logger.LOG_FILE_NAME, "w")
        log_file.write("")
        log_file.close()


logger = Logger()