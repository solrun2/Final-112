l = []
while True :
    n = int(input())
    if n == 0 :
        break
    l.append(n)
maxnum = l[0]
for i in range(len(l)) :
    sum = 0
    for j in range(i, len(l)) :
        sum += l[j]
        if sum > maxnum :
            maxnum = sum
print(maxnum)