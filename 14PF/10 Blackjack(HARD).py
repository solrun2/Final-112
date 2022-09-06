card = input().split()
point = []
for i in card :
    if i == "A" :
        point.append(1)
    elif i == "J" or i == "Q" or i == "K" :
        point.append(10)
    else :
        point.append(int(i))
allpoint = 0
cnt = 0
for i in point :
    if allpoint >= 16 :
        break
    cnt += 1
    allpoint += i
if allpoint > 21 :
    ans = "busted"
else :
    ans = allpoint
maxpoint = ""
numpoint = 0
for i in card[:cnt] :
    if i == "K" :
        maxpoint = "K"
        numpoint = 10
    elif i == "Q" :
        maxpoint = "Q"
        numpoint = 10
    elif i == "J" :
        maxpoint = "J"
        numpoint = 10
    elif i == "A" :
        continue
    elif 2 <= int(i) <= 10 :
        if int(i) > numpoint :
            maxpoint = i
            numpoint = int(i)
print(maxpoint)
print(ans)
    