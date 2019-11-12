# Python library imports
import os
import random
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# User implemented imports
from point import cPoint as pnt
from rect import cRect as rct

from ball import cBall as ball
from paddle import cPaddle as paddle
from board import cBoard as board
from graphics import cGraphics as gfx

from game import cGame as game
from controller import cController

# API implemented imports
import pygame

pygame.init()

if __name__ == '__main__':
	pongGame = game()

	screen = gfx()

	balls = []
	balls.append(ball(pnt(5, 5), rct(pnt(0, 0), pnt(20, 20))))
	balls.append(ball(pnt(5, 5), rct(pnt(0, 0), pnt(20, 20))))
	balls.append(ball(pnt(5, 5), rct(pnt(0, 0), pnt(20, 20))))
	balls.append(ball(pnt(5, 5), rct(pnt(0, 0), pnt(20, 20))))

	pongGame.addUnit(balls)

	boards = []
	boards.append(board(pnt(0, 0), rct(pnt(0, 0), pnt(200, 200))))
	boards.append(board(pnt(210, 0), rct(pnt(0, 0), pnt(200, 200))))
	boards.append(board(pnt(420, 0), rct(pnt(0, 0), pnt(200, 200))))
	boards.append(board(pnt(640, 0), rct(pnt(0, 0), pnt(200, 200))))
	
	pongGame.addUnit(boards)

	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		for y in range(len(balls)):
			balls[y].pos.y = random.randint(0, 500)
			balls[y].pos.x = random.randint(0, 750)

			for x in range(len(boards)):
				boards[x].transformUnitPos(balls[x])
				boards[x].transformUnitPos(balls[x])
				boards[x].transformUnitPos(balls[x])
				boards[x].transformUnitPos(balls[x])

			balls[0].color = (random.randint(0, 255), random.randint(0, 50), random.randint(0, 25))
			balls[1].color = (random.randint(0, 148), random.randint(0, 180), random.randint(0, 75))
			balls[2].color = (random.randint(0, 25), random.randint(0, 25), random.randint(0, 255))
			balls[3].color = (random.randint(0, 55), random.randint(0, 255), random.randint(0, 25))
			#u1 = screen.draw(balls[y])
			#u2 = screen.draw(boards[0], 1)
			#u3 = screen.draw(boards[1], 1)
			#u4 = screen.draw(boards[2], 1)
			#u5 = screen.draw(boards[3], 1)
			#pygame.display.update((u1, u2, u3, u4, u5))
			pongGame.updateScreen()

