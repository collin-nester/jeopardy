#Collin and Negus' Jeopardy! game.
#Credit to Merv Griffin for inventing Jeopardy
#Credit to kite.com for the dictionary creation method code

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
            
def game_start_and_rules():
    print("Welcome to Jeopardy! This is only basic Jeopardy, no Daily Doubles, Double Jeopardy, or Final Jeopardy.")
    print("The program will ask you to choose a category, and you should fully type in which one you want.")
    print("You will then be asked to type in the dollar amount. No need to type the dollar sign ($), just the number.")
    print("It will ask you the question, and you should type in what you think the answer is. Capitilization does not matter, but spelling does.")
    print("You win money for correct answers and lose money for wrong ones. The game ends when you run out of questions.")
    print("Have fun!")

def ask_category():
    global category
    g = 0
    while g != 1:
        category = input("Choose a category: " + str(", ".join(categories_list) + "    "))
        for i in categories_list:
            if category[2:5] == i[2:5]:
                category = i
                g = 1
        if g != 1:
            print("Error, please enter a category. ")
            
        
    
def ask_dollar_amount():
    global current_question, real_answer, dollar_amount, question_reference
    current_dollar_availability = []
    for i in dollar_list:
        if category in i:
            if i[-3:] == "000":
                current_dollar_availability.append(i[-4:])
            else:
                current_dollar_availability.append(i[-3:])
    g = 0
    while g != 1:
        dollar_amount = input("Choose a dollar amount: $" + str(", $".join(current_dollar_availability) + "    "))
        if dollar_amount in current_dollar_availability:
            dollar_amount = int(dollar_amount)
            g = 1
        if g != 1:
            print("Please choose an available dollar amount. ")
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
        print("$" + str(score))
    if correctness == False:
        print("Incorrect. The answer was " + real_answer)
        score -= dollar_amount
        print("$" + str(score))
        
def remove_question():
    del questions_dictionary[question_reference]
    del answers_dictionary[question_reference]
    dollar_list.remove(question_reference)

def category_removal():
    n = 0
    for i in questions_dictionary:
        if category in i[0:len(category)]:
            n += 1
    if n == 0:
        categories_list.remove(category)

def game_end():
    if score >= 0:
        print("Thanks for playing Jeopardy. Your total winnings for this game are $" + str(score))
    if score < 0:
        print("Thanks for playing Jeopardy. You lost $" + str(score))

game_start_and_rules()
while len(categories_list) > 0:
    ask_category()
    ask_dollar_amount()
    ask_question()
    check_answer()
    remove_question()
    category_removal()
game_end()
