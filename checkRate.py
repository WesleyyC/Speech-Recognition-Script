# Check the rate of audio in a folder
# The folderDirectory can be changed
# Need to install sox first

import subprocess
import os

folderDirectory = "Audio"

for file in os.listdir("folderName"):
	if file.endswith(".wav"):
		subprocess.call(["sox", "--i", folderName+"/"+file])