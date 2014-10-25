def cleanID(file):
	cleanV = open("newVersion.match", "a")
	for line in file:
		if "-" in line:
			end = line.rfind("-") - 1
			cleanV.write(line[:end]+")\n")
	cleanV.close()

if __name__ == "__main__":
	import sys
	f = open(sys.argv[1],"r")
	try:
		cleanID(f)
	except:
		print "Please supply a file name."