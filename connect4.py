import numpy as np
import pygame
import sys
import math

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 7
COLUMN_COUNT = 7

def create_board():
    board = np.zeros(( COLUMN_COUNT, ROW_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r




def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horixontal locations for win

    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # check for vertical locations for win 
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True


   # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+1] == piece and board[r+3][c+1] == piece:
                return True

   # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+1] == piece and board[r-3][c+1] == piece:
                return True



def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQAURESIZE, r*SQAURESIZE+SQAURESIZE, SQAURESIZE, SQAURESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQAURESIZE+SQAURESIZE/2), int(r*SQAURESIZE+SQAURESIZE+SQAURESIZE/2)), RADIus )


    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQAURESIZE+SQAURESIZE/2), height-int(r*SQAURESIZE+SQAURESIZE/2)), RADIus )

            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQAURESIZE+SQAURESIZE/2), height-int(r*SQAURESIZE+SQAURESIZE/2)), RADIus )
    pygame.display.update()  

            



board = create_board()
print_board(board)
game_over = False
turn = 0


pygame.init()

SQAURESIZE = 100

width = COLUMN_COUNT * SQAURESIZE
height = (ROW_COUNT + 1)  * SQAURESIZE

RADIus = int(SQAURESIZE/2 - 5)

size = (width, height)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQAURESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQAURESIZE/2)), RADIus)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQAURESIZE/2)), RADIus)
        
        pygame.display.update()


        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQAURESIZE))
            # Ask player one for input
            if turn == 0:
                posx = event.pos[0]
                col= int(math.floor(posx/SQAURESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True
            #             break

                

            
            # # Ask Player two for input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQAURESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40,10))
                        game_over = True
            #             break




            print_board(board)
            draw_board(board)
            turn +=1
            turn = turn % 2
            if game_over:
                pygame.time.wait(3000)
