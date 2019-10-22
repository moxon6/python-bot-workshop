import sys
from console_output import ConsoleOutput

sys.stdout = sys.stderr = ConsoleOutput()

from browser import document, window, html, timer
from constants import Constants

def register_bot(bot, bot_name):
    print("Registering bot...")
    document[Constants.BOT_NAME_ID].innerHTML = bot_name
    class Message:
        def __init__(self, text, sender):
            self.text = text
            self.sender = sender

    class Messages:
        bot_typing = False
        messages = []

    def add_entry():
        dom_input = document[Constants.MESSAGE_INPUT_ID]
        message = Message(dom_input.value, "you")
        dom_input.value = ""
        Messages.messages.append(message)
        Messages.bot_typing = True
        render()

        def bot_reply():
            # Messages.bot_typing = False
            reply = Message(bot(message.text), "bot")
            Messages.messages.append(reply)
            render()
        timer.set_timeout(bot_reply, 1000)

    def createLI(message): 
        sender = message.sender == "you"
        return html.LI([
            html.DIV([
                html.IMG(src=("assets/human.jpg" if sender else "assets/bot.gif"), Class="profile-image"),
                html.DIV([
                    html.P(message.text, Class="message")
                ], Class="message-container")
            ], Class="li-container")
        ], Class=("sent" if sender else "replies"))

    def render():
        message_list = document["messages-list"]
        message_list.clear()
        message_list <= (createLI(message) for message in Messages.messages)

        bot_typing = document["bot-typing"]
        bot_typing.clear()
        if Messages.bot_typing:
            bot_typing.innerHTML = "%s is typing..." % bot_name


    def add_entry_return(ev):
        if (ev.keyCode == 13):
            add_entry()

    send = document['send']
    message_input = document['message-input']

    send.bind("click", lambda *args: add_entry())
    message_input.bind("keydown", add_entry_return)
    render()
    print("Bot Registered")