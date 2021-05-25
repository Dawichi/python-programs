import os
import sys

def mad_libs():
	os.system('cls' if os.name=='nt' else 'clear')
	print('┌───────────────────────────────────┐')
	print('│        1. Mad Libs game!          │')
	print('└───────────────────────────────────┘')
	print()
	print('Complete these data to build your own story')
	name = input("→ Protagonist's name: ")
	drink = input("→ Choose a drink: ")
	place = input("→ Choose a place: ")
	reason = input("→ Why is he/she there?: ")
	adjective = input("→ Choose an adjective (Describing word): ")
	print('------------------------------')
	print('Our', adjective, 'protagonist today is', name)
	print(name, 'is drinking', drink, 'in', place)
	print('because', reason)
	print('That was not a good story, but a real one.')
	print('------------------------------')

sys.modules[__name__] = mad_libs