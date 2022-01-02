#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random

def play(number_to_guess, number_of_attempts):
  #Flag to check if we found the number already
  found = False
  #Local variable for the number of attemps
  attempts = number_of_attempts
  
  #We enter a loop to make the user guess the number then we check if it's the correct one
  while not found and attempts > 0:
    print(f"You have {attempts} attempts ramaining to guess the number.")
    guess = int(input("Make a guess: "))
    #We decrease the number of attemps immediately after the guess
    attempts -= 1
    #We evaluate the guess
    if number_to_guess < guess:
      print("Too high.")
    elif number_to_guess > guess:
      print("Too low.")
    else:
      found = True
      print(f"You got it! The answer was {number_to_guess}.")
      break

    #We check if there are attempts left to continue the game
    if attempts > 0:
      print("Guess again.")
    else:
      print("You've run out of guesses. You lose.")


def start():
  #Let's include the ASCII art logo
  print(art.logo)
  #Introduction
  print("Welcome to the number guessing Game !\nI'm thinking of a number between 1 and 100.")
  #We think of a number between 1 and 100.
  answer = random.randint(1,100)
  #Optional phrase to show the number for debugging purposes
  #print(f"Psst, the correct answer is {answer}")

  #Let's ask the user to choose the difficulty level
  #TODO: Handle incorrect words
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  #We set the number of attemps according to the difficulty
  if difficulty == 'easy':
    attempts = 10
  else:
    attempts = 5

  #Now we play the game with the level of difficulty chosen
  play(answer, attempts)

start()