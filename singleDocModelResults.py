import functions
from functions import *

def findF1(results):
	f = open("/home/amber/Documents/Code/DataManipulation/testb/" + results, 'r')
	line = f.readline()
	while (line):
		if "Token-level Acc Level2" in line:
			while(line):
				if "Overall" in line:
					line = line.split()
					return line[3]
				line = f.readline()
		line = f.readline()
			
g = open("results50.txt", 'wb')
g.write("Filename\t\ttest\tLBJ\n")

total = 0
better = 0
worse = 0
diffBetter = []
diffWorse = []

lbjResults = getFileNames("./testb", "lbj")
ab6Results = getFileNames("./testb", "output")

for output in ab6Results:
	for lbj in lbjResults:
		if output[9:12] == lbj[9:12]:
			test = findF1(output)
			gold = findF1(lbj)
			g.write(output + "\t" + test + "\t" + gold + "\n")
			if float(test) > float(gold):
				better += 1
				diffBetter.append(float(test)-float(gold))
			elif float(test) < float(gold):
				worse += 1
				diffWorse.append(float(gold)-float(test))
			total += 1
avgBetter = sum(diffBetter)/float(len(diffBetter))
avgWorse = sum(diffWorse)/float(len(diffWorse))
			

g.write("\nTotal:\t" + str(total) + "\n")
g.write("Better:\t" + str(better) + "\n")
g.write("Worse:\t" + str(worse) + "\n\n")
g.write("AvgBetter\t" + str(avgBetter) + "\n")
g.write("AvgWorse\t" + str(avgWorse) + "\n")


