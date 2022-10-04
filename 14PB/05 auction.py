dict = {}
while True :
    n = input()
    if n == "end" :
        break
    bid = n.split()
    if bid[0] not in dict :
        dict[bid[0]] = [(bid[1]),1]
    else :
        if bid[1] > dict[bid[0]][0] :
            dict[bid[0]] = [(bid[1]),dict[bid[0]][1]+1]
orderDict = sorted(dict)
for i in orderDict :
    if dict[i][1] == 1 :
        print("{} bid at the price of {:.1f} baht in 1 time.".format(i,float(dict[i][0])))
    else :
        print("{} bid at the price of {:.1f} baht in {} times.".format(i,float(dict[i][0]),dict[i][1]))
    if float(dict[i][0]) == max(float(dict[j][0]) for j in orderDict) :
        winner = i
print("The winner is {}.".format(winner))