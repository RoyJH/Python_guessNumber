import random
from art import logo
from replit import clear
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
max_num = 101
tries = 0

difficulty = {"easy": 9999999, "normal": 10, "hard": 5, "custom": "custom"}

def check_guess(pick, guess):
    if pick == guess:
        print("Thats right, you win!")
        end = True
        return end
    elif pick < guess:
        print("Lower")
        end = False
        return end
    elif pick > guess:
        print("Higher")
        end = False
        return end

def setup_game():
    print(logo)
    print("Welcome to my gussing game.")
    print("The rules are simple: Guess the correct number. You have limited guesses.")
    print("'Easy': 9999999 tries. \n'Normal': 10 tries\n'Hard': 5 tries\n'Custom: User sets tries and number range'")
    print("Select your difficulty:")
    tries = difficulty[input("Select one of the following: 'easy', 'normal', 'hard', or 'custom': ")]
    return tries
    
def play_game(tries):
    if tries == "custom":
        tries = int(input("How many tries would you like: "))
        max_num = int(input("What's the maximum number in number range: ")) + 1
        print(tries)
    else:
        #tries = int(difficulty[tries])
        max_num = 101
    nums = [num for num in range(1,max_num)]
    pick = random.choice(nums)
    guess = 0
    end = False
    while end == False:
        if tries != 0:
            print(f"Tries remaining: {tries}.")
        if tries <= 0:
            print(f"Out of tries. The correct number is: {pick}")
            end = True
        else:
            guess = int(input(f"Pick a number between 1 and {max_num -1}: "))
            end = check_guess(pick=pick, guess=guess)
            tries -= 1
    print("Would you like to play again?")
    again = input("'yes' or 'no': ")
    if again == "yes":
        clear()
        tries = setup_game()
        play_game(tries)
    elif again == "no":
        print("I hope you had fun. Goodbye!")
    else:
        print("Invalid option. Exiting program...")
        

tries = setup_game()
play_game(tries)
