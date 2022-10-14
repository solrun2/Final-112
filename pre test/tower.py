n = int(input())
towerList = []
for i in range(n) :
    towerList.append(int(input()))
if sum(towerList)%n != 0 :
    print("Impossible")
else :
    avg = sum(towerList)//n
    cnt = 0
    while True :
        if towerList == [avg]*n :
            break
        towerList[towerList.index(max(towerList))] -= 1
        towerList[towerList.index(min(towerList))] += 1
        cnt += 1
    if cnt > 10 :
        print("Impossible")
    else :
        print(cnt)