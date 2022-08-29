def fibo(n) :
    if n == 1 or n == 2 :
        return 1
    else :
        a = 0
        b = 1
        i = 1
        while i < n :
            a,b = b,a+b
            i += 1
        return b

n = int(input("Enter n: "))
print("fibo({}) = {}".format (n, fibo(n)))