import sys
import time
import tb as traceback
import javascript

from browser import document as doc, window, alert
from browser.local_storage import storage
from browser import html

editor = window.ace.edit("editor")
editor.setTheme("ace/theme/solarized_dark")
editor.session.setMode("ace/mode/python")
editor.focus()

editor.setOptions({
    'enableLiveAutocompletion': True,
    'highlightActiveLine': False,
    'highlightSelectedWord': True
})

def reset_src():
    if storage is not None and "py_src" in storage:
        editor.setValue(storage["py_src"])
    else:
        editor.setValue('for i in range(10):\n\tprint(i)')
    editor.scrollToRow(0)
    editor.gotoLine(0)

class cOutput:
    encoding = 'utf-8'

    def __init__(self):
        self.cons = doc["console"]
        self.buf = ''

    def write(self, data):
        self.buf += str(data)

    def flush(self):
        self.cons.value += self.buf
        self.buf = ''

    def __len__(self):
        return len(self.buf)

cOut = cOutput()
sys.stdout = cOut
sys.stderr = cOut

info = sys.implementation.version
version = '%s.%s.%s' % (info.major, info.minor, info.micro)
if info.releaselevel == "rc":
    version += f"rc{info.serial}"

output = ''

def show_console(ev):
    doc["console"].value = output
    doc["console"].cols = 60

# run a script, in global namespace if in_globals is True
def run(*args):
    global output
    doc["console"].value = ''
    src = editor.getValue()
    if storage is not None:
       storage["py_src"] = src

    t0 = time.perf_counter()
    try:
        ns = {'__name__':'__main__'}
        exec(src, ns)
        state = 1
    except Exception as exc:
        traceback.print_exc(file=sys.stderr)
        state = 0
    sys.stdout.flush()
    output = doc["console"].value

    print('<completed in %6.2f ms>' % ((time.perf_counter() - t0) * 1000.0))
    return state

def show_js(ev):
    src = editor.getValue()
    doc["console"].value = javascript.py2js(src, '__main__')

reset_src()

doc['show_js'].bind('click', show_js)
doc['run'].bind('click',lambda *args: run())
doc['show_console'].bind('click', show_console)
