import sys
import time
import tb as traceback
from browser import document, window
from browser.local_storage import storage
from constants import Constants
from console_output import ConsoleOutput

sys.stdout = sys.stderr = ConsoleOutput()

default_code = open('default_template.py').read()


def run(editor):
    document[Constants.CONSOLE_TEXTAREA_ID].value = ''
    wrapper = document[Constants.MESSAGE_INPUT_WRAPPER_ID]
    wrapper.innerHTML = wrapper.innerHTML # Quick way to strip event listeners
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
    editor = window.ace.edit("editor")
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
    editor.setValue(dict(storage).get(Constants.LOCAL_STORAGE_KEY, default_code))
    document[Constants.RUN_BUTTON_ID].bind('click', lambda *args: run(editor))

if __name__ == "__main__":
    main()
