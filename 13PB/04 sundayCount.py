firstDay = [int(i) for i in input().split("-")]
lastDay = [int(i) for i in input().split("-")]
firstSunday = int(input())
dayInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
wrongMonth = False
wrongDay = False
if firstDay[1] < 1 or firstDay[1] > 12 or lastDay[1] < 1 or lastDay[1] > 12 :
    wrongMonth = True
if firstDay[1] <= 12 and lastDay[1] <= 12 :
    if firstDay[0] < 1 or firstDay[0] > dayInMonth[firstDay[1]-1] or lastDay[0] < 1 or lastDay[0] > dayInMonth[lastDay[1]-1] :
        wrongDay = True
if firstDay[0] > 31 or firstDay[0] < 1 or lastDay[0] > 31 or lastDay[0] < 1 :
    wrongDay = True
if firstSunday < 1 or firstSunday > 7 :
    wrongDay = True
if wrongMonth :
    print("Wrong Month")
if wrongDay :
    print("Wrong Day")
if not wrongMonth and not wrongDay :
    sundayCount = 0
    if firstDay[1] == lastDay[1] :
        dayDiff = abs(firstDay[0] - lastDay[0])
        if firstDay[0]%7 == firstSunday or firstSunday == 7 and firstDay[0]%7 == 0 :
            sundayCount += 1
        sundayCount += abs(dayDiff//7)
    elif firstDay[1] < lastDay[1] :
        dayDiff = sum(dayInMonth[firstDay[1]+1:lastDay[1]]) + dayInMonth[firstDay[1]-1] - firstDay[0] + lastDay[0]
        if firstDay[0]%7 == firstSunday or firstSunday == 7 and firstDay[0]%7 == 0 :
            sundayCount += 1
        sundayCount += dayDiff//7
    elif lastDay[1] < firstDay[1] :
        dayDiff = sum(dayInMonth[lastDay[1]+1:firstDay[1]]) + dayInMonth[lastDay[1]-1] - lastDay[0] + firstDay[0]
        if lastDay[0]%7 == firstSunday or firstSunday == 7 and lastDay[0]%7 == 0 :
            sundayCount += 1
        sundayCount += dayDiff//7
    print(sundayCount)