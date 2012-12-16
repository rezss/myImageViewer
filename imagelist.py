import os
import glob
from pyglet.image import load
import copy

class ImageList:
	"""Doctstring for imageList"""
	imageList_, thumbList_ = list(), list()
	path_ = "./bin/data"
	ext_ = "*.png"

	def __init__(self):
		self.loadImages()
		# self.resizeAll(480)

	def loadImages(self):
		for infile in glob.glob(os.path.join(self.path_, self.ext_)):
			# print ("current file is " + infile)
			image = load(infile)
			thumb = copy.deepcopy(image)

			self.centerImage(image)
			self.centerImage(thumb)

			self.imageList_.append(image)
			self.thumbList_.append(thumb)

	def centerImage(self, newImage):
		newImage.anchor_x = newImage.width // 2
		newImage.anchor_y = newImage.height // 2

	def centerImageAll(self):
		for image in self.imageList_:
			image.anchor_x = image.width // 2
			image.anchor_y = image.height // 2

	def resizeAll(self, newScale):
		if (newScale > 0):
			for image in self.imageList_:
				if (image.width > newScale):
					tmp_width = image.width
					image.width = newScale
					if (image.height > newScale):
						image.height = newScale // image.height \
							* tmp_width
						# print (image.height)
						# image.scale = newScale / float(image.height)
				elif (image.height > newScale):
					tmp_height = image.height
					image.height = newScale
					if (image.width > newScale):
						image.width = newScale // image.width \
							* tmp_height

	def getImageList(self):
		return self.imageList_

	def getThumbList(self):
		return self.thumbList_