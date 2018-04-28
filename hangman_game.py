import os
import random
import sys


#make a list of words
words = ["guide",
"ultimate",
"delete",
"slides","sunny",
"repository", "request",
"setting",
"explore",
"wisdom",
"apple",
"banana",
"cobra",
"tentacles",
"waterfall"]


def clear():
	""" clear the terminal """
	
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')


def draw(wrong_guesses,right_guesses,random_word):
	""" Make appear the strikes and blank word line spaces """
	
	clear()
	print('Strikes: {}/7'.format(len(wrong_guesses)))
	print ('')
	for letter in wrong_guesses:
		print(letter,)
	print('\n\n')
	for letter in random_word:
		if letter in right_guesses:
			print (letter, end = '')
		else:
			print("_", end = '')
	print('')


def get_guess(wrong_guesses,right_guesses):
	""" return the guess """
	
	while True:
		guess= input("Guess a letter: ").lower()
		if len(guess) != 1:
			print ("You only can guess 1 letter at a time")
		elif guess in wrong_guesses or guess in right_guesses:
			print ("You guessed that letter already before")
		elif not guess.isalpha():
			print ("You only can use letters")
		else:
			return guess


def play(done):
	""" Start the game loop """
	
	clear()
	random_word = random.choice(words)
	wrong_guesses = []
	right_guesses = []

	while True:
		draw(wrong_guesses, right_guesses, random_word)
		guess = get_guess(wrong_guesses, right_guesses)
		if guess in random_word:
			right_guesses.append(guess)
			found = True
			for letter in random_word:
				if letter not in right_guesses:
					found = False
			if found:
				print ("You Win!!! CONGRATULATIONS!!!")
				print("The secret word was {}".format(random_word))
				done = True
		else:
			wrong_guesses.append(guess)
			if len(wrong_guesses) == 7:
				draw(wrong_guesses, right_guesses, random_word)
				print ("You Lost!  T_T")
				print ("The secret word was {}".format(random_word))
				done = True

		if done:
			play_again = input("Wanna Play Again? Y/n").lower()
			if play_again != "n":
				return play(done = False)
			else:
				sys.exit()


def welcome():
	""" Introduce the directions """
	
	start = input("Press enter/return to start, or enter Q to quit ").lower()
	if start == "q":
		print ("Bye Bye! Hope you come back and play!")
		sys.exit()
	else:
		return True


print("Welcome to the Hangman Game!! ")
done = False
while True:
	clear()
	welcome()
	play(done)
