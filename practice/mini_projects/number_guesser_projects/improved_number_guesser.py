
#number guesser

import random
number = random.randint(1,50)  #random number between 1 and 50

#number =input("enter a number between 1 and 50: ")

import random
number = random.randint(1,50)
print("\nWelcome to my Number Guesser Mini Project\n".upper())
def number_guesser():
    print("I am thinking of a number between 1 and 50, can you guess?\n You have 3 attempts")
    attempt = 3
    secret_number = number
 
    guess = int(input("Your number: "))
    while not (1 <= guess <= 50):
        print("Invalid number!, please choose between 1 and 50")
        guess = int(input("Your number: "))
 #1st Attempt
    attempt -= 1  
    if guess == number:
        print("You guessed right, congratulations!")
    elif guess > number:
        print("Too high!")
    else:
        print("Too low!")
    print( f"You have {attempt} more attempts")

    #2nd Attempt
    attempt -= 1
    guess = int(input("Your number: "))
    if number % 2 == 0:
        print("Hint: The number is even!")
    else: 
        print("Hint: The number is odd!")
    print("You have 1 more attempt")

    #3rd Attempt
    if guess == int(input("Your number: ")):
        print("Correct! You guessed it in 3 tries!")
    else: 
        print("Gameover!")

    print(f"The number is {number}")


number_guesser()


#Computer: "I’m thinking of a number between 1 and 100."
#Player: 50
#Computer: "Too low!"
#Player: 75
#Computer: "Too high!"
#Player: 63
#Computer: "Correct! You guessed it in 3 tries!"


#Original code 


'''import random
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

'''