import cPickle as pickle
import functions
from functions import *

#if haven't already done, break up test and train files and create term vectors for train docs
if not os.path.isdir("./testb/"):
	os.makedirs("/home/amber/Documents/Code/DataManipulation/testb")
	splitDocsToFiles("/home/amber/Documents/Code/DataManipulation", "eng.testb", "/testb")
	createPlainFiles("/home/amber/Documents/Code/DataManipulation", "eng.testb", "/testb")
if not os.path.isdir("./train/"):
	os.makedirs("./train")
	splitDocsToFiles("/home/amber/Documents/Code/DataManipulation", "eng.train", "/train")
	createPlainFiles("/home/amber/Documents/Code/DataManipulation", "eng.train", "/train")
	pkl_tvs("./train")

#For all test files:
#	create term vector
#	get cosign sim with all train term vectors and save in dict with train pkl file name
#	sort dict and get top ___
#	re-aggregate the respective training files
#	train model with new training set
#	tag test text and save to file
for testFile in getFileNames("./testb", "parsed"):
	testVector = make_tv("./testb/" + testFile)
	topDocs = getTopDocs(testVector, getFileNames("./train", "pkl"), "./train", 50)
	f = open("/home/amber/Documents/Code/DataManipulation/testb/" + testFile[:len(testFile)-10] + "train.txt", "wb")
	for doc in topDocs:
		f.write("O\t0\t0\tO\t-X-\t-DOCSTART-\tx\tx\tO\n")
		g = open("/home/amber/Documents/Code/DataManipulation/train/" + doc, 'r')
		lines = g.readlines()
		for line in lines:
			f.write(line)
		g.close()
	f.close()
		


