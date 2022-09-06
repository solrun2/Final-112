def closestNum(list) :
    distance = max(list) - min(list)
    for j in range(len(list)-1) :
        if abs(list[j] - list[j+1]) < distance :
            distance = abs(list[j] - list[j+1])
            i = j
    for j in range(len(list)-1) :
        if abs(list[j] - list[j+1]) == distance :
            print(list[j], list[j+1])

n = int(input())
l = []
for i in range(n) :
    l.append(int(input()))
l.sort()
closestNum(l)
