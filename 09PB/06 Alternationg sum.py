def alternatingSum(n) :
    if n%2 == 0 :
        return -n // 2
    else :
        return (n+1) // 2

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n,alternatingSum(n)))