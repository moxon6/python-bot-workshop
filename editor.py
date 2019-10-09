import sys
import time
import tb as traceback
import javascript

from browser import document, window, alert
from browser.local_storage import storage
from browser import html
from handlers import Handlers
from console import ConsoleOutput
import constants

editor = window.ace.edit("editor")
editor.setTheme("ace/theme/solarized_dark")
editor.session.setMode("ace/mode/python")
editor.focus()
editor.scrollToRow(0)
editor.gotoLine(0)
editor.setOptions({
    'enableLiveAutocompletion': True,
    'highlightActiveLine': False,
    'highlightSelectedWord': True
})

sys.stdout = sys.stderr = ConsoleOutput()

if storage is not None and constants.LOCAL_STORAGE_KEY in storage:
    editor.setValue(storage[constants.LOCAL_STORAGE_KEY])
else:
    editor.setValue('for i in range(10):\n\tprint(i)')

handlers = Handlers(editor)
document[constants.JAVASCRIPT_BUTTON_ID].bind('click', handlers.show_js)
document[constants.RUN_BUTTON_ID].bind('click', lambda *args: handlers.run())
document[constants.PYTHON_BUTTON_ID].bind('click', handlers.show_console)

