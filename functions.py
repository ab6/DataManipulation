import re
import os
import cPickle as pickle
from math import sqrt
import operator

#Annotate given file with trained tagger
def annotate(tagger, testFile):
#	if __name__ == "__main__":
#		startingDir = os.getcwd
	print ""

#TrainLBJtagger
def trainTagger(trainFile):
	print ""
	

#Get top ___ similar documents
#returns dict with pkl doc and sim to test vector
def getTopDocs(tv1, fileList, directory, num):
	docSims = dict()
	for trainPkl in fileList:
		f = open("./train/" + trainPkl, 'rb')
		tv2 = pickle.load(f)
		f.close()
		docSims[trainPkl] = cosign(tv1, tv2)
	sortedDict = sorted(docSims.iteritems(), key=operator.itemgetter(1), reverse=True)
	topSim = sortedDict[:20]
	docs = []
	for doc, sim in topSim:
		docs.append(doc[:(len(doc)-10)] + "tagged.txt")
	return docs

#Calculate cosine similarity btw two term vectors
def cosign(tv1, tv2):
	total = 0
	for word in tv1:
		if word in tv2:
			total += tv1[word] * tv2[word]
	return float(total) / (scalar(tv1) * (scalar(tv2)))

#Scalar: https://gist.github.com/288282 is where code came from
def scalar(tv):
	total = 0
	for word, count in tv.items():
		total += count * count
	return sqrt(total)

#Calculate all term vectors and save as pickle files
def pkl_tvs(directory):
	testFilenames = getFileNames(directory, "parsed")
	for filename in testFilenames:
		tv = make_tv(directory + "/" + filename)
		g = open(directory + "/" + filename[:(len(filename)-4)] + ".pkl", 'wb')
		pickle.dump(tv, g)

#Term vector from file
def make_tv(filename):
	f = open(filename, 'r')
	text = f.read()
	return calc_tv(text)

#Calculate term vector for text
def calc_tv(text):
	tv = dict()
  	results = re.split('\W+', text)
	for result in results:
      		lresult = result.lower()
		if not lresult.isdigit():
			if lresult in tv:
				tv[lresult] = tv[lresult] + 1
			else:
				tv[lresult] = 1
	return tv

#Get the names of certain files in a directory
def getFileNames(directory, matchPattern):
	dirList = os.listdir(directory)
	filenames = []
	for fname in dirList:
		if re.search(matchPattern, fname):
			filenames.append(fname)
	return filenames

#splits Reuters train or test file into individual docs, 
#both tagged and plain text
def splitDocsToFiles(filepath, filename, folder):
   	oDoc = open (filepath + "/" + filename)
	count = 0
  	newFileKey = "-DOCSTART-"
	newTaggedFile = ""
	newParsedFile = ""
	string = ""
	for eachLine in oDoc:
      		if newFileKey in eachLine:
         		if newTaggedFile: 
				newTaggedFile.close()
				newParsedFile.close()
         		count = count + 1
         		fileTagged = filepath + folder + "/" + filename + str(count) + "tagged" + ".txt"
         		newTaggedFile = open(fileTagged, 'w')
			fileParsed = filepath + folder + "/" + filename + str(count) + "parsed" + ".txt"
         		newParsedFile = open(fileParsed, 'w')
   		else:
         		newTaggedFile.write(eachLine)
			if eachLine.strip():
             			cut = eachLine.find(' ')
              			word = eachLine[:cut]
              			if not word == '.':
                 			string = string + word + " "
              			else:
                 			string = string + word
          		else:
              			newParsedFile.write(string + "\n")
				string = ""
   	newTaggedFile.close()
	newParsedFile.close()
   	oDoc.close()

