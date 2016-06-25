from PIL import Image
import os, drawText

class EveryPicture:

	def __init__(self):


	def rotateAllPictures(self, directory, angle):
		for infile in os.listdir(directory):
			try:
				im = Image.open(infile)
				im.rotate(angle).save(infile)
			except IOError:
				pass
