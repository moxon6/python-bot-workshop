from browser import document, window, html
import editor

class Message:
    def __init__(self, text, sender):
        self.text = text
        self.sender = sender

class Messages:
    messages = []

def add_entry():
    message = Message(document['message-input'].value, "You")
    Messages.messages.append(message)
    reply = Message(bot_response(message.text), "Bot")
    Messages.messages.append(reply)
    render()

def bot_response(text):
    return text[::-1]

def render():
    document["table"].clear()
    t = html.TABLE()
    document["table"] <= t
    t <= html.TR(html.TH("Messages"))
    t <= (html.TR(html.TD(message.sender + " : " + message.text)) for message in Messages.messages)

document['send'].bind("click", lambda *args: add_entry())
render()