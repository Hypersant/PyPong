# User implemented imports
from point import cPoint as pnt
from rect import cRect as rct

# API implemented imports

class cGameObject:
	def __init__(self, pos = pnt(0, 0), size = rct(pnt(0, 0), pnt(0, 0)), color = (0, 255, 0)):
		""" cGameObject(self, pos = pnt(0, 0), size = rct(pnt(0, 0), pnt(0, 0)), color = (0, 255, 0)):\n
			- cGameObject represents a single game entity (pos, size and color) """

		self.pos = pos
		self.size = size
		self.color = color

	def getWidth(self):
		return self.size.x2

	def getHeight(self):
		return self.size.y2

	def getRectRelativeArea(self):
		return ((self.size.x1 + self.pos.x), (self.size.y1 + self.pos.y), self.size.x2, self.size.y2)

	def getRectAbsoluteArea(self):
		return (self.size.x1, self.size.y1, self.size.x2, self.size.y2)

#	def outputPos(self):
#		print("cUnit __init__ (pos):", self.pos.x, self.pos.y)

#	def outputSize(self):
#		print("cUnit __init__ (size):", self.size.x1, self.size.y1, self.size.x2, self.size.y2)

#	def outputColor(self):
#		print("cUnit __init__ (color):", self.color)
