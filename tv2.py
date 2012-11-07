import re
   
def calc_tv(text):
	tv = dict()
	results = re.split('\W+',text)
	for result in results:
		lresult = result.lower()
		if not lresult.isdigit():
			if lresult in tv:
				tv[lresult] = tv[lresult] + 1	
			else:
				tv[lresult] = 1
	return tv
      

name = raw_input("Input file:")
oDoc = open(name)
string = ''
for line in oDoc:
        string = line + string
data = dict()
data = calc_tv(string)

print data        
oDoc.close()



