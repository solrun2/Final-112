def findMajorityElement(list,n) :
    f_count = 0
    index = -1
    for i in range(n) :
        count = 0
        for j in range(n) :
            if list[i] == list[j] :
                count += 1
        if count > f_count :
            f_count = count
            index = i
    if f_count > n/2 :
        print(list[index])
    else :
        print("0")

n = int(input())
l = []
for i in range(n) :
    l.append(input())
findMajorityElement(l,n)