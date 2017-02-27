def match(x,y,a,b):
    l = n
    for i in range(l):
        if [x,y] == [a[i],b[i]]:
            return(True)
    return(False)

def write_game(px,py,bx,by,h,w):
    for y in range(h):
        for x in range(w):
            if [x,y] == [px,py]:
                print("P", end="")
            elif [x,y] == [wallx,wally]:
                print("#", end="")
            elif match(x,y,bx,by):
                print("B", end="")
            elif match(x,y,hx,hy):
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

def check_blocked(move,x,y):
    return (x >= 0 and x < sizew and y >= 0 and y < sizeh and [x,y] != [wallx,wally])

def end_game():
    count = 0
    for i in range(n):
        for j in range(n):
            if hx[i] == bx[j] and hy[i] == by[j]:
                count += 1
                break;
    if count == n:
        return (1)
    for i in range (n):
        if (check_blocked('W',bx[i],by[i]-1) == False and check_blocked('A',bx[i]-1,by[i]) == False):
            return(2)
        if (check_blocked('S',bx[i],by[i]+1) == False and check_blocked('A',bx[i]-1,by[i]) == False):
            return(2)
        if (check_blocked('W',bx[i],by[i]-1) == False and check_blocked('D',bx[i]+1,by[i]) == False):
            return(2)
        if (check_blocked('S',bx[i],by[i]+1) == False and check_blocked('D',bx[i]+1,by[i]) == False):
            return(2)  
    return(0)

def check_move(move,x,y):
    if check_blocked(move, x, y) == True:
        for i in range(n):
            if visited[i] == False and x == bx[i] and y == by[i]:
                visited[i] = True
                [next_x, next_y] = object_move(move, bx[i], by[i])
                if check_move(move,next_x,next_y) == True:
                    [bx[i],by[i]] = [next_x, next_y]
                    visited[i] = False
                    return (True)
                return (False)
        return(True)
    return (False)

sizeh = 6
sizew = 6
px = 3 #player
py = 3
n = int(input('Number of boxes (max = 4): ')) #number of boxes
bx = [3,3,2,4]
by = [2,4,3,3]
hx = [1,0,0,1]
hy = [1,1,2,2]
visited = [False]*4
print(visited)
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
        [px, py] = [next_x, next_y]
    else:
         print("Can't Move !!! Go Away !!!")

    endgame = end_game()
    if endgame == 0:
        continue
    write_game(px, py, bx, by, sizeh, sizew)
    if endgame == 1:
        print("YOU WON !!!")
        break
    elif endgame == 2:
        print("YOU LOST !!!")
        break