def countwords(s,x):
    l = len(s)
    count = 0
    for i in range(l-4):
        if s[i:i+5].lower() == x:
            count += 1
    return(count)
        
f = open("alice_words.txt", "r")
count = 0
line = 0
while True:
    s = f.readline()
    if len(s) == 0:
       break
    else:
        count += countwords(s,"alice")

f.close()
print(count)
