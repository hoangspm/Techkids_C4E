s = "ThiS is String with Upper and lower case Letters"
s = s.lower()

count = {}

for i in s:
    if (i != " "):
        if (i not in count.keys()):
            count[i] = 1
        else:
            count[i] += 1

cc = list(count. keys())
cc. sort()

for i in cc:
    print(i,count[i])
