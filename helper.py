import constants
from enum import Enum

class Helper:
    
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

