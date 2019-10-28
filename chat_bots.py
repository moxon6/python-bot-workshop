from browser import document, window, html, timer
from constants import Constants
from errors import log_errors

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

    @log_errors
    def add_entry():
        dom_input = document[Constants.MESSAGE_INPUT_ID]
        if len(dom_input.value) is 0:
            return
        message = Message(dom_input.value, "you")
        dom_input.value = ""
        Messages.messages.append(message)
        Messages.bot_typing = True
        response = bot(message.text)
        if type(response) is str and len(response) > 0:
            reply = Message(response, "bot")
        else:
            reply = Message("No Response from bot", "bot")
        render()

        @log_errors
        def bot_reply():
            Messages.bot_typing = False
            Messages.messages.append(reply)
            render()
        timer.set_timeout(bot_reply, 1000)

    def create_bot_typing_message():
        return html.LI([
            html.DIV([
                html.IMG(src=("assets/bot.gif"), Class="profile-image"),
                html.DIV([
                    html.IMG(src="assets/loading.gif", Class="loading-message")
                ], Class="loading-message-wrapper")
            ], Class="message-wrapper")
        ], Class="replies")

    def createLI(message): 
        sender = message.sender == "you"
        return html.LI([
            html.DIV([
                html.IMG(src=("assets/human.jpg" if sender else "assets/bot.gif"), Class="profile-image"),
                html.DIV([
                    html.P(message.text, Class="message-text")
                ], Class="message-text-wrapper")
            ], Class="message-wrapper")
        ], Class=("sent" if sender else "replies"))

    def render():
        message_list = document["messages-list"]
        message_list.clear()
        message_list <= (createLI(message) for message in Messages.messages)

        if Messages.bot_typing:
            message_list.append(create_bot_typing_message())

    def add_entry_return(ev):
        if (ev.keyCode == 13):
            add_entry()

    send = document['send-message']
    message_input = document['message-input']

    send.bind("click", lambda *args: add_entry())
    message_input.bind("keydown", add_entry_return)
    render()
    print("Bot Registered")