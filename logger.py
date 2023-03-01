from order import Order
#from franchise import Franchise

class Logger:

    LOG_FILE_NAME = "log.txt"

    def __init__(self, transaction_count: int, daily_sales: int) -> None:
        self.transaction_count = transaction_count
        self.daily_sales = daily_sales

    def log_transaction(self, order: Order, store_number: int) -> None:
        self.transaction_count += 1
        self.daily_sales += order.price
        log_file = open(Logger.LOG_FILE_NAME, "a")
        log = f"Transaction {self.transaction_count}: Store Number: {store_number} dish: {order.dish_name} price: {order.price} total daily sales: {self.daily_sales}\n"
        log_file.write(log)
        log_file.close()

    def clear_log() -> None:
        log_file = open(Logger.LOG_FILE_NAME, "w")
        log_file.write("")
        log_file.close()


logger = Logger(0, 0)