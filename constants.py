import locale

GET_ORDER_INPUT_COMMAND_STRING = "What would you like to order, pizza, pasta, or salad? "
UNRECOGNIZED_SELECTION_OUTPUT_STRING = "Unable to recognize selection, please try again"
GET_COUNT_INPUT_COMMAND_STRING = "How many would you like? "
UNRECOGNIZED_COUNT_OUTPUT_STRING = "Unable to recognize number, please try again"

CLEAR_LOGS_STRING = "Would you like to clear the log, YES or NO: "
LOGS_CLEARED_MESSAGE = "Logs cleared"
UNRECOGNIZED_LOGS_ENTRY_MESSAAGE = "Entry not recognized, please try again"

LOG_FILE_NAME = "log.txt"
LOG_TRANSACTION_COUNT_FILE_NAME = "log_number.txt"

DEFAULT_STARTING_LOG_NUMBER = 41

PIZZA_NAME = "Cheese Pizza"
PIZZA_PRICE = 11.99

PASTA_NAME = "Spagetti"
PASTA_PRICE = 9.99

SALAD_NAME = "Chef's Salad"
SALAD_PRICE = 8.99

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')