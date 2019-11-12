# User implemented imports
from point import cPoint as pnt
from rect import cRect as rct

from ball import cBall as ball
from paddle import cPaddle as paddle
from board import cBoard as board
from graphics import cGraphics as gfx

# API implemented imports
import pygame

class cGame:
	def __init__(self):
		self.screen = gfx()
		self.unitList = []

	def addUnit(self, units = []):
		for x in units:
			self.unitList.append(x)

		for unit in units:
			buffer = "{0}: ({1}, {2})"
			print(buffer.format(type(unit).__name__, unit.pos.x, unit.pos.y))

	def updateScreen(self):
		for gameObj in self.unitList:
			if type(gameObj).__name__ == 'cBoard':
				self.screen.draw(gameObj, 1)
			else:
				self.screen.draw(gameObj)

		updateBuffer = []

		for x in self.unitList:
			updateBuffer.append(x.getRectRelativeArea())
			print(x.getRectRelativeArea())

		pygame.display.update(updateBuffer)
