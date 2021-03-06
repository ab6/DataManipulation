import re
import os
import cPickle as pickle
from math import sqrt
import operator

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
	topSim = sortedDict[:num]
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
	string = ""
	lineCount = 0
	for eachLine in oDoc:
      		if newFileKey in eachLine:
         		if newTaggedFile: 
				newTaggedFile.close()
         		count = count + 1
			if count < 10:
				fileTagged = filepath + folder + "/" + filename + "00" + str(count) + "tagged.txt"
			elif count < 100:   
				fileTagged = filepath + folder + "/" + filename + "0" + str(count) + "tagged.txt"      		
			else:
				fileTagged = filepath + folder + "/" + filename + str(count) + "tagged.txt"
         		newTaggedFile = open(fileTagged, 'w')
   		else:
			if eachLine.strip():
         			newTaggedFile.write(lbjFormat(eachLine, lineCount))
				lineCount += 1
			else:
				newTaggedFile.write("\n")
				lineCount = 0

   	newTaggedFile.close()
   	oDoc.close()

#Format line for Lbj tagger
def lbjFormat(line, count):
	string = ""
	remString = ""
        cut = line.find(' ')
        word = line[:cut]
        remString = line[cut + 1:]
        cut = remString.find(' ')
        spot2 = remString[:cut]
        remString = remString[cut + 1:]
        cut = remString.find(' ')
        spot3 = remString[:cut]
        remString = remString[cut + 1:]
        cut = remString.find(' ')
        spot4 = remString[:cut]
        return (spot4 +'\t' + '0\t' + str(count)+ '\t' + spot3 +'\t' + spot2 + '\t' + word + '\tx\t' + 'x\t' + 'x\n')

	
def createPlainFiles(filepath, filename, folder):
	oDoc = open (filepath + "/" + filename)
	count = 0
  	newFileKey = "-DOCSTART-"
	newParsedFile = ""
	string = ""
	for eachLine in oDoc:
      		if newFileKey in eachLine:
         		if newParsedFile: 
				newParsedFile.close()
         		count = count + 1
			if count < 10:
				fileParsed = filepath + folder + "/" + filename + "00" + str(count) + "parsed.txt"
			elif count < 100:   
				fileParsed = filepath + folder + "/" + filename + "0" + str(count) + "parsed.txt"      		
			else:
				fileParsed = filepath + folder + "/" + filename + str(count) + "parsed.txt"
         		newParsedFile = open(fileParsed, 'w')
   		else:
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
	newParsedFile.close()
   	oDoc.close()

