# Loop all the wav file and get the emma file from Mashup.
# Audio file in a folder called "audio" in the same directory of this file.
# Emma output file in a folder called "emma" in the same directory of this file.

import subprocess
import os

def getName(file):
	deciminPosition = file.rfind('.')
	fileName = file[:deciminPosition]
	return fileName


for file in os.listdir("audio"):
	if file.endswith(".wav"):
		fileName = getName(file)
		subprocess.call(["sh", "call_reco.sh", "audio/"+file, "emma/"+fileName+".emma"])

