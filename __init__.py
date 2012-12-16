import pyglet

from imagelist import ImageList
from spritelist import SpriteList

class MainWindow(pyglet.window.Window):
	"""docstring for MainWindow"""
	thumbList_ = None

	firstViewImage_, currentImage_, imageCount_ = 0, 0, 0
	thumbSelectorPos_, thumbSize_, imageSize_ = 0, 100, 480

	drawFullImageB = False

	def __init__(self, newWidth = 640, newHeight = 480):
		super(MainWindow, self).__init__(width = newWidth, 
			height = newHeight)

		pyglet.gl.glClearColor(0.625, 0.625, 0.625, 1)

		self.width_, self.height_ = newWidth, newHeight

		self.imageList_ = ImageList().getImageList()
		self.thumbList_ = ImageList().getThumbList()
		

		self.initMainScene()
		self.initThumbnails()

	def initThumbnails(self):
		self.thumbList_ = SpriteList(self.thumbList_, False)
		self.thumbSpriteList_ = self.thumbList_.getThumbList()
		self.thumbList_.resize(self.thumbSpriteList_, 100)
		self.imageCount_ = len(self.thumbSpriteList_) // 2
		print(self.thumbSpriteList_)

		x, y = 100, 70

		for thumb in self.thumbSpriteList_:
			thumb.set_position(x, y)
			x = (x + 150) % 750

	def drawThumbnails(self):
		posX = 100
		for n in range(self.firstViewImage_, self.firstViewImage_ + 5):
			self.thumbSpriteList_[n % self.imageCount_].x = posX
			self.thumbSpriteList_[n % self.imageCount_].draw()
			posX = (posX + 150) % 750


	def drawThumbnailSelector(self, thumbNumber):
		xLeft, xRight = 40, 160
		if (thumbNumber == 1):
			xLeft, xRight = 190, 310
		elif (thumbNumber == 2):
			xLeft, xRight = 340, 460
		elif (thumbNumber == 3):
			xLeft, xRight = 490, 610
		elif (thumbNumber == 4):
			xLeft, xRight = 640, 760
		
		pyglet.gl.glBegin(pyglet.gl.GL_TRIANGLES)
		pyglet.gl.glVertex2i(xLeft, 120) # TOP
		pyglet.gl.glVertex2i(xLeft, 20) # BOTTOM LEFT
		pyglet.gl.glVertex2i(xRight, 20) # BOTTOM RIGHT
		pyglet.gl.glVertex2i(xRight, 120) # TOP
		pyglet.gl.glVertex2i(xLeft, 120) # BOTTOM LEFT
		pyglet.gl.glVertex2i(xRight, 20) # BOTTOM RIGHT
		pyglet.gl.glEnd()


	def initMainScene(self):
		self.imageList_ = SpriteList(self.imageList_, True)
		self.imageSpriteList_ = self.imageList_.getImageList()
		self.imageList_.resize(self.imageSpriteList_, 480)

		for image in self.imageSpriteList_:
			image.set_position(self.width_//2, self.height_//2)

	def drawMainScene(self):
		self.imageSpriteList_[self.currentImage_].draw()

	def setCurrentImage(self, newCurrentImg):
		if (newCurrentImg < 0):
			self.currentImage_ = newCurrentImg + self.imageCount_
		elif (newCurrentImg > self.imageCount_):
			self.currentImage_ = newCurrentImg % self.imageCount_
		else:
			self.currentImage_ = newCurrentImg

	def selectImage(self, changeTo):
		if (changeTo == 1):
			self.setCurrentImage(self.currentImage_ + 1)
			if (self.thumbSelectorPos_ == 4):
				self.setFirstViewImage(self.currentImage_)
			self.setThumbSelectorPos(self.thumbSelectorPos_ + 1)
			return self.thumbSelectorPos_
		elif (changeTo == -1):
			self.setCurrentImage(self.currentImage_ - 1)
			if (self.thumbSelectorPos_ == 0):
				self.setFirstViewImage(self.currentImage_ - 4)
				self.setThumbSelectorPos(4)
				return self.thumbSelectorPos_
			self.setThumbSelectorPos(self.thumbSelectorPos_ - 1)
			return self.thumbSelectorPos_
		elif (changeTo == 0):
			self.drawFullImageB = True


	def setFirstViewImage(self, changeTo):
		if (changeTo < 0):
			self.firstViewImage_ = changeTo + self.imageCount_
		elif (changeTo > self.imageCount_):
			self.firstViewImage_ = changeTo % self.imageCount_
		else:
			self.firstViewImage_ = changeTo

	def setThumbSelectorPos(self, changeTo):
		if (changeTo > 4):
			self.thumbSelectorPos_ = changeTo % 5
		elif (changeTo < 0):
			self.thumbSelectorPos_ = changeTo + 4
		else:
			self.thumbSelectorPos_ = changeTo

	def centerThumbnails(self):
		self.setFirstViewImage(self.currentImage_ - 2)
		self.setThumbSelectorPos(2)

	def on_draw(self):
		self.clear()
		if (not self.drawFullImageB):
			self.drawThumbnailSelector(self.thumbSelectorPos_)
			self.drawThumbnails()
		else:
			self.drawMainScene()

	def on_key_press(self, symbol, key):
		if (symbol == pyglet.window.key.LEFT):
			self.setThumbSelectorPos(self.selectImage(-1))
		elif (symbol == pyglet.window.key.RIGHT):
			self.setThumbSelectorPos(self.selectImage(1))
		elif (symbol == pyglet.window.key.ENTER):
			if (self.drawFullImageB):
				print (self.drawFullImageB)
				self.drawFullImageB = not self.drawFullImageB
				self.centerThumbnails()
			else:
				self.selectImage(0)
		elif (symbol == pyglet.window.key.SPACE):
			pass
		elif (symbol == pyglet.window.key.ESCAPE):
			pyglet.app.exit()

	def on_mouse_press(self, x, y, button, modifiers):
		if (button == pyglet.window.mouse.LEFT):
			pass

def main():
	MainWindow(800, 600)

	pyglet.app.run()

if __name__ == "__main__":
	main()

