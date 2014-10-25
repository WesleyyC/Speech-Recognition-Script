# Get a list of name of all the wav file in the current dirctory

import os

def getName(file):
	deciminPosition = file.find('.')
	fileName = file[:deciminPosition]
	return fileName

if __name__ == "__main__":
	fieldDoc = open("pizza.field", "a")
	for file in os.listdir(os.getcwd()):
		if file.endswith(".wav"):
			fileName = getName(file)
			fieldDoc.write(fileName + "\n")
	fieldDoc.close()