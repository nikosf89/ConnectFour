import pygame
import numpy as np
from sys import exit

pygame.init()

WIDTH = 700
HEIGHT = 600
BOARD = np.full((6, 7), -1, dtype=np.int8)
GAME_OVER = False
TOTAL_MOVES = 0


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CONNECT FOUR")

def draw_text(text, x, y, font_size, color):
    my_font = pygame.font.SysFont("Arial", font_size, bold=True)
    my_font_surf = my_font.render(text, True, color)
    my_font_rect = my_font_surf.get_rect(center = (x, y))
    screen.blit(my_font_surf, my_font_rect)
    return my_font_rect


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
    x_pos = int(x /100)
    y_pos = int(y / 100)
    if y_pos == 5 and BOARD[y_pos, x_pos] == -1:
        return True
    elif BOARD[y_pos, x_pos] == -1 and BOARD[y_pos+1, x_pos] != -1:
        return True
    else:
        return False

def check_winner():
    global GAME_OVER
    #Check vertically
    for i in range(7):
        for j in range(1,4):
            if np.array_equal(BOARD[:, i][3-j: 7-j],np.full((4,), 0)):
                GAME_OVER = True
                return 0
            elif np.array_equal(BOARD[:, i][3-j: 7-j],np.full((4,), 1)):
                GAME_OVER = True
                return 1
    
    #Check horizontally
    for i in range(6):
        for j in range(1, 5):
            if np.array_equal(BOARD[i, 4-j:8-j], np.full((4,),0)):
                GAME_OVER = True
                return 0
            elif np.array_equal(BOARD[i, 4-j:8-j], np.full((4,),1)):
                 GAME_OVER = True
                 return 1

    #Check diagonally

    #Check draw
    if TOTAL_MOVES == 42:
        GAME_OVER = True
        return 2


def start_menu():
    screen.fill("magenta")
    against_player_rect = draw_text("AGAINST PLAYER", WIDTH/2, 200, 40, "white")
    against_cpu_rect = draw_text("AGAINST CPU", WIDTH/2, 300, 40, "white")
    exit_rect = draw_text("EXIT", WIDTH/2, 400, 40, "white")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if against_player_rect.collidepoint(event.pos):
                    against_player()
                elif against_cpu_rect.collidepoint(event.pos):
                    against_cpu()
                elif exit_rect.collidepoint(event.pos):
                    exit()
          
        pygame.display.update()
           
def against_player():
    global TOTAL_MOVES
    global GAME_OVER
    global BOARD
    TOTAL_MOVES = 0
    GAME_OVER = False
    BOARD = np.full((6, 7), -1, dtype=np.int8)
    player = 0
    draw_board()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not GAME_OVER:
                x = event.pos[0]
                y = event.pos[1]
                if is_valid_location(x, y):
                    make_move(player, x, y)
                    TOTAL_MOVES += 1
                    player = (player + 1) % 2
            if event.type == pygame.KEYDOWN and GAME_OVER:
                if event.key == pygame.K_SPACE:
                    start_menu()
  
        res = check_winner()
        if res == 0:
            draw_text("RED PLAYER WINS!", WIDTH/2, HEIGHT/2, 40, "white")
            draw_text("PRESS SPACE FOR MAIN MENU", WIDTH/2, HEIGHT/2 + 40, 40, "white")
        elif res == 1:
            draw_text("YELLOW PLAYER WINS!", WIDTH/2, HEIGHT/2, 40, "white")
            draw_text("PRESS SPACE FOR MAIN MENU", WIDTH/2, HEIGHT/2 + 40, 40, "white")
        elif res == 2:
            draw_text("IT'S A DRAW!", WIDTH/2, HEIGHT/2, 40, "white")
            draw_text("PRESS SPACE FOR MAIN MENU", WIDTH/2, HEIGHT/2 + 40, 40, "white")
        pygame.display.update()


def against_cpu():
    pass


if __name__ == '__main__':
    start_menu()