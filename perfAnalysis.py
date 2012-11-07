
def compare():
	f = open("/home/ab6/Downloads/eng.testb_formatted", 'r')
	g = open("/home/ab6/Downloads/output_formatted.txt", 'r')

	totalCount = 0
	TP_Corr = 0
	TP_Wrong = 0
	TN = 0
	FP = 0
	FN = 0
	

	for gold in f:
		gold = gold.split()
		test = g.readline().split()
		if gold[0] != test[0]:
			print(totalCount)
			return
		if len(gold) == 1:
			if len(test) == 1:
				if gold != test:
					print ("error " + str(totalCount))
				TN += 1
			else:
				FP += 1
		else:
			if len(test) == 1:
				FN += 1
			else: 
				if gold[1] != test[1]:
					TP_Wrong +=1
				else:
					TP_Corr += 1
		totalCount += 1

	print("Totalcount = " + str(totalCount))
	print("True Pos Correct = " + str(TP_Corr))
	print("True Pos Wrong = " + str(TP_Wrong))
	print("True Neg = " + str(TN))
	print("False Pos = " + str(FP))
	print("False Neg = " + str(FN))
	
	f.close()
	g.close()


def formatAnnotated():
	f = open("/home/ab6/Downloads/output.txt", 'r')
	g = open("/home/ab6/Downloads/output_formatted.txt", 'w')

	saved = ""
	for line in f:
		if line.split():
			for word in line.split():
				if word[0] == "[" and len(word) > 1:
					saved = word[1:]
				elif word[len(word)-1] == "]" and len(word) > 1:
					g.write(word[:len(word)-1] + " " + saved + "\n")
				else:
					g.write(word + "\n")

	f.close()
	g.close()

def formatGold():
	f = open("/home/ab6/Downloads/eng.testb", 'r')
	g = open("/home/ab6/Downloads/eng.testb_formatted", 'w')

	for line in f:
		if line.split():
			line = line.split()
			if line[0] != "-DOCSTART-":
				if line[3] != "O":
					g.write(line[0] + " " + line[3][2:] + "\n")
				else:
					g.write(line[0] + "\n")

	f.close()
	g.close()

formatGold()
formatAnnotated()
compare()
