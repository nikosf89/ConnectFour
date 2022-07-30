import pygame
import numpy as np
from sys import exit

pygame.init()

WIDTH = 700
HEIGHT = 600
BOARD = np.full((6, 7), -1, dtype=np.int8)
print(BOARD)
player = 1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CONNECT FOUR")

def draw_board():
    screen.fill("blue")
    for i in range(7):
        for j in range(6):
            pygame.draw.circle(screen, "black", ((2*i+1)*50, (2*j+1)*50), 45)


def make_move(player, x, y):
    x_pos = int(x / 100)
    y_pos = int(y / 100)
    if player == 0:
        pygame.draw.circle(screen, "red", ((2*x_pos+1)*50, (2*y_pos+1)*50), 45)
        BOARD[y_pos, x_pos] = 0
    elif player == 1:
        pygame.draw.circle(screen, "yellow", ((2*x_pos+1)*50, (2*y_pos+1)*50), 45)
        BOARD[y_pos, x_pos] = 1


def is_valid_location(x, y):
    return True
           
def main_game():
    player = 0
    draw_board()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if is_valid_location(x, y):
                    make_move(player, x, y)
                    player = (player + 1) % 2
        
        pygame.display.update()


if __name__ == '__main__':
    main_game()

