import time
from browser import document, window
from browser.local_storage import storage
from constants import Constants

from errors import log_errors

default_code = open('default_template.py').read()

@log_errors
def reset():
    document[Constants.CONSOLE_TEXTAREA_ID].value = ''
    wrapper = document[Constants.MESSAGE_INPUT_WRAPPER_ID]
    wrapper.innerHTML = wrapper.innerHTML # Quick way to strip event listeners

@log_errors
def run(src):
    reset()
    storage[Constants.LOCAL_STORAGE_KEY] = src
    t0 = time.perf_counter()
    exec(src, {'__name__':'__main__'})
    print('<completed in %6.2f ms>' % ((time.perf_counter() - t0) * 1000.0))

@log_errors
def main():
    editor = window.ace.edit("editor")
    editor.setTheme("ace/theme/monokai")
    editor.session.setMode("ace/mode/python")
    editor.focus()
    editor.scrollToRow(0)
    editor.gotoLine(0)
    editor.setOptions({
        'enableLiveAutocompletion': True,
        'highlightActiveLine': False,
        'highlightSelectedWord': True,
        'fontSize': '16px'
    })
    editor.setValue(dict(storage).get(
        Constants.LOCAL_STORAGE_KEY,
        default_code
    ))

    def reset_to_default():
        editor.setValue(default_code)

    document[Constants.RUN_BUTTON_ID].bind('click', lambda *args: run(editor.getValue()))
    document[Constants.RESET_BUTTON_ID].bind('click', lambda *args: reset_to_default())

if __name__ == "__main__":
    print("Python initialised...")
    main()
