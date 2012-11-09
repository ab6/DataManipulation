import cPickle as pickle
import functions
from functions import *

#if haven't already done, break up test and train files and create term vectors for train docs
if not os.path.isdir("./testb/"):
	os.makedirs("/home/amber/Documents/Code/DataManipulation/testb")
	splitDocsToFiles("/home/amber/Documents/Code/DataManipulation", "eng.testb", "/testb")
if not os.path.isdir("./train/"):
	os.makedirs("./train")
	splitDocsToFiles("/home/amber/Documents/Code/DataManipulation", "eng.train", "/train")
	pkl_tvs("./train")

#Get file names of term vector pkl files in training set
tvFilenames = getFileNames("./train", ".pkl")

#For all test files:
#	create term vector
#	get cosign sim with all train term vectors and save in dict with train pkl file name
#	sort dict and get top ___
#	re-aggregate the respective training files
#	train model with new training set
#	tag test text and save to file
for testFile in getFileNames("./testb", "parsed"):
	testVector = make_tv("./testb/" + testFile)
	topDocs = getTopDocs(testVector, getFileNames("./train", "pkl"), "./train", 20)
	for doc, sim in topDocs:
	


