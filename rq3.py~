
name = 'eng.testb1tagged'
oDoc = open (name)
nDoc = open ('aaa' + name + '.txt', 'w')
string = ""
remString = ""
count = 0
for eachLine in oDoc:
    if eachLine.strip():
        cut = eachLine.find(' ')
        word = eachLine[:cut]
        remString = eachLine[cut + 1:]
        cut = remString.find(' ')
        spot2 = remString[:cut]
        remString = remString[cut + 1:]
        cut = remString.find(' ')
        spot3 = remString[:cut]
        remString = remString[cut + 1:]
        cut = remString.find(' ')
        spot4 = remString[:cut]

        string = (spot4 +'\t' + '0\t' + str(count)+ '\t' + spot3 +'\t' + spot2 + '\t' + word + '\tx\t' + 'x\t' + 'x\n')
        nDoc.write(string)
        string = ""
        count += 1
    else:
        nDoc.write("\n")
        count = 0
nDoc.close()
oDoc.close()
