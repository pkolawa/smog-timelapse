from PIL import Image
import sys
import os

for infile in os.listdir(str(sys.argv[1])):
	try:
		im = Image.open(infile)
		im.rotate(180).save(infile)
	except IOError:
		pass
