import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if next_val > current_val:
        return (user_input == 'h')
    return (user_input == 'l')

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    result = False
    for i in range(len(word)):
        if letter == word[i]:
            result = True
    if result:
        print("Well done!", letter, "is in the word")
    else:
        print("Sorry,", letter, "is not in the word")
    return result, board

