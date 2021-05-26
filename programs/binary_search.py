import os
import sys
import re
import time

def binary_search():
	test_arr = [12, 15, 18, 22, 24, 27, 31, 35, 38, 40, 43, 46, 49, 54, 57, 61]
	os.system('cls' if os.name=='nt' else 'clear')
	print('┌───────────────────────────────────┐')
	print('│    4. Binary Search Algorithm     │')
	print('└───────────────────────────────────┘')
	print()
	print('Binary search visualized')
	print('This algorithm divides the array recursively until find a value in a list')
	print()
	print('Test array:')
	print_encapsulated(test_arr)
	print()
	while True:
		user_pick = input('→ Choose between [I]nterative or [R]ecursive implementation: ')
		if not re.match('[IiRr]', user_pick):
			print('Oops! \nSorry, that is a invalid option :(')
			input()
			continue
		user_pick = str.upper(user_pick)
		search = ask_num()
		if user_pick == 'I':
			print('-------------------------------------')
			print('The interactive search consist in check the number in the middle of the array')
			print('If it is the value, done! If its greater, then we select the first half. Else, we select the second')
			print('By this way, the time cost of the search is heavily reduced in long ordered arrays')			
			print('Interactively searching for', search, '...')
			time.sleep(1)
			result = binary_search_interative(test_arr, search)
			if result:
				print('\nThe number is in the', result+1, 'position of the array!')
			else:
				print('\nSorry, the number is not in the array :(')
		else:
			print('Recursively searching for', search, '...')
			binary_search_recursive(test_arr, search)
		break
	
sys.modules[__name__] = binary_search


# An input that only allows integers 
def ask_num():
	while True:
		number = input('→ Which number are you looking for?')
		try:
			int(number)
			return int(number)
		except ValueError:
			try:
				float(number)
				print("This is a float")
				continue
			except ValueError:
				print("This is not a number")
				continue


# Prints an array of 1-digit int in box cells
def print_encapsulated(arr):
	top = '────┬'
	mid = ' '
	bot = '────┴'
	top_line = '┬'
	mid_line = '│'
	bot_lane = '┴'
	for x in arr:
		top_line += top
		mid_line += (mid + str(x) + ' │')
		bot_lane += bot
	print(top_line)
	print(mid_line)
	print(bot_lane)


# Interative implementation
def binary_search_interative(arr, x):
	low = 0
	high = len(arr) - 1
	counter = 0
	print('Array is ' + str(len(arr)-1) + ' digit long')
	while low <= high:
		counter += 1
		mid = (low + high) // 2
		print('\n-------------------------------------')
		print('Steps: ' + str(counter))
		print('  Index search: [' + str(mid) +']')
		print('  Split in num: ' + str(arr[mid]))
		print_encapsulated(arr[low:int(mid)])
		print_encapsulated([arr[int(mid)]])
		print_encapsulated(arr[int(mid)+1:high])
		if arr[mid] == x:
			return int(mid)
		elif arr[mid] > x:
			high = mid - 1
		elif arr[mid] < x:
			low = mid + 1


# recursive implementation
def binary_search_recursive(arr, x):
	low = 0
	high = len(arr) - 1
	if len(arr) == 0:
		return -1
	else:
		mid = (low + high) // 2
		if arr[mid] == x:
			return mid
		else:
			if arr[mid] < x:
				return binary_search_recursive(arr[mid + 1:], x)
			else:
				return binary_search_recursive(arr[:mid], x)