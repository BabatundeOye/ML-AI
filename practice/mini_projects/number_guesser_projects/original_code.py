
import random
number = random.randint(1,50)
def number_guesser():
    print("I am thinking of a number between 1 and 50, can you guess?")
    secret_number = number
    attempts = 3

    guess = int(input("Your number: "))
    if guess == number:
        print("You guessed right, congratulations!")
    else: 
        print("you have 2 more attempts")
    
    guess = int(input("Your number: "))
    if guess == number:
        print("You guessed right, congratulations!")
    else: 
        print("you have 1 more attempts")

    guess = int(input("Your number: "))
    if guess == number:
        print("You guessed right, congratulations!")
    else: 
        print("gameover")


number_guesser()
