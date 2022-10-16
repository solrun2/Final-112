hw = [int(i) for i in input().split()]
percent = [float(i) for i in input().split()]
n = int(input())
participant = []
for i in range(n) :
    participant.append([int(i) for i in input().split()])
score = []
for i in range(n) :
    score.append([int(i) for i in input().split()])
studentDict = {}
for i in range(n) :
    studentDict[i] = [round(sum(participant[i])/len(participant[i])*100,2),round(sum(score[i])/sum(hw)*100,2)]
passcnt = 0
for i in studentDict :
    if studentDict[i][0] < percent[0] and studentDict[i][1] < percent[1] :
        passcnt += 1
print(passcnt)
for i in studentDict :
    if studentDict[i][0] < percent[0] and studentDict[i][1] < percent[1] :
        print("({}) {:.2f} {:.2f}".format(i+1,studentDict[i][0],studentDict[i][1]))
    else :
        print("{} {:.2f} {:.2f}".format(i+1,studentDict[i][0],studentDict[i][1]))