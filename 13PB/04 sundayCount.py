dayOne = input().split("-")
dayTwo = input().split("-")
firstSunday = int(input())
if int(dayOne[1]) < 1 or int(dayOne[1]) > 12 or int(dayOne[2]) < 1 or int(dayOne[2]) > 31 or int(dayTwo[1]) < 1 or int(dayTwo[1]) > 12 or int(dayTwo[2]) < 1 or int(dayTwo[2]) > 31 :
    print("Wrong Month")
elif firstSunday < 1 or firstSunday > 7 :
    print("Wrong Day")
dayInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
