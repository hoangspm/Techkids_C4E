p = {
    "x": 2,
    "y": 3
}

boxes = []

boxes.append({"x": 2, "y": 4})
boxes.append({"x": 3, "y": 3})
boxes.append({"x": 1, "y": 1})

points = []

points.append({"x": 4, "y": 6})
points.append({"x": 4, "y": 7})
points.append({"x": 4, "y": 8})

screen_width = 10
screen_height = 10

def stage_two():
    p_two = {
        "x": 1,
        "y": 1
    }

    boxes_two = []

    boxes.append({"x": 2, "y": 6})
    boxes.append({"x": 3, "y": 7})
    boxes.append({"x": 1, "y": 5})

    points_two = []

    points.append({"x": 4, "y": 4})
    points.append({"x": 4, "y": 1})
    points.append({"x": 4, "y": 8})

    screen_width = 10
    screen_height = 10
    return p_two, boxes_two, points_two, screen_width, screen_height

def check_lose(next_bx,next_by,screen_height,screen_width):
    if [next_bx,next_by] == [0,0] or [next_bx,next_by] == [0,screen_height-1] or [next_bx,next_by] == [screen_width-1,0] or [next_bx,next_by] == [screen_width-1,screen_height-1]:
        return True
    return False
def check_win(boxes, points):
    win = 0
    for box in boxes:
        for point in points:
            if(box["x"] == point["x"]) and (box["y"] == point["y"]):
                win += 1
    return win



def find_object(objects, x, y):
    for object in objects:
        if object["x"] == x and object["y"] == y:
            return object
    return None


def in_map(x, y, screen_width, screen_height):
    if x < 0 or y < 0 or x > screen_width - 1 or y > screen_height - 1:
        return False
    return True

def check_match(objects, x, y):
    for object in objects:
        if object["x"] == x and object["y"] == y:
            return True
    return False

def print_map(p, boxes, points, screen_width, screen_height):
    for y in range(screen_height):
        for x in range(screen_width):
            if x == p["x"] and y == p["y"]:
                print("T ", end="")
            elif check_match(boxes, x, y):
                print("B ", end="")
            elif check_match(points, x, y):
                print("x ", end="")
            else:
                print("- ", end="")
        print()


def move(x, y, dx, dy):
    return [x + dx, y + dy]
while True:
    print_map(p, boxes, points, screen_width, screen_height)

    choice = input("What do you want? U - D - L - R: ").upper()

    dx = 0
    dy = 0

    if choice == "W":
        dy = -1
    elif choice == "S":
        dy = 1
    elif choice == "A":
        dx = -1
    elif choice == "D":
        dx = 1

    [next_px, next_py] = move(p["x"], p["y"], dx, dy)

    if not in_map(next_px, next_py, screen_width, screen_height):
        print("Go away!!!")
    else:
        found_box = find_object(boxes, next_px, next_py)
        if found_box is not None:
            [next_bx, next_by] = [found_box["x"] + dx, found_box["y"] + dy]
            if in_map(next_bx, next_by, screen_width, screen_height):
                found_box["x"] = next_bx
                found_box["y"] = next_by
                p["x"], p["y"] = next_px, next_py
        else:
            p["x"], p["y"] = next_px, next_py
    win = check_win(boxes, points)
    if win == len(points):
        print("YOU WIN")
        print_map(p, boxes, points, screen_width, screen_height)
        break