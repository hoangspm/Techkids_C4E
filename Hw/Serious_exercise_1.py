#Serious_exercise_1
goods = ["T-Shirt","Sweater"]

while True:
    act = input("Welcome, what do want? (C,R,U,D)")
    act = act.upper()
    
    if act == "C":
        item = input("Enter new item: ")
        goods.append(item)

        len_goods = len(goods)
        if len_goods == 0:
            print("Empty !!!")
        else:
            print("Our items: ", end="")
            for i in range(len_goods-1):
                print(goods[i],', ',end="")
            print(goods[len_goods-1])
        
    elif act == "R":
        len_goods = len(goods)
        if len_goods == 0:
            print("Empty !!!")
        else:
            print("Our items: ", end="")
            for i in range(len_goods-1):
                print(goods[i],', ',end="")
            print(goods[len_goods-1])

    elif act == "U":
        pos = int(input("Update position? "))
        len_goods = len(goods)
        while pos not in range(len_goods):
            pos = int(input("Illegal position!!! Update position??? "))
        item = input("New item? ")
        
        goods[pos]=item

        len_goods = len(goods)
        if len_goods == 0:
            print("Empty !!!")
        else:
            print("Our items: ", end="")
            for i in range(len_goods-1):
                print(goods[i],', ',end="")
            print(goods[len_goods-1])

    elif act == "D":
        pos = int(input("Delete position? "))
        len_goods = len(goods)
        while pos not in range(len_goods):
            pos = int(input("Illegal position!!! Update position??? "))
            
        goods.pop(pos)

        len_goods = len(goods)
        if len_goods == 0:
            print("Empty !!!")
        else:
            print("Our items: ", end="")
            for i in range(len_goods-1):
                print(goods[i],', ',end="")
            print(goods[len_goods-1])
