from point import cPoint as pnt

class cRect:
	def __init__(self, UpperLeft = pnt(0, 0), LowerRight = pnt(0, 0)):
		self.x1 = UpperLeft.x
		self.y1 = UpperLeft.y
		self.x2 = LowerRight.x
		self.y2 = LowerRight.y
