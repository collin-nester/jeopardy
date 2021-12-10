#Collin and Negus' Jeopardy! game.
#Credit to Merv Griffin for inventing Jeopardy
#Credit to kite.com for the dictionary creation method code
#What Negus did: game_start_and_rules, ask_question, check_answer, game_end
#What Collin did: dictionary and list creation, category_removal
#What we both did: ask_category, ask_dollar_amount, remove_question
#Pseudocode and Brainstorm were both of us


#Defines the score variable, which keeps track of the user's score
score = 0

#This creates a categories list from the categories formatted document;
#it will be used to keep track of what categories are still available

with open('/Users/collinnester24/Documents/python/GitHub/Jeopardy/game1/categories_formatted.txt', 'r') as reader:
    categories_list = reader.readlines()

#This takes all items in the categories list
#and removes spaces and newline characters
for i, k in enumerate(categories_list):
    categories_list[i] = categories_list[i].strip()

#This code makes the questions and answers dictionaries from a file,
#which are used to store the questions and answers with a key of
#their category and their dollar value and value of the question
#or answer, depending on the dictionary. These are not modified
#through the rest of the program
questions_dictionary = {}
with open('/Users/collinnester24/Documents/python/GitHub/Jeopardy/game1/questions_formatted.txt', 'r') as reader:
    for line in reader:
        key, value = line.split("~")
        value = value.strip()
        questions_dictionary[key] = value

answers_dictionary = {}
with open('/Users/collinnester24/Documents/python/GitHub/Jeopardy/game1/answers_formatted.txt', 'r') as reader:
    for line in reader:
        key, value = line.split("~")
        value = value.strip()
        answers_dictionary[key] = value
 
#This code makes a list of all dollar amounts derived from adding
#the numbers 200-1000 in increments of 200 to each category. This
#list is modified throughout the code to eliminate questions that
#have already been played.
dollar_list = []
for i, j in enumerate(categories_list):
    for k in range(5):
        dollar_list.append(str(j) + " " + str(200 * ( k + 1 )))
            
#This defines the function that prints the rules at the start of
#the game.
def game_start_and_rules():
    print("Welcome to Jeopardy! This is only basic Jeopardy, no Daily Doubles, Double Jeopardy, or Final Jeopardy.")
    print("The program will ask you to choose a category, and you should fully type in which one you want.")
    print("You will then be asked to type in the dollar amount. No need to type the dollar sign ($), just the number.")
    print("It will ask you the question, and you should type in what you think the answer is. Capitilization does not matter, but spelling does.")
    print("You win money for correct answers and lose money for wrong ones. The game ends when you run out of questions.")
    print("Have fun!")

#This defines the function that asks the user what category
#they would like to choose.
def ask_category():
    global category
    g = 0
    #This loop runs while a category has not been properly
    #entered by the user; in the loop, the user is asked to
    #choose a category in categories list, and if the 3rd-6th
    #characters match a category in the categories list, then
    #the category is defined as whatever it matched in the 
    #categories list and the while loop is broken. If the
    #3rd-6th characters do not match, it will print an error
    #message and rerun the previous code.
    while g != 1:
        category = input("Choose a category: " + str(", ".join(categories_list) + "    "))
        for i in categories_list:
            if category[2:5] == i[2:5]:
                category = i
                g = 1
        if g != 1:
            print("Error, please enter a category. ")
            
#This defines the function that asks the user what dollar 
#amount question they want
def ask_dollar_amount():
    global current_question, real_answer, dollar_amount, question_reference
    #Creates a blank list, then adds all the dollar values 
    #remaining in the current category to it
    current_dollar_availability = []
    for i in dollar_list:
        if category in i:
            if i[-3:] == "000":
                current_dollar_availability.append(i[-4:])
            else:
                current_dollar_availability.append(i[-3:])
    g = 0
    #Prints a list of dollar amounts and asks the user
    #what dollar amount they want
    while g != 1:
        dollar_amount = input("Choose a dollar amount: $" + str(", $".join(current_dollar_availability) + "    "))
        if dollar_amount in current_dollar_availability:
            dollar_amount = int(dollar_amount)
            g = 1
        if g != 1:
            print("Please choose an available dollar amount. ")
    #Defines several variables
    question_reference = str(category) + " " + str(dollar_amount)
    real_answer = answers_dictionary[question_reference]
    current_question = questions_dictionary[question_reference]
    
#Defines the function which asks the user the question
#and sets the answer variable equal to it
def ask_question():
    global answer
    answer = input(current_question + " ")

#Defines the function which checks if the the answer is
#correct and either adds or subtracts the number of points
#from the score variable and prints the score
def check_answer():
    global score
    if real_answer.lower() in answer.lower():
        correctness = True
    else:
        correctness = False
    if correctness == True:
        print("Answer is correct. Good job! ")
        score += dollar_amount
        print("$" + str(score))
    if correctness == False:
        print("Incorrect. The answer was " + real_answer)
        score -= dollar_amount
        print("$" + str(score))
        
#This defines the function which removes the question,
#answer, and dollar amounts from their respective lists
def remove_question():
    del questions_dictionary[question_reference]
    del answers_dictionary[question_reference]
    dollar_list.remove(question_reference)

#This defines the function which removes the current
#category from the category list if there are no more
#questions in that catergory
def category_removal():
    n = 0
    for i in questions_dictionary:
        if category in i[0:len(category)]:
            n += 1
    if n == 0:
        categories_list.remove(category)

#This defines the function which prints the score and an
#ending message at the end of the game
def game_end():
    if score >= 0:
        print("Thanks for playing Jeopardy. Your total winnings for this game are $" + str(score))
    if score < 0:
        print("Thanks for playing Jeopardy. You lost $" + str(score))

#This calls all functions to run the game, looping the
#ones that need to be done until the end of the game
game_start_and_rules()
while len(categories_list) > 0:
    ask_category()
    ask_dollar_amount()
    ask_question()
    check_answer()
    remove_question()
    category_removal()
game_end()
