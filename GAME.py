import numpy as np
import pygame
import sys
import math
from BOARD import *

board = BOARD.create_board()
BOARD.print_board(board)
game_over = False
turn = 0
pygame.init()
BOARD.draw_board(board)
pygame.display.update()


while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, CHOCOLATE, (0,0, width, SQUARESIZE))
			posx = event.pos[0]
			if turn == 0:
				pygame.draw.circle(screen, MINT, (posx, int(SQUARESIZE/2)), RADIUS)
			else: 
				pygame.draw.circle(screen, ORANGE, (posx, int(SQUARESIZE/2)), RADIUS)
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, CHOCOLATE, (0,0, width, SQUARESIZE))

			if turn == 0:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if BOARD.is_valid_location(board, col):
					row = BOARD.get_next_open_row(board, col)
					BOARD.drop_piece(board, row, col, 1)

					if BOARD.winning_move(board, 1):
						label = myfont.render("Player 1 wins!!", 1, MINT)
						screen.blit(label, (40,10))
						game_over = True



			else:				
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if BOARD.is_valid_location(board, col):
					row = BOARD.get_next_open_row(board, col)
					BOARD.drop_piece(board, row, col, 2)

					if BOARD.winning_move(board, 2):
						label = myfont.render("Player 2 wins!!", 1, ORANGE)
						screen.blit(label, (40,10))
						game_over = True

			BOARD.print_board(board)
			BOARD.draw_board(board)

			turn += 1
			turn = turn % 2

			if game_over:
				pygame.time.wait(3000)