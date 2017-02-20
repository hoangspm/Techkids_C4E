#Shepherd

sizes = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is SPM and here is flock")
print(sizes)
months = 3

for month in range(months):
    max = 0
    for i in range(7):
       if sizes[max] < sizes[i]:
           max = i
    print("Now my biggest sheep has size ",sizes[max]," let's shear it")

    sizes[max] = 8
    print("after shearing, here is my flock")
    print(sizes)
    
    print("MONTH ",month+1," :")
    for i in range(7):
        sizes[i] += 50
    print("One month has passed, now here is my flock")
    print(sizes)

total_size = 0
for i in range(7):
    total_size += sizes[i]

print("My flock has size in toltal: ",total_size)
print("I would get ",total_size,"* 2$ = ",total_size*2)
