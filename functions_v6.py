def get_words(file_name:str):
    with open(file_name) as f:
        WORD_LIST = f.read().lower().split(',')
        # WORD_LIST.sort()
    return WORD_LIST


def print_some_set_values(words:set[str], amount)-> None:
    counter = 1
    for word in words:
        print(word, end=" ")
        
        counter += 1
        if counter > amount: 
            print("\n")
            break

def green_letters(letters: tuple, words):
    new_answers = []
    for word in words:
        validWord = True
        for letterIndex, letter in enumerate(letters):
            if letter is None: continue

            if word[letterIndex] != letter:
                validWord = False
                break
        
        if validWord: new_answers.append(word)
    
    return new_answers

            

def yellow_letters(letters: tuple, words):
    new_answers = []
    for word in words:
        for letterIndex, letter in enumerate(letters):
            if letter is None: continue

            if letter not in word:
                validWord = False
                break

            if word[letterIndex] == letter: 
                validWord = False
                break

            validWord = True
        
        if validWord: new_answers.append(word)
    
    return new_answers
                   

def gray_letters(letters: tuple, words):
    new_answers = []
    for word in words:
        validWord = True
        for letter in letters:
            if letter in word:
                validWord = False
                break
        
        if validWord: new_answers.append(word)
    
    return new_answers




def get_actions()-> int:
    description = "GREEN\t=> 1 \t\tGRAY\t=> 3 \nYELLOW\t=> 2 \t\tEXIT\t=> ENTER"
    print(description)

    while True:
        action = input("CHOOSE AN ACTION: ")

        # check if user chose EXIT
        if not action:
            print("EXIT PROGRAM")
            exit(1)
        
        # check if the user input isn't a number 
        try:
            action = int(action)
        except ValueError:
            print("CHOOSE A NUMBER!")
            continue
        
        # check if the number is in the right range (1-3)
        if 1 <= action <= 3:
            return action
        else: print("CHOOSE A VALID NUMBER BETWEEN 1-3")

# letters start
def check_letters(letters:tuple)->bool:
    for letter in letters:
        if letter.isalpha(): continue
        if letter == ".": continue
        return False

    return True


def format_letters(letters:tuple)->tuple:
    formatted_letters = []
    for character in letters:
        if character.isalpha(): formatted_letters.append(character.lower())
        else: formatted_letters.append(None)
    
    return tuple(formatted_letters)

def get_letters():
    a = 0
    # description = "INPUT LETTERS WITH DOTS TO FILL IN THE BLANKS (EX: FL..E). PRESS ENTER TO GO BACK"
    # print(description)

    while True:
        letters = input("INPUT LETTERS: ")
        if not letters: return ()

        if len(letters) > 5:
            print("INVALID AMOUNT OF CHARACTERS! MAX 5")
            continue
        
        letters = tuple(letters)
        validInput = check_letters(letters)
        if not validInput:
            print("ENTER A VALID INPUT! LETTERS AND DOTS ONLY")
            continue
        else: return format_letters(letters)
    
        


