import pygame
from player import Player
from box import Box
from gate import Gate

class Map:
    def __init__(self,width,height):
        self.player = Player(0,0)
        self.box = Box(1,1)
        self.gate = Gate(9,9)
        self.width = width
        self.height = height

    def in_map(self,x,y):
        return 0 <= x < self.width and 0 <= y < self.height

    def move_player(self,dx,dy):
        [next_px,next_py] = self.player.calc_next(dx,dy)
        if self.in_map(next_px,next_py):
            if self.box.match(next_px,next_py):
                [next_bx, next_by] = self.box.calc_next(dx, dy)
                if self.in_map(next_bx, next_by):
                    self.box.move(dx, dy)
                    self.player.move(dx,dy)
            else:
                self.player.move(dx,dy)

    def check_win(self):
        return self.gate.match(self.box.x,self.box.y)

    def process_input(self,move):
        dx,dy = 0,0
        if move == pygame.K_UP:
            dy = -1
        if move == pygame.K_DOWN:
            dy = 1
        if move == pygame.K_LEFT:
            dx = -1
        if move == pygame.K_RIGHT:
            dx = 1

        self.move_player(dx,dy)