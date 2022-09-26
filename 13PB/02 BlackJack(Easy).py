n = int(input())
faceCard = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
cardPoint = [1,2,3,4,5,6,7,8,9,10,10,10,10]
ans = []
for i in range(n) :
    card = [i for i in input().split()]
    bigPoint = 0
    score = 0
    for i in card :
        if score <= 16 :
            if faceCard.index(i) > bigPoint :
                bigPoint = faceCard.index(i)
            score += cardPoint[faceCard.index(i)]
    if score > 21 :
        ans.append("busted")
    else :
        ans.append(score)
for i in ans :
    print(i)