damage = int(input())
zombie_hp = [int(x) for x in input().split()]
bullet = []
cnt = 0
for i in zombie_hp :
    while i > 0 :
        i -= damage
        cnt += 1
    bullet.append(cnt)
print(bullet[-1])
for i in bullet :
    print(i, end = " ")