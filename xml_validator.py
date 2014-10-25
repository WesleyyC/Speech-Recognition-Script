import xml.etree.ElementTree as ET

def validate(xmlfile):
	try:
		root = ET.parse(xmlfile)
		print "Good to go!"
	except Exception as e:
		print e.msg
		
if __name__ == "__main__":
	import sys
	try:
		validate(sys.argv[1])
	except:
		print "Please supply a file name."
