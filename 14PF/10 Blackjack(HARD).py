card = [i for i in input().split()]
faceCard = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
cardPoint = [1,2,3,4,5,6,7,8,9,10,10,10,10]
bigPoint = 0
score = 0
for i in card :
    if score <= 16 :
        if faceCard.index(i) > bigPoint :
            bigPoint = faceCard.index(i)
        score += cardPoint[faceCard.index(i)]
print(faceCard[bigPoint])
if score > 21 :
    print("busted")
else :
    print(score)