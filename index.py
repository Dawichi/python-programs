import os
from programs import mad_libs
from programs import num_guess
from programs import rock_paper
from programs import binary_search

def start_game():
	wanna_play = True
	while wanna_play:
		os.system('cls' if os.name=='nt' else 'clear')
		print('╔═══════════════════════════════════╗')
		print('║     Welcome to programs menu!     ║')
		print('╟───────────────────────────────────╢')
		print('║     ♦ 1. Mad Libs Generator       ║')
		print('║     π 2. Number guessing          ║')
		print('║     X 3. Rock Paper Scissors      ║')
		print('║     O 4. Binary Search            ║')
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
			if program == 'exit':
				valid = True
				break
			print()
			print('Ooops!')
			print('There is not any program assigned to that number :(')
			print('Please, try again')
		
		print('END! \n \n \nPress ENTER to go back to programs menu')
		play_again = input("Do you wanna exit? (Type 'yes' to exit): ")
		print()
		if (play_again.lower() == "yes") | (play_again.lower() =="exit"):
			print("That's cool, have a good day!")
			wanna_play = False
			break
		

if __name__ == '__main__':
    start_game()