#TTT_interface.py - Handles All Interface Calls For Tic Tac Toe
#Ari Cohen

import pygame, sys
from pygame.locals import *
from buttons import *

pygame.init()
MAIN_SURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tic Tac Toe!')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 100, 0)
BLUE = (0, 0, 128)
YELLOW = (255, 255, 0)
LIGHT_YELLOW = (100, 100, 0)
RED = (255, 0, 0)
LIGHT_RED = (100, 0, 0)
GRAY = (150, 150, 150)

class Piece():
    X = 3
    O = 4

class Board():

    def __init__(self, position, board_width, square_width):
        self.position = position
        self.total_squares = board_width * board_width
        self.board_width = board_width
        self.square_width = square_width
        self.squares = []
        for square_num in range(self.total_squares):
            new_square = Square(square_num, self)
            self.squares.append(new_square)
        width = (board_width * square_width) + (5 * (board_width - 1))
        self.surface = pygame.Surface((width, width))
        self.board_rect = pygame.Rect(position[0], position[1], width, width)

    def set_square(self, row, col, piece):
        self.squares[(self.board_width * row) + col].click_action(piece)

    def get_square_coords(self, row, col):
        (x, y) = self.squares[(self.board_width * row) + col].get_location()
        x += self.position[0]
        y += self.position[1]
        return (x,y)

    def update_board_surface(self):
        self.surface.fill(BLACK)
        for square in self.squares:
            square_surf = square.get_square_surface()
            self.surface.blit(square_surf, square.position)
        return self.surface

    def draw_board(self):
        board_surf = self.update_board_surface()
        MAIN_SURF.blit(board_surf, self.position)

    def check_for_mouse(self, dragging_piece):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.board_rect.collidepoint([mouse_x, mouse_y]):
            mouse_x -= self.position[0]
            mouse_y -= self.position[1]
            col = mouse_x / (self.square_width + 5)
            row = mouse_y / (self.square_width + 5)
            bad_drag = self.squares[(self.board_width * row) + col].click_action(dragging_piece)
            if(bad_drag):
                return [False, [col, row]]
            else:
                return [True, [col, row]]
        else:
            return [False, 0]
    
class Square():

    EMPTY = 0

    def __init__(self, square_number, board):
        self.square_num = square_number
        self.board = board
        self.width = self.board.square_width
        row = self.square_num / self.board.board_width
        col = self.square_num % self.board.board_width
        self.position = ((self.width + 5) * col, (self.width + 5) * row)
        self.surface = pygame.Surface((self.width, self.width))
        self.surface.fill(WHITE) #Square colors
        self.piece = Square.EMPTY

    def get_val(self):
        pass

    def set_val(self):
        pass

    def get_location(self):
        return self.position

    def get_square_surface(self):
        return self.surface

    def click_action(self, piece_num):
        if(self.piece == Square.EMPTY):
            raw_piece = pygame.image.load("Quarto_Pieces/Shadowed/Piece_"+str(piece_num)+".png") #for 3d use jpg
            self.piece = pygame.transform.scale(raw_piece, (self.width, self.width))
            self.surface.blit(self.piece, (0, 0))
            return False
        else:
            return True

def signal_end_of_game(game_status, game_state, player_1,
                       player_2, current_player):
    interface_state = game_state.interface_state
    player_1.game_over(game_state)
    player_2.game_over(game_state)
    if game_status == GameStatus.TIE:
        game_text = "It's a tie."
    elif game_status == GameStatus.WIN:
        game_text = "Player "+current_player.player_num+" wins!"
    else:
        game_text = "Game over - unknown reason"

    my_font = pygame.font.Font('freesansbold.ttf', 52)
    text_surface = my_font.render(game_text, True, BLACK, YELLOW)
    button_surface = my_font.render("Play Again!", True, BLACK, YELLOW)
    button_rect = button_surface.get_rect()
    button_rect.topleft = (300, 520)

    while True:
        events = interface_state.do_event_fetch()
        MAIN_SURF.blit(text_surface, (250, 20))
        MAIN_SURF.blit(button_surface, (300, 520))
        pygame.display.update()
        if (events == MOUSEBUTTONDOWN):
            if (button_rect.collidepoint(pygame.mouse.get_pos())):
                break


board = Board((350, 88), 3, 100)

while True:
    MAIN_SURF.fill(WHITE)
    board.draw_board()
    
    for event in pygame.event.get():
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()
        elif(event.type == KEYDOWN):
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            key_map = pygame.key.get_pressed()
            print key_map
        elif(event.type == MOUSEBUTTONDOWN):
            print MOUSEBUTTONDOWN
        elif(event.type == MOUSEBUTTONUP):
            print MOUSEBUTTONUP

    pygame.display.update()
