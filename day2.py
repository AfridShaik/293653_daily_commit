txt = input()
word_list = txt.split()

for i in word_list :
	if (len(i) == len(max(word_list ,key =len))):
		print(i)