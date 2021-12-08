#Collin and Negus' Jeopardy! game.
#Credit to Merv Griffin for inventing Jeopardy
#Credit to no one so far for borrowing pieces of code

score = 0

with open('/Users/collinnester24/Documents/python/GitHub/Jeopardy/categories_formatted.txt', 'r') as reader:
    categories_list = reader.readlines()

for i, k in enumerate(categories_list):
    categories_list[i] = categories_list[i].strip()

questions_dictionary = {}
with open('/Users/collinnester24/Documents/python/GitHub/Jeopardy/questions_formatted.txt', 'r') as reader:
    for line in reader:
        key, value = line.split("~")
        value = value.strip()
        questions_dictionary[key] = value

answers_dictionary = {}
with open('/Users/collinnester24/Documents/python/GitHub/Jeopardy/answers_formatted.txt', 'r') as reader:
    for line in reader:
        key, value = line.split("~")
        value = value.strip()
        answers_dictionary[key] = value
 
dollar_list = []
for i, j in enumerate(categories_list):
    for k in range(5):
        dollar_list.append(str(j) + " " + str(200 * ( k + 1 )))
            
def ask_category():
    global category
    category = input("Choose a category: " + str(categories_list) + " ")
    for i in categories_list:
        if category[2:5] == i[2:5]:
            category = i
    
def ask_dollar_amount():
    global current_question, real_answer, dollar_amount, question_reference
    dollar_amount = int(input("Choose a dollar amount: " + str(score)))

    question_reference = str(category) + " " + str(dollar_amount)
    real_answer = answers_dictionary[question_reference]
    current_question = questions_dictionary[question_reference]
    
def ask_question():
    global correctness
    answer = input(current_question + " ")
    if real_answer.lower() in answer.lower():
        correctness = True
    else:
        correctness = False

def check_answer():
    global score
    if correctness == True:
        print("Answer is correct. Good job! ")
        score += dollar_amount
        print(score)
    if correctness == False:
        print("Incorrect. The answer was " + real_answer)
        score -= dollar_amount
        print(score)
    #You don't really need to do anything before this: just change it so it prints what question 
        
def remove_question():
    del questions_dictionary[question_reference]
    del answers_dictionary[question_reference]
    dollar_list.remove(question_reference)

def category_removal():
    print(dollar_list)
    for i in categories_list:
        if i not in dollar_list:
            categories_list.remove(i)

def game_end():
    if score >= 0:
        print("Thanks for playing Jeopardy. Your total winnings for this game are $" + str(score))
    if score < 0:
        print("Thanks for playing Jeopardy. You lost $" + str(score))

while len(categories_list) > 0:
    ask_category()
    ask_dollar_amount()
    ask_question()
    check_answer()
    remove_question()
    category_removal()
game_end()
