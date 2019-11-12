# User implemented imports
from point import cPoint as pnt

# API implemented imports
import pygame

class cGraphics:
	def __init__(self, screen = pnt(896, 240)):
		""" cGraphics(self, screen = pnt(1024, 768)):\n
			- Creates a screen surface with PyGame """

		self.screen = pygame.display.set_mode((screen.x, screen.y))

	def getScreen(self):
		return self.screen

	def draw(self, obj, thickness = 0):
		""" draw(self, obj, thickness = 0):\n
			- Draws a primitive shape (filling by default) """
		return pygame.draw.rect(self.screen, obj.color, ((obj.pos.x + obj.size.x1), (obj.pos.y + obj.size.y1), obj.size.x2, obj.size.y2), thickness)
