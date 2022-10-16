dict = {}
max = 0
while True :
    s = input()
    if s == "end" :
        break
    else :
        s = s.split()
    if s[0] not in dict :
        dict[s[0]] = [s[1],1]
    else :
        dict[s[0]][1] += 1
        if float(dict[s[0]][0]) < float(s[1]) :
            dict[s[0]][0] = s[1]
    if float(s[1]) > max :
        max = float(s[1])
        winner = s[0]
orderDict = sorted(dict)
for i in orderDict :
    if dict[i][1] == 1 :
        print("{} bid at the price of {:.1f} baht in 1 time.".format(i,float(dict[i][0])))
    else :
        print("{} bid at the price of {:.1f} baht in {} times.".format(i,float(dict[i][0]),dict[i][1]))
print("The winner is {}.".format(winner))