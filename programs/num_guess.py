import os
import sys
import random
attempts_list = []

def show_score():
	print('-------------------------------------')
	if len(attempts_list) <= 0:
		print('HIGHSCORE: 0')
		print("There is currently no high score, it's yours for the taking!")
	else:
		print('HIGHSCORE: {} attempts'.format(min(attempts_list)))
	print('-------------------------------------')



def num_guess():
	os.system('cls' if os.name=='nt' else 'clear')
	print('┌───────────────────────────────────┐')
	print('│     2. Number guessing game!      │')
	print('└───────────────────────────────────┘')
	print()
	print('Try to guess the number in the fewest possible attempts!')
	show_score()
	print("Are you ready to play?")
	random_number = int(random.randint(1, 100))
	attempts = 0
	playing = True 

	while playing:
		try:
			print()
			guess = input('→ Pick a number between 1 and 100: ')
			if int(guess) < 1 or int(guess) > 100:
				raise ValueError("Please guess a number within the given range")
			# Success
			if int(guess) == random_number:
				print("Nice! You got it!")
				attempts += 1
				attempts_list.append(attempts)
				print("It took you {} attempts".format(attempts))
				play_again = input("Would you like to play again? (Enter Yes/No) ")
				attempts = 0
				show_score()
				random_number = int(random.randint(1, 100))
				if play_again.lower() == "no":
					break
			# Lower
			elif int(guess) > random_number:
				print("It's lower, go DOWN ↓")
				attempts += 1
			# Higher
			elif int(guess) < random_number:
				print("It's higher, go UP ↑")
				attempts += 1

		except ValueError as err:
			print()
			print("Oh no!, that is not a valid value :(")
			print("Try again...")
			print("({})".format(err))



sys.modules[__name__] = num_guess