# Change the rate of all the audio files in a folder called audio and ouput it to a folder called Audio Modified
# Can also change the input and outpu directory for future use.
# Need to install sox first

import subprocess
import os

inputDirectory = "Audio"
ouputDirectory = "Audio Modified"

def getName(file):
	deciminPosition = file.find('.')
	fileName = file[:deciminPosition]
	return fileName

for file in os.listdir(inputDirectory):
	if file.endswith(".wav"):
		fileName = getName(file)
		subprocess.call(["sox", inputDirectory+"/"+file, "-r", "8000", ouputDirectory+"/"+file])
