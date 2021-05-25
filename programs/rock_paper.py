import sys
import random
import os
import re
import time


def set_option(option):
	if option == 'R': return '⊚ - Rock'
	if option == 'P': return '▮ - Paper'
	if option == 'S': return '✂ - Scissors'
	return 'x'


def user_won(result):
	if result:
		print('┌───────────────────────────────────┐')
		print('│        🎉 🎉 YOU WIN!!!           │')
		print('└───────────────────────────────────┘')
	else:
		print('┌───────────────────────────────────┐')
		print('│        😥 😥 You lose...          │')
		print('└───────────────────────────────────┘')
	input('Exit game...')



def rock_paper():
	os.system('cls' if os.name=='nt' else 'clear')
	print('┌───────────────────────────────────┐')
	print('│     3. Rock, Paper, Scissors!     │')
	print('└───────────────────────────────────┘')
	print()
	print("I'ts a best of five game")
	print('The first one in reach 3 core points wins')
	input('Start...')

	user_points = 0
	cpu_points = 0
	playing = True
	
	while playing:
		if user_points == 3:
			user_won(True)
			break
		if cpu_points == 3:
			user_won(False)
			break


		os.system('cls' if os.name=='nt' else 'clear')
		print('┌───────────────────────────────────┐')
		print('│             USER        CPU       │')
		print('│ Score:        {}           {}       │'.format(user_points, cpu_points))
		print('└───────────────────────────────────┘')
		print('Rock, Paper, Scissors - Shoot!')

		user_pick = input('→ Choose your weapon [R]ock], [P]aper, or [S]cissors: ')
		if not re.match('[SsRrPp]', user_pick):
			print('Oops! \nSorry, that is a invalid character :(')
			input()
			continue

		print('Preparing my choice...')
		time.sleep(1)
		options = ['R', 'P', 'S']
		npc_pick = random.choice(options)
		user_pick = str.upper(user_pick)
		print('\nUSER:   {}'.format(set_option(user_pick)))
		print('\nNPC:    {}'.format(set_option(npc_pick)))
		print('\nSo the winner is...')
		time.sleep(3)

		if npc_pick == user_pick:
			print("It's a DRAW! \nNo points distribution")
			input('Continue...')
		elif (npc_pick == 'R' and user_pick == 'S') or (npc_pick == 'P' and user_pick == 'R') or (npc_pick == 'S' and user_pick == 'P'):
			print('I win! \n1 Point for CPU')
			cpu_points += 1
			input('Continue...')
		else:
			print('You win! \n1 Point for USER')
			user_points += 1
			input('Continue...')

sys.modules[__name__] = rock_paper