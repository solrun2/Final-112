allEx =int(input())
passPercent = float(input())
studentNum = int(input())
scoreList = []
for i in range(studentNum):
    scoreList.append(int(input()))
cnt = 0
for i in scoreList :
    if (i/allEx)*100 < passPercent :
        cnt += 1
print(cnt)
n = 1
for i in scoreList :
    scorePercent = (i/allEx) * 100
    if scorePercent >= passPercent :
        print("{} {:.2f}".format(n, scorePercent))
    else :
        print("({}) {:.2f}".format(n, scorePercent))
    n += 1