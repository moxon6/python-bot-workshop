from chat_bots import register_bot

def reverser_bot(text):
    return text[::-1]

register_bot(reverser_bot)