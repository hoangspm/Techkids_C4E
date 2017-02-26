def write_game(px,py,bx,by,h,w):
    for y in range(h):
        for x in range(w):
            if [x,y] == [px,py]:
                print("P", end="")
            elif [x,y] == [bx,by]:
                print("B", end="")
            elif [x,y] == [hx,hy]:
                print("*", end="")
            elif [x,y] == [wallx,wally]:
                print("#", end="")
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
    return (x >= 0 and x < sizew and y >= 0 and y < sizeh and [x,y] != [wallx,wally])

def end_game(x,y):
    if [x,y] == [hx,hy]:
        return(1)
    if (check_move('W',x,y-1) == False and check_move('A',x-1,y) == False):
        return(2)
    if (check_move('S',x,y+1) == False and check_move('A',x-1,y) == False):
        return(2)
    if (check_move('W',x,y-1) == False and check_move('D',x+1,y) == False):
        return(2)
    if (check_move('S',x,y+1) == False and check_move('D',x+1,y) == False):
        return(2)
    return(0)

sizeh = 4
sizew = 4
px = 2 #player
py = 3
n = 1 #number of boxes
bx = 2 #box
by = 2
hx = 0 #destination
hy = 3
wallx = 1 #wall
wally = 3

while True:

    while True:
        write_game(px,py,bx,by,sizeh,sizew)
        move = input("Your move? ").upper()
        if move in ['W','S','A','D']:
            break

    [next_x,next_y] = object_move(move,px,py)
    if check_move(move,next_x,next_y) == True:
        if next_x == bx and next_y == by:
            [next_bx,next_by] = object_move(move,bx,by)
            if check_move(move,next_bx,next_by) == True:
                [px,py] = [next_x,next_y]
                [bx,by] = [next_bx,next_by]
            else:
                print("Can't Move !!! Go Away !!!")
        else:
            [px, py] = [next_x, next_y]
    else:
         print("Can't Move !!! Go Away !!!")

    endgame = end_game(bx, by)
    if endgame == 0:
        continue
    write_game(px, py, bx, by, sizeh, sizew)
    if endgame == 1:
        print("YOU WON !!!")
        break
    elif endgame == 2:
        print("YOU LOST !!!")
        break