# User implemented imports
from gameObject import cGameObject as go
from point import cPoint as pnt

# API implemented imports
import random

class cBoard(go):
	pass

	def transformUnitPos(self, unit):
		""" transformUnitPos(self, unit):\n
			- Transforms the unit position to be relative to the board """

		# Out of bounds check: X plane
		if ((unit.pos.x + unit.getWidth()) >= self.getWidth()):
			minValue = 0
			maxValue = self.getWidth() - unit.getWidth()

			newPos = random.randint(minValue, maxValue)
			unit.pos.x = newPos

		# Out of bounds check: Y plane
		if ((unit.pos.y + unit.getHeight()) >= self.getHeight()):
			minValue = 0
			maxValue = self.getHeight() - unit.getHeight()

			newPos = random.randint(minValue, maxValue)
			unit.pos.y = newPos

		unit.pos += self.pos
