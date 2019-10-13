from browser import document, window, html
import sys

from app import ConsoleOutput

def register_bot(bot_response):
    sys.stdout = sys.stderr = ConsoleOutput()
    print("Registering bot...")
    class Message:
        def __init__(self, text, sender):
            self.text = text
            self.sender = sender

    class Messages:
        messages = []

    def add_entry():
        dom_input = document['message-input']
        message = Message(dom_input.value, "you")
        dom_input.value = ""
        Messages.messages.append(message)
        reply = Message(bot_response(message.text), "bot")
        Messages.messages.append(reply)
        render()

    def createLI(message):
        return html.LI([
            html.IMG(src=("assets/human.jpg" if message.sender == "you" else "assets/bot.gif")),
            html.P(message.text)
        ], Class=("replies" if message.sender == "you" else "sent"))

    def render():
        t = document["messages-list"]
        t.clear()
        t <= (createLI(message) for message in Messages.messages)

    def add_entry_return(ev):
        if (ev.keyCode == 13):
            add_entry()

    send = document['send']
    message_input = document['message-input']

    send.bind("click", lambda *args: message_input.click())
    message_input.bind("keydown", add_entry_return)
    render()
    print("Bot Registered")