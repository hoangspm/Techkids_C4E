def write_game(px,py,bx,by,h,w):
    for y in range(h):
        for x in range(w):
            if x == px and y == py:
                print("P", end="")
            elif x == bx and y == by:
                print("B", end="")
            elif x == hx and y == hy:
                print("*", end="")
            else:
                print("-", end="")
        print()

def object_move(move,x,y):
    if move == 'W':
        return [x,y-1]
    elif move == 'S':
        return [x,y+1]
    elif move == 'A':
        return [x-1,y]
    elif move == 'D':
        return [x+1,y]

def check_move(move,x,y):
    if move == 'W' and y==0:
        return (False)
    elif (move == 'S' and y==sizeh-1):
        return (False)
    elif (move == 'A' and x==0):
        return (False)
    elif (move == 'D' and x==sizew-1):
        return (False)
    return (True)

sizeh = 4
sizew = 4
px = 1
py = 3
bx = 2
by = 2
hx = 0
hy = 3
n = 1

while True:

    while True:
        write_game(px,py,bx,by,sizeh,sizew)
        move = input("Your move? ").upper()
        if move in ['W','S','A','D']:
            break

    [next_x,next_y] = object_move(move,px,py)
    if check_move(move,px,py) == True:
        if next_x == bx and next_y == by:
            if check_move(move,next_x,next_y) == True:
                [px,py] = [next_x,next_y]
                [bx,by] = object_move(move,next_x,next_y)
            else:
                print("Can't Move !!! Go Away !!!")
        else:
            [px, py] = [next_x, next_y]
    else:
         print("Can't Move !!! Go Away !!!")

    if bx == hx and by == hy:
        write_game(px, py, bx, by, sizeh, sizew)
        print("YOU WIN")
        break
