import random
r = random.randint(1,100)

count = 0
start = input("Enter the start of the random number range")
end = input("Enter the end of the random number range")
start = int(start)
end = int(end)

while True:
	count = count + 1 #count += 1
	num = input("guess the number: ")
	num = int(num)
	if num == r:
		print('Bingo!')
		break 
	elif num > r:
		print('Your number is larger than the correct answer')
	elif num < r:
		print ('Your number is smaller than the correct answer')
	print('You have tried ', count, 'time(s)')