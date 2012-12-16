from __future__ import division
import pyglet

class SpriteList():
	"""docstring for SpriteList"""
	spriteImageList_, spriteThumbList_ = list(), list()


	def __init__(self, newImageList, isImage, newX = 640, newY = 480):
		for sprite in newImageList:
			self.x_, self.y_ = newX, newY
			if (isImage):
				self.spriteImageList_.append(pyglet.sprite.Sprite(sprite))
			else:
				self.spriteThumbList_.append(pyglet.sprite.Sprite(sprite))

	def resize(self, spriteList, newScale):
		if (newScale > 0):
			for sprite in spriteList:
				if (sprite.width > newScale):
					sprite.scale = newScale / float(sprite.width)
					if (sprite.height > newScale):
						sprite.scale = newScale / float(sprite.height) \
							* sprite.scale
				elif (sprite.height > newScale):
					sprite.scale = newScale / float(sprite.height)
					if (sprite.width > newScale):
						sprite.scale = newScale / float(sprite.width) \
							* sprite.scale
					

	def getThumbList(self):
		return self.spriteThumbList_

	def getImageList(self):
		return self.spriteImageList_
		