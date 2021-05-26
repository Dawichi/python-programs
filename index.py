import os
from programs import mad_libs
from programs import num_guess
from programs import rock_paper
from programs import binary_search
from programs import dice_roll

def start():
	alive = True
	while alive:
		os.system('cls' if os.name=='nt' else 'clear')
		print('╔═══════════════════════════════════╗')
		print('║     Welcome to programs menu!     ║')
		print('╟───────────────────────────────────╢')
		print('║     ♦ 1. Mad Libs Generator       ║')
		print('║     π 2. Number guessing          ║')
		print('║     X 3. Rock Paper Scissors      ║')
		print('║     O 4. Binary Search            ║')
		print('║     ∷ 5. Dice roll                ║')
		print('╚═══════════════════════════════════╝')
		print('Here you can pick between the programs available!')

		valid = False
		while not valid:
			program = input('→ Type the number of your desired program: ')
			if program == '1':
				valid = True
				mad_libs()
				break
			if program == '2':
				valid = True
				num_guess()
				break
			if program == '3':
				valid = True
				rock_paper()
				break
			if program == '4':
				valid = True
				binary_search()
				break
			if program == '5':
				valid = True
				dice_roll()
				break
			if program == 'exit':
				valid = True
				break
			print()
			print('Ooops!')
			print('There is not any program assigned to that number :(')
			print('Please, try again')
		
		print('\nEND! \n \n \nPress ENTER to go back to programs menu')
		play_again = input("Do you wanna exit? (Type 'yes' to exit): ")
		print()
		if (play_again.lower() == "yes") | (play_again.lower() =="exit"):
			print("That's cool, have a good day!")
			alive = False
			break
		

if __name__ == '__main__':
    start()