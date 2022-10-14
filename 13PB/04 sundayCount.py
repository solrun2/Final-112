daymonth1 = [int(i) for i in input().split("-")]
daymonth2 = [int(i) for i in input().split("-")]
firstSunday = int(input())
monthlist = [31,28,31,30,31,30,31,31,30,31,30,31]
check = [True,True]
if daymonth1[1] < 1 or daymonth1[1] > 12 or daymonth2[1] < 1 or daymonth2[1] > 12 :
    check[1] = False
if check[1] == True and (daymonth1[0] < 1 or daymonth1[0] > monthlist[daymonth1[1]-1] or daymonth2[0] < 1 or daymonth2[0] > monthlist[daymonth2[1]-1]) or firstSunday < 1 or firstSunday > 7 or daymonth1[0] > 31 or daymonth2[0] > 31 :
    check[0] = False
if check[0] == False or check[1] == False :
    if check[1] == False :
        print("Wrong Month")
    if check[0] == False :
        print("Wrong Day")
else :
    daysol = []
    cnt = []
    daysol.append(daymonth1)
    daysol.append(daymonth2)
    for i in daysol:
        d,m = int(i[0]),int(i[1])
        ans = sum(monthlist[:m-1]) + d
        cnt.append(ans)
    cnt.sort()
    count = 0
    while firstSunday <= cnt[1]:
            if firstSunday >= cnt[0]:
                    count += 1
            firstSunday += 7
    print(count)