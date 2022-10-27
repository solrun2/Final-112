area = [int(i) for i in input().split()]
wall = []
for i in range(area[1]) :
    alp = input()
    wall.append([])
    for j in alp :
        wall[i].append(j)
dmgcnt = int(input())
dmgapl = []
for i in range(dmgcnt) :
    dmgapl.append(input())
for i in range(area[1]) :
    for j in range(area[0]) :
        if wall[i][j] in dmgapl :
            wall[i][j] = "."
cnt = 0
while cnt < area[1] :
    for i in range(area[1]-1,0,-1) :
        for j in range(area[0]) :
            if wall[i][j] == "." :
                wall[i][j],wall[i-1][j] = wall[i-1][j],wall[i][j]
    cnt += 1
for i in range(area[1]) :
    for j in range(area[0]) :
        print(wall[i][j],end="")
    print()