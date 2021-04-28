def multiplication_table(number):
	multiplier = 1
	while multiplier <= 5:
		result = multiplier * number
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		multiplier += 1

multiplication_table(3)

multiplication_table(5)

multiplication_table(8)	