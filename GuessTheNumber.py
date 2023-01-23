import random
import os

def clear():
    os.system('cls')


difficulty_level = {
    "hard" : 5,
    "easy" : 10
}

def set_difficulty():
    return difficulty_level[input("Choose your starting difficulty, 'easy' or 'hard': ").lower()]

def check_answer(guess, answer, turns):
    if answer == guess:
        print(f"You guessed the number correctly!  It was {guess}.")
        return 0
    elif guess < answer:
        print(f"Your guess is too low.  Guess higher.")
        turns -= 1
        return turns
    else:
        print(f"Your guess is too high.  Guess lower.")
        turns -= 1
        return turns

def guess_the_number():
    turns = set_difficulty()
    answer = random.randint(1,100)
    clear()
    print("Welcome to the number guessing game.\n I'm thinking of a number between 1 and 100.")
    guess = int(input("Your guess: "))
    
    while turns != 0:
        turns = check_answer(guess, answer, turns)

        if turns > 0:
            print(f"You have {turns} guesses remaining.")
            guess = int(input("Next Guess: "))
        elif turns == 0:
            print(f"You are out of turns, the correct answer was {answer}.")
        
        

    play_again = input("Would you like to play again? yes/no ").lower()
    if play_again == 'yes':
        guess_the_number()


guess_the_number()