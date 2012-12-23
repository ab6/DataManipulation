import cPickle as pickle
import functions
from functions import *

path = "/home/amber/Code/DataManipulation"

#if haven't already done, break up test and train files and create term vectors for train docs
if not os.path.isdir("./testb/"):
	os.makedirs(path + "/testb")
	splitDocsToFiles(path, "eng.testb", "/testb")
	createPlainFiles(path, "eng.testb", "/testb")
if not os.path.isdir("./train/"):
	os.makedirs("./train")
	splitDocsToFiles(path, "eng.train", "/train")
	createPlainFiles(path, "eng.train", "/train")
	pkl_tvs("./train")

#For all test files:
#	create term vector
#	get cosign sim with all train term vectors and save in dict with train pkl file name
#	sort dict and get top ___
#	re-aggregate the respective training files
#	train model with new training set
#	tag test text and save to file
files = getFileNames("./testb", "parsed")

for testFile in files:
	testVector = make_tv("./testb/" + testFile)
	topDocs = getTopDocs(testVector, getFileNames("./train", "pkl"), "./train", 50)
	f = open(path + "/testb/" + testFile[:len(testFile)-10] + "train.txt", "wb")
	for doc in topDocs:
		f.write("O\t0\t0\tO\t-X-\t-DOCSTART-\tx\tx\tO\n")
		g = open(path + "/train/" + doc, 'r')
		lines = g.readlines()
		for line in lines:
			f.write(line)
		g.close()
	f.close()
		


