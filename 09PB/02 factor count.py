def factor_count(n):
    cnt = 0
    i = 1
    while i<=n :
        if n%i == 0 :
            cnt += 1
        i += 1
    return cnt

n = int(input("Enter n: "))
c = factor_count(n)
print(c)