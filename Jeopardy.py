#Collin and Negus' Jeopardy! game.
#Credit to Merv Griffin for inventing Jeopardy
#Credit to no one so far for borrowing pieces of code

score = 0

with open('/Users/collinnester24/Documents/python/GitHub/Jeopardy/categories_formatted.txt', 'r') as reader:
    categories_list = reader.readlines()

def questions_dictionary_creation():
    questions_dictionary = {}
    with open('/Users/collinnester24/Documents/python/GitHub/Jeopardy/questions_formatted.txt', 'r') as reader:
        for line in reader:
            key, value = line.split("~")
            questions_dictionary[key] = value

def answers_dictionary_creation():
    answers_dictionary = {}
    with open('/Users/collinnester24/Documents/python/GitHub/Jeopardy/answers_formatted.txt', 'r') as reader:
        for line in reader:
            key, value = line.split("~")
            answers_dictionary[key] = value

def ask_category():
    pass

def ask_dollar_amount():
    pass

def ask_question():
    pass

def check_answer():
    pass

def remove_question():
    pass

def category_removal():
    pass

def game_end():
    pass

questions_dictionary_creation()
answers_dictionary_creation()
while len(categories_list) > 0:
    ask_category()
    ask_dollar_amount()
    ask_question()
    check_answer()
    remove_question()
    category_removal()
game_end()