def find_sd(l) :
    x = 0
    for i in range(len(l)) :
        x += (l[i]-avg)**2
    sd = math.sqrt(x/(len(l)-1))
    return sd

import math
l = []
while True :
    n = float(input("Enter score: "))
    if n == -1 :
        break
    elif n < 0 or n > 100 :
        print("Score is out of range.")
    else :
        l.append(n)
if len(l) == 0 :
    pass
else :
    print("Maximum score is {:.2f}.".format(max(l)))
    print("Minimum score is {:.2f}.".format(min(l)))
    avg = sum(l)/len(l)
    print("Average score is {:.2f}.".format(avg))
    sd = find_sd(l)
    print("Standard deviation is {:.2f}.".format(sd))