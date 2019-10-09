from browser import document as doc, window
from browser import html
import editor

__BRYTHON__.debug = 1
doc['show_js'].bind('click',editor.show_js)
doc['run'].bind('click',lambda *args: editor.run())
doc['show_console'].bind('click',editor.show_console)
