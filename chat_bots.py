import sys
from console_output import ConsoleOutput

sys.stdout = sys.stderr = ConsoleOutput()

from browser import document, window, html
from constants import Constants

def register_bot(bot, bot_name):
    print("Registering bot...")
    document[Constants.BOT_NAME_ID].innerHTML = bot_name
    class Message:
        def __init__(self, text, sender):
            self.text = text
            self.sender = sender

    class Messages:
        messages = []

    def add_entry():
        dom_input = document[Constants.MESSAGE_INPUT_ID]
        message = Message(dom_input.value, "you")
        dom_input.value = ""
        Messages.messages.append(message)
        reply = Message(bot(message.text), "bot")
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