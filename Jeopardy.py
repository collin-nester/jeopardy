#Collin and Negus' Jeopardy! game.
#Credit to Merv Griffin for inventing Jeopardy
#Credit to no one so far for borrowing pieces of code

score = 0

with open('/Users/collinnester24/Documents/python/GitHub/Jeopardy/categories_formatted.txt', 'r') as reader:
    categories_list = reader.readlines()

questions_dictionary_creation():
questions_dictionary = {}
with open('/Users/collinnester24/Documents/python/GitHub/Jeopardy/questions_formatted.txt', 'r') as reader:
    for line in reader:
        key, value = line.split("~")
        questions_dictionary[key] = value

answers_dictionary_creation():
answers_dictionary = {}
with open('/Users/collinnester24/Documents/python/GitHub/Jeopardy/answers_formatted.txt', 'r') as reader:
    for line in reader:
        key, value = line.split("~")
        answers_dictionary[key] = value
 
dollar_dictionary = {}
with open('/Users/collinnester24/Documents/python/GitHub/Jeopardy/dollars_formatted.txt', 'r') as reader:
    for line in reader:
        key, value = line.split("~")
        dollar_dictionary[key] = value
            
            
def ask_category():
    Category = input("Choose a category: " + categories_list)
    for i in catgories_list:
        if Category[2:5] == i[2:5]:
            Category == i
    
def ask_dollar_amount():
    for i in questions_dictionary:
        Dollar_amount = list[$200, $400, $600, $800, $1000]

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
