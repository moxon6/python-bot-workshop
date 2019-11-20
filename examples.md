# Guessing game example

```
from chat_bots import register_bot

bot_word = "pens"
bot_word_len = len(bot_word)

num_guesses = 0

def guess_word_bot(text):
    global num_guesses
    num_guesses += 1
    
    if not len(text) == bot_word_len:
        return wrong_len_msg(bot_word_len)

    num_cows = 0
    num_bulls = 0

    for index, letter in enumerate(text):
        if is_letter_bull(bot_word, index, letter):
            num_bulls += 1
        elif is_letter_cow(bot_word, letter):
            num_cows += 1
    
    return win_msg(num_guesses, bot_word) if num_bulls == bot_word_len \
        else char_count_msg(num_cows, num_bulls)
    
def is_letter_bull(bot_word, index, letter):
    return bot_word[index] == letter

def is_letter_cow(bot_word, letter):
    return letter in bot_word

def pluraliser(num, ending="s"):
    return "" if num == 1 else ending
   
def char_count_msg(num_cows, num_bulls):
    return f"""
        Close, but no cigar. 
        Your guess had {num_cows} cow{pluraliser(num_cows)} 
        and {num_bulls} bull{pluraliser(num_bulls)}. 
        That's {num_guesses} guess{pluraliser(num_guesses, "es")}. 
        Try again!
        """

def wrong_len_msg(bot_word_len):
    return f"""
        Oh-oh. I'm thinking of a {bot_word_len} letter word. 
        Maybe I should have mentioned that earlier. Oops! 
        That still counts, so you've used up {num_guesses} 
        guess{pluraliser(num_guesses, "es")}.
        """

def win_msg(num_guesses, bot_word):
    return f"""
        You win! Only {num_guesses} guess{pluraliser(num_guesses, "es")}. 
        It was {bot_word} I was thinking of.
        """

def bot_name(bot_word_len):
    return f"""
        Cows and bulls: guess the {bot_word_len}-letter word. 
        I'll tell you how you've done - 
        "Cow" means a letter in the wrong position, while 
        "Bull" means a letter in the right position.
        Good luck!
        """
   
register_bot(guess_word_bot, bot_name(bot_word_len))
```
