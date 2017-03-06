class Gate:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.text = '* '

    def match(self,x,y):
        return self.x == x and self.y == y