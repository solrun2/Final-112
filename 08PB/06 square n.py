import math

def sqrt_n_times(x, n) :
    ans = x
    i = 1
    while i<= n :
        ans = math.sqrt(ans)
        i += 1
    return ans

x = float(input())
n = int(input())
print( sqrt_n_times(x, n) )