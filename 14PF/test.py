ls = []
min = 1e9
while True :
    n = input()
    if n == "" :
        break
    else :
        n = float(n)
    if n < min :
        min = n
    ls.append(n)
print(ls.count(min))