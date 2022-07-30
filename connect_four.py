from pip import main
import pygame
import numpy as np
from sys import exit

pygame.init()

WIDTH = 700
HEIGHT = 600
BOARD = np.zeros(shape=(6,7), dtype=np.int8)
print(BOARD)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CONNECT FOUR")

def draw_board():
    screen.fill("blue")
    for i in range(7):
        for j in range(6):
            pygame.draw.circle(screen, "black", ((2*i+1)*50, (2*j+1)*50), 45)

           
def main_game():
    draw_board()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        pygame.display.update()


if __name__ == '__main__':
    main_game()

