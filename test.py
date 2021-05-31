import os
import time

# Player
player_l1 = ['╭','─','╮']
player_l2 = ['╰','┬','╯']
player_l3 = ['╰','┼','╮']
player_l4 = ['╭','┴','╮']
player_l5 = ['╯',' ','╰']
player = [player_l1, player_l2, player_l3, player_l4, player_l5]


# Screen lines
line9 = ['─' for x in range(100)]
line8 = [' ' for x in range(100)]
line7 = [' ' for x in range(100)]
line6 = [' ' for x in range(100)]
line5 = [' ' for x in range(100)]
line4 = [' ' for x in range(100)]
line3 = [' ' for x in range(100)]
line2 = [' ' for x in range(100)]
line1 = [' ' for x in range(100)]
line0 = ['─' for x in range(100)]
screen = [line9, line8, line7, line6, line5, line4, line3, line2, line1, line0]

# Lateral borders
for x in screen:
	x[0] = '│'
	x[99] = '│'

# Corners
line9[0] = '┌'
line9[99] = '┐'
line0[0] = '└'
line0[99] = '┘'







def print_array(arr):
	result = ''
	for x in arr:
		result += str(x)
	print(result)


def print_player(x, y):
	if y >= 4:
		if y <= 9:
			if x >= 0:
				if x <= 97:
					print('yessssssssssss')



def main():
	playing = True
	while playing:
		os.system('cls' if os.name=='nt' else 'clear')
		for x in screen:
			print_array(x)
		time.sleep(2)






main()


