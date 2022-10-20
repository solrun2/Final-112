priority = [int(i) for i in input().split()]
numcnt = []
for i in range(len(priority)):
    numcnt.append(i)
i = 0
while True :
    s = priority[i]+i
    if s > len(priority)-1 :
        s %= len(priority)
    priority.pop(s)
    numcnt.pop(s)
    if len(priority) == 1 :
        break
    if i > len(priority)-1 :
        i = i%len(priority)
    i = priority[i]+i
    if i > len(priority)-1 :
        i = i%len(priority)

print(numcnt[0])