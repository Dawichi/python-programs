import os
import sys
import random


def dice_roll():
	os.system('cls' if os.name=='nt' else 'clear')
	print('┌───────────────────────────────────┐')
	print('│           5. Dice roll!           │')
	print('└───────────────────────────────────┘')
	print()
	while True:
		throw_dice = random.randint(1, 6)
		if throw_dice == 1:
			print(one)
		if throw_dice == 2:
			print(two)
		if throw_dice == 3:
			print(three)
		if throw_dice == 4:
			print(four)
		if throw_dice == 5:
			print(five)
		if throw_dice == 6:
			print(six)
		print('Press ENTER to throw again')
		exit = input('Or type [exit]: ')
		if exit.lower() == 'exit':
			break


sys.modules[__name__] = dice_roll


one = '''
┌───────────┐
│           │
│     X     │
│           │
└───────────┘
'''
two = '''
┌───────────┐
│        X  │
│           │
│  X        │
└───────────┘
'''
three = '''
┌───────────┐
│        X  │
│     X     │
│  X        │
└───────────┘
'''
four = '''
┌───────────┐
│  X     X  │
│           │
│  X     X  │
└───────────┘
'''
five = '''
┌───────────┐
│  X     X  │
│     X     │
│  X     X  │
└───────────┘
'''
six = '''
┌───────────┐
│  X  X  X  │
│           │
│  X  X  X  │
└───────────┘
'''