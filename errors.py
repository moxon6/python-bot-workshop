import tb as traceback
import sys
from console_output import ConsoleOutput

def log_errors(func):
    sys.stdout = sys.stderr = ConsoleOutput()

    def wrapper(*args):
        try:
            return func(*args)
        except:
            print(traceback.format_exc())
    return wrapper