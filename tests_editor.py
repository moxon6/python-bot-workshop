from browser import document as doc, window
from browser import html
import header
import editor

qs_lang,language = header.show()

# other translations

trans = {
    'report_bugs':{'en':'Please report bugs in the ',
                   'es':'Poner los bugs en el ',
                   'fr':"Signalez les bugs dans l'"},
    'test_page':{'en':'Tests page','es':'P&aacute;gina de pruebas','fr':'Page de tests'},
    'run':{'en':'run','es':'ejecutar','fr':'Exécuter'},
    'clear':{'en':'clear','es':'borrar','fr':'Effacer'}
}

for key in trans:
    if key in doc:
        doc[key].html = trans[key].get(language,trans[key]['en'])

# link to test page
tplink = doc['test_page']
if qs_lang:
    tplink.attrs["href"] += '?lang=%s' %qs_lang

def set_debug(ev):
    if ev.target.checked:
        __BRYTHON__.debug = 1
    else:
        __BRYTHON__.debug = 0

__BRYTHON__.debug = int(doc['set_debug'].checked)

# bindings
doc['set_debug'].bind('change',set_debug)

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
