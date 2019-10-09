import sys
import time
import tb as traceback
from browser import document, window
from browser.local_storage import storage

default_code = open('default.py').read()

class Constants:
    LOCAL_STORAGE_KEY = "LOCAL_STORAGE_KEY"
    RUN_BUTTON_ID = 'execute_button'
    CONSOLE_TEXTAREA_ID = "console"

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

def run(editor):
    document[Constants.CONSOLE_TEXTAREA_ID].value = ''
    src = editor.getValue()
    if storage is not None:
        storage[Constants.LOCAL_STORAGE_KEY] = src

    t0 = time.perf_counter()
    try:
        ns = {'__name__':'__main__'}
        exec(src, ns)
        state = 1
    except Exception as exc:
        traceback.print_exc(file=sys.stderr)
        state = 0
    sys.stdout.flush()
    print('<completed in %6.2f ms>' % ((time.perf_counter() - t0) * 1000.0))
    return state

def main():
    sys.stdout = sys.stderr = ConsoleOutput()
    editor = window.ace.edit("editor")
    editor.setValue(dict(storage).get(Constants.LOCAL_STORAGE_KEY, default_code))
    document[Constants.RUN_BUTTON_ID].bind('click', lambda *args: run(editor))

main();