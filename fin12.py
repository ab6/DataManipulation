name = raw_input("Input file:")
copy = name
oDoc = open (name)
count = 0
newFileKey = "-DOCSTART-"
newFile = ""
for eachLine in oDoc:
    if newFileKey in eachLine:
        if newFile: newFile.close()
        count = count + 1
        fileName = name + str(count) + ".txt"
        newFile = open(fileName, 'w')
    else:
        newFile.write(eachLine)
newFile.close()
oDoc.close()

i = 1
while i <= count:

    string = copy + str(i) + '.txt'
    toParseDoc = open (string)
    numb = len(string)
    name = string[:numb - 4]
    parsedDoc = open (name + 'parsed' + '.txt', 'w')
    string = ""
    for eachLine in toParseDoc:
        if eachLine.strip():
            cut = eachLine.find(' ')
            word = eachLine[:cut]
            if not word == '.':
                string = string + word + " "
            else:
                string = string + word
        else:
            parsedDoc.write(string)
            string = ""
            parsedDoc.write('\n')
    
    i += 1        
    parsedDoc.close()
    toParseDoc.close()
print "File complete."
