class Box:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.text = 'B '

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def match(self,x,y):
        return self.x == x and self.y == y

    def in_map(self,width,height):
        return self.x >= 0 and self.x < width and self.y >= 0 and self.y < height