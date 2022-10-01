def fibo(n) :
    if n == 0 :
        return 1
    elif n == 1 :
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

n = float(input())
s = input()
if s not in "eEoO" or n % 1 != 0 or n < 0 or n <= 0 and s in "Oo" or len(s) != 1 or s == "":
    print("ERROR")
else :
    n = int(n)
    sum = 0
    if s in "Ee" :
        for i in range(n+1) :
            if i%2 == 0 :
                sum += fibo(i)
    else :
        for i in range(n+1) :
            if i%2 == 1 :
                sum += fibo(i)
    print(sum)