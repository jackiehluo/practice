words = {
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven",
	8: "eight",
	9: "nine",
	10: "ten",
	11: "eleven",
	12: "twelve",
	13: "thirteen",
	14: "fourteen",
	15: "fifteen",
	16: "sixteen",
	17: "seventeen",
	18: "eighteen",
	19: "nineteen",
	20: "twenty",
	30: "thirty",
	40: "forty",
	50: "fifty",
	60: "sixty",
	70: "seventy",
	80: "eighty",
	90: "ninety",
	100: "hundred",
	1000: "thousand"
	}

total = 0

a, b = (int(x) for x in raw_input().split())

for number in range(a, b + 1):
	letters = 0
	if len(str(number)) == 1:
		letters = len(words[number])
	elif len(str(number)) == 2:
		if number in words:
			letters = len(words[number])
		else:
			ones = number % 10
			tens = number - ones
			letters = len(words[tens]) + len(words[ones])
	elif len(str(number)) == 3:
		if number % 100 == 0:
			hundreds = number / 100
			letters = len(words[hundreds]) + len(words[100])
		elif number % 10 == 0:
			tens = number % 100
			hundreds = (number - tens) / 100
			letters = len(words[hundreds]) + len(words[100]) + 3 + len(words[tens])
		else:
			ones = number % 10
			tens = (number - ones) % 100
			hundreds = (number - tens - ones) / 100
			if tens / 10 > 1:
				letters = len(words[hundreds]) + len(words[100]) + 3 + len(words[tens]) + len(words[ones])
			elif tens / 10 == 1:
				letters = len(words[hundreds]) + len(words[100]) + 3 + len(words[tens + ones])
			else:
				letters = len(words[hundreds]) + len(words[100]) + 3 + len(words[ones])
	else:
		letters = len(words[1]) + len(words[1000])
	total += letters


print total
