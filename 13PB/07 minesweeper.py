area = input().split("x")
m = int(area[0])
n = int(area[1])
bombcnt = int(input())
bombPosition = []
for i in range(bombcnt) :
    x = input().split(",")
    bombPosition.append([int(x[0]),int(x[1])])
table = []
for i in range(m) :
    table.append([])
    for j in range(n) :
        table[i].append(0)
for i in range(bombcnt) :
    table[bombPosition[i][0]][bombPosition[i][1]] = "*"
for i,j in bombPosition :
    for k in range(i-1,i+2) :
        for l in range(j-1,j+2) :
            if k >= 0 and k < m and l >= 0 and l < n and table[k][l] != "*" :
                table[k][l] += 1
for i in range(m) :
    for j in range(n) :
        print(table[i][j],end="")
    print()