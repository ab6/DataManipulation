import functions
from functions import *

def findF1(f):
	line = f.readline()
	while (line):
		if "Token-level Acc Level2" in line:
			while(line):
				if "Overall" in line:
					line = line.split()
					return line
				line = f.readline()
		line = f.readline()
	
			
g = open("results20.txt", 'wb')
g.write("Filename\t\ttest\tLBJ\n")

total = 0
better = 0
worse = 0
diffBetter = []
diffWorse = []
totTokens = 0
sumTestF1 = 0
sumGoldF1 = 0

lbjResults = getFileNames("./testb", "lbj")
ab6Results = getFileNames("./testb", "output")

for output in ab6Results:
	for lbj in lbjResults:
		if output[9:12] == lbj[9:12]:
			outputFile = open("/home/amber/Documents/Code/DataManipulation/testb/" + output, 'r')
			lbjFile = open("/home/amber/Documents/Code/DataManipulation/testb/" + lbj, 'r')
			testLine = findF1(outputFile)
			lbjLine = findF1(lbjFile)
			testF1 = float(testLine[3])
			goldF1 = float(lbjLine[3])
			testTot = int(testLine[4])
			g.write(output + "\t" + str(testF1) + "\t" + str(goldF1) + "\n")
			if testF1 > goldF1:
				better += 1
				diffBetter.append(testF1-goldF1)
			elif testF1 < goldF1:
				worse += 1
				diffWorse.append(goldF1-testF1)
			total += 1
			totTokens += testTot
			sumTestF1 += testF1 * testTot
			sumGoldF1 += goldF1 * testTot
			outputFile.close()
			lbjFile.close()
avgBetter = sum(diffBetter)/float(len(diffBetter))
avgWorse = sum(diffWorse)/float(len(diffWorse))
avgTestF1 = sumTestF1/float(totTokens)
avgGoldF1 = sumGoldF1/float(totTokens)

g.write("\nTotal:\t" + str(total) + "\n")
g.write("Better:\t" + str(better) + "\n")
g.write("Worse:\t" + str(worse) + "\n\n")
g.write("AvgBetter\t" + str(avgBetter) + "\n")
g.write("AvgWorse\t" + str(avgWorse) + "\n")
g.write("AvgTestF1\t" + str(avgTestF1) + "\n")
g.write("AvgGoldF1\t" + str(avgGoldF1) + "\n")

g.close()


