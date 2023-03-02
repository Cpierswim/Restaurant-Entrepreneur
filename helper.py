import constants
from enum import Enum
class Helper:

    def get_starting_log_number() -> int:
        '''Returns the number that the first log of the day should start with
        '''
        response = Helper.__ask_to_clear_log()
        if response == Helper.LogClearResponse.YES:
            Helper.clear_log()
            return constants.DEFAULT_STARTING_LOG_NUMBER
        else:
            count_log_file = open(constants.LOG_TRANSACTION_COUNT_FILE_NAME, "r")
            number = count_log_file.read()
            count_log_file.close()
            try:
                return int(number) + 1
            except:
                return constants.DEFAULT_STARTING_LOG_NUMBER
            

    def __ask_to_clear_log():
        '''Asks if the Logs should be cleared and returns a 'YES' or 'NO' LogClearResponse
        '''
        valid_entry = False
        while not valid_entry:
            entry = input(constants.CLEAR_LOGS_STRING)
            entry = entry.strip().lower()
            if entry == "yes" or entry == "y":
                valid_entry = True
                return Helper.LogClearResponse.YES
            elif entry == "no" or entry == "n":
                valid_entry = True
                return Helper.LogClearResponse.NO
            else:
                print(constants.UNRECOGNIZED_LOGS_ENTRY_MESSAAGE + "\n")
    
    def clear_log() -> None:
        '''Clears the log at constants.LOG_FILE_NAME
        '''
        log_file = open(constants.LOG_FILE_NAME, "w")
        log_file.write("")
        log_file.close()

    class OrderEnum(Enum):
        PIZZA = "pizza"
        PASTA = "pasta"
        SALAD = "salad"

    class LogClearResponse(Enum):
        YES = "YES"
        NO = "NO"



