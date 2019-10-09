from browser import document as doc, window
from browser import html
import editor


__BRYTHON__.debug = 1

# next functions are defined in editor.py
doc['show_js'].bind('click',editor.show_js)
# Create a lambda around editor.run() so that the event object is not passed to it
doc['run'].bind('click',lambda *args: editor.run())
doc['show_console'].bind('click',editor.show_console)
