# This is a script to generate the recognition dictionry quickly form the jsgf grammar file.
# To use this script in the termianl $ python createDic,py <fileName>;

def cleanWord(word):
	if "(" in word:
		word = word.replace("(" , "")
	if ")" in word:
		word = word.replace(")" , "")
	if "*" in word:
		word = word.replace("*" , "")
	if "[" in word:
		word = word.replace("[" , "")
	if "]" in word:
		word = word.replace("]" , "")
	if "|" in word:
		word = word.replace("|" , "")
	if ";" in word:
		word = word.replace(";" , "")
	if "#" in word:
		word = word.replace("#", "")
	return word

def createDic(file):
	dic = open("dictList.txt","a")
	for line in file:
		for word in line.split():
			if (not "<" in word and not "=" in word):
				newWord = cleanWord(word)
				if newWord:
					dic.write(newWord+"\n")
	dic.close()

if __name__ == "__main__":
	import sys
	f = open(sys.argv[1],"r")
	try:
		createDic(f)
	except:
		print "Please supply a file name."