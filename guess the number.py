#MShep TTA
#Sept 2021
#random guess
import random # imports the random library

print ("\n\tHello and welcome to the Guess your number game \n\n")

myName = input("Hello! What is your name?")
number = random.randint(1,10)
print("Well, " + myName +  "I am thinking of a number between 1 and 10.")

guess = int(input("Take a guess:") )

if guess == number:
    print("Good job, " + myName + " You guessed my number")
else:
   print("Wrong, better luck next time")

