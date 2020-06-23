#This is a  Number Guessing Game

# using Python

#Here has the rules of this game using these rules this game is created
'''
In the program, while loop runs until the number guessed by the user is equal to the generated number or the number of

attempts is less than the maximum number of chances. If the number of attempts becomes greater than the number of chances

the game stops and the user loses the game. If the user guesses the correct number in the given number of chances then he

or she will win. After every guess made by the user, the program informs the user whether the guessed number was smaller,

greater than the actual generated number.

In this code, a random number is generated between 1-9 using the randint() function.

The user is given a specific number of chances to guess the number if the chances exceed the user guesses the user would lose.


'''

import random

print("                                     WELL TO GUSSING GAME\nNumber guessing game")

# randint function to generate the

number = random.randint(1, 9)


# chances are 5
chances = 0

print("Guess a number (between 1 and 9):")

# While loop to count the number

while chances < 5:

    # Enter a number between 1 to 9
    guess = int(input())

    # Compare the user entered number

    if guess == number:


        print("Congratulation YOU WON!!!")
        break


    elif guess < number:
        print("Your guess was lower then the random number: Guess a number higher than", guess)

    # The user entered number is
    # greater than the generated

    else:
        print("Your guess was higher then the random number: Guess a number lower than", guess)

    # Increase the value of chance by 1
    chances += 1

# Check whether the user
# guessed the correct number
if not chances < 5:
    print("YOU LOSE!!! The number is", number)


