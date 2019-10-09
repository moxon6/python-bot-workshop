from browser import document as doc, window
from browser import html
import editor


__BRYTHON__.debug = 1


# next functions are defined in editor.py
doc['show_js'].bind('click',editor.show_js)
# Create a lambda around editor.run() so that the event object is not passed to it
doc['run'].bind('click',lambda *args: editor.run())
doc['show_console'].bind('click',editor.show_console)

# erase "main" div
def clear_main(ev):
    doc['main'].text = ''

main_content = 'Zone with id="main" ; use it to test interaction with DOM elements'

# add "main" div
def add_main(ev):
    global main_content
    try:
        # if "main" div already exists, save content and erase container
        main_content = doc["main"].html
        doc["main_container"].html = ""
        doc["add_main"].text = 'Show "main" div'
    except KeyError:
        t = html.TABLE()
        row = html.TR()
        b = html.BUTTON('Clear')
        b.bind('click', clear_main)
        row <= html.TD(b)+html.TD(html.DIV(Id="main"))
        t <= row
        doc["main_container"] <= t
        doc["main"].html = main_content
        doc["add_main"].text = 'Hide "main" div'

doc["add_main"].bind('click', add_main)
