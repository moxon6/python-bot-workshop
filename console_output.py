from browser import document, window, html
from constants import Constants

class ConsoleOutput:
    encoding = 'utf-8'

    def __init__(self):
        self.buf = ""
        self.console = document[Constants.CONSOLE_TEXTAREA_ID]

    def write(self, data):
        self.buf = str(data)

    def flush(self):
        self.console.value += self.buf
        self.buf = ''

    def __len__(self):
        return len(self.buf)
