from functions_v6 import *
import random

def main()->None:
    WORD_LIST = get_words("wordle-words.txt")
    current_answers = WORD_LIST.copy()

    print(random.choices(current_answers, k=3))

    while True:
        action = get_actions()
        letters = get_letters()

        # if letters: break
    
        match action:
            case 1: current_answers = green_letters(letters, current_answers)
            
            case 2: current_answers = yellow_letters(letters, current_answers)

            case 3: current_answers = gray_letters(letters, current_answers)

        answer_length = len(current_answers)    
        print(f"amount of possible words: {answer_length}")

        if answer_length > 50:
            print(current_answers[:10])
        elif answer_length > 0: print(current_answers)
        else: print("NO ANSWER, PLEASE TRY AGAIN")

        print("")


def testing()->None:
    WORD_LIST = get_words("wordle-words.txt")

    for i in range(10): print(WORD_LIST[i])
    
 
    


if __name__ == "__main__":
    main()
    # testing()