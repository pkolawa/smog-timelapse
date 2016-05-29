from PIL import Image
import sys
import os

class EveryPicture:

	def __init__(self):


	def makePictures(self):
		for infile in os.listdir(str(sys.argv[1])):
			try:
				im = Image.open(infile)
				im.rotate(180).save(infile)
			except IOError:
				pass
