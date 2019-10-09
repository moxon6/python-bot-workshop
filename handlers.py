import sys
import time
import tb as traceback
import javascript

from browser import document
from browser.local_storage import storage
from browser import html
from constants import CONSOLE_TEXTAREA_ID, LOCAL_STORAGE_KEY

class Handlers:
    def __init__(self, editor):
        self.editor = editor
        self.output = ""


    def show_console(self, ev):
        document[CONSOLE_TEXTAREA_ID].value = self.output
        document[CONSOLE_TEXTAREA_ID].cols = 60

    def run(self, *args):
        document[CONSOLE_TEXTAREA_ID].value = ''
        src = self.editor.getValue()
        if storage is not None:
            storage[LOCAL_STORAGE_KEY] = src

        t0 = time.perf_counter()
        try:
            ns = {'__name__':'__main__'}
            exec(src, ns)
            state = 1
        except Exception as exc:
            traceback.print_exc(file=sys.stderr)
            state = 0
        sys.stdout.flush()
        self.output = document[CONSOLE_TEXTAREA_ID].value

        print('<completed in %6.2f ms>' % ((time.perf_counter() - t0) * 1000.0))
        return state
    
    def show_js(self, ev):
        src = self.editor.getValue()
        document[CONSOLE_TEXTAREA_ID].value = javascript.py2js(src, '__main__')
