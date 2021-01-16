import random
r = random.randint(1,100)
while True:
	num = input("guess the number: ")
	num = int(num)
	if num == r:
		print('Bingo!')
		break 
	elif num > r:
		print('Your number is larger than the correct answer')
	elif num < r:
		print ('Your number is smaller than the correct answer')