from browser import document, window, html
import editor

class Message:
    def __init__(self, text):
        self.text = text

class Messages:
    messages = []

def get_text(row):
    return list(row.get(selector="INPUT"))[0].value

def add_entry(row):
    Messages.messages.append(
        Message(get_text(row))
    )
    render()


def render():
    document["table"].clear()
    
    t = html.TABLE()
    document["table"] <= t
    
    t <= html.TR(html.TH("Messages"))
    t <= (html.TR(html.TD(message.text)) for message in Messages.messages)


    row = html.TR()
    row <= html.TD(html.INPUT(name="new_message"))
    button = html.BUTTON("Add")
    row <= html.TD(button)
    t <= row
    button.bind("click", lambda ev: add_entry(ev.target.parent.parent))

render()