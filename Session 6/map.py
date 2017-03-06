from player import Player
from box import Box
from gate import Gate

class Map:
    def __init__(self,width,height):
        self.player = Player(0,0)
        self.box = Box(1,1)
        self.gate = Gate(2,2)
        self.width = width
        self.height = height

    def print(self):
        for y in range (self.width):
            for x in range (self.width):
                if self.player.match(x,y):
                    print(self.player.text, end="")
                elif self.box.match(x,y):
                    print(self.box.text, end="")
                elif self.gate.match(x,y):
                    print(self.gate.text, end ="")
                else:
                    print("- ", end="")
            print()

    def move_player(self,dx,dy):
        self.player.move(dx,dy)

    def move_box(self,dx,dy):
        self.box.move(dx,dy)

    def check_win(self,x,y):
        return self.gate.match(x,y)

    def process_input(self,move):
        direction = move.upper()
        dx,dy = 0,0
        if direction == 'W':
            dy = -1
        if direction == 'S':
            dy = 1
        if direction == 'A':
            dx = -1
        if direction == 'D':
            dx = 1

        self.move_player(dx,dy)
        if self.player.in_map(self.width,self.height) == False:
            self.move_player(-dx, -dy)
        else:
            if self.box.match(self.player.x,self.player.y) == True:
                 self.move_box(dx, dy)
                 if self.box.in_map(self.width, self.height) == False:
                    self.move_box(-dx, -dy)
                    self.move_player(-dx, -dy)


    def loop(self):
        while True:
            self.print()
            move = input(" Your move (W,A,S,D)? ")
            self.process_input(move)
            if self.check_win(self.box.x,self.box.y) == True:
                self.print()
                print('YOU WIN !!!')
                break;