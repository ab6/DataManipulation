import re
import os
import shutil
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import cluster

#Get the names of certain files in a directory
def getFileNames(directory, matchPattern):
	dirList = os.listdir(directory)
	filenames = []
	for fname in dirList:
		if re.search(matchPattern, fname):
			filenames.append(fname)
	return filenames

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

#splits Reuters train or test file into individual docs, 
#both tagged and plain text
def splitDocsToFiles(filepath, filename):
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
				fileTagged = filepath + "/files/" + filename + "00" + str(count) + "tagged.txt"
			elif count < 100:   
				fileTagged = filepath + "/files/" + filename + "0" + str(count) + "tagged.txt"      		
			else:
				fileTagged = filepath + "/files/" + filename + str(count) + "tagged.txt"
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

#create plaintext versions of reuters tagged docs
def createPlainFiles(filepath, filename):
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
				fileParsed = filepath + "/files/" + filename + "00" + str(count) + "parsed.txt"
			elif count < 100:   
				fileParsed = filepath + "/files/" + filename + "0" + str(count) + "parsed.txt"      		
			else:
				fileParsed = filepath + "/files/" + filename + str(count) + "parsed.txt"
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

#######################################################################

path = os.path.dirname(os.path.abspath(__file__))

#break up test and train files and create plaintext versions
if os.path.isdir("./files/"):
	shutil.rmtree("./files/")
os.makedirs(path + "/files")
splitDocsToFiles(path, "eng.testb")
createPlainFiles(path, "eng.testb")
splitDocsToFiles(path, "eng.train")
createPlainFiles(path, "eng.train")

#read in text
files = getFileNames("./files", "parsed")
documents = [open("./files/" + f).read() for f in files]

#create vectors and cluster docs
numClusters = 4
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(documents)
k_means = cluster.KMeans(n_clusters=numClusters)
k_means.fit(vectors)

#match up cluster assignment with file name
clusters = [(files[i], k_means.labels_[i]) for i in range(len(files))]

#create training and test files for each cluster
for i in range(numClusters):
	test = open("clustertest" + str(i), 'wb')
	train = open("clustertrain" + str(i), 'wb')
	for (fileName, cluster) in clusters:
		if cluster == i:
			g = open("./files/" + fileName[:12] + "tagged.txt", 'r')
			lines = g.readlines()		
			if re.search("test", fileName):
				test.write("O\t0\t0\tO\t-X-\t-DOCSTART-\tx\tx\tO\n")
				for line in lines:
					test.write(line)
			else:
				train.write("O\t0\t0\tO\t-X-\t-DOCSTART-\tx\tx\tO\n")
				for line in lines:
					train.write(line)
			g.close()			
	test.close()
	train.close()
