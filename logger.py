from order import Order

class Logger:

    def __init__(self, transaction_count: int, daily_sales: int) -> None:
        self.transaction_count = transaction_count
        self.daily_sales = daily_sales

    def log_transaction(order: Order, count: int) -> None:
        pass