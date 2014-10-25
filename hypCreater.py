# Read all the .emma file and come up with the .hyp file.

import os

def getName(file):
	deciminPosition = file.find('.')
	fileName = file[:deciminPosition]
	return fileName

def getLiteral(file):
	f = open("emma/"+file,"r")
	for line in f:
		if "<emma:literal>" in line:
			start = line.find("<emma:literal>") + 14
			end = line.find("</emma:literal>")
			return line[start:end]
	return "no emma"

def readAndWrite(file):
	fileName = getName(file)
	emmaLiteral = getLiteral(file)
	f = open("result.ref", "a")
	f.write(emmaLiteral + " (" + fileName + ")\n")
	f.close()
	print(emmaLiteral + " (" + fileName + ")")

for file in os.listdir("emma"):
	if file.endswith(".emma"):
		readAndWrite(file)



	