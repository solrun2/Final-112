l = []
n = int(input())
b = n
if n == -1 :
    pass 
else :
    l.append(n)
    while True :
        n = int(input())
        if n == -1 :
            break     
        if n >= b :
            l.append(n) 
            b = n
    print(l)