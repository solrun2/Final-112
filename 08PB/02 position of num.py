def digit(num) :
    num %= 10 
    return num

def tens(num) :
    num %= 100
    num //= 10
    return num

def hundreds(num) :
    num %= 1000
    num //= 100
    return num

def thousands(num) :
    num %= 10000
    num //= 1000
    return num

def sum_digits(num) :
    ans = digit(num) + tens(num) + hundreds(num) + thousands(num)
    return ans

n   = int(input('Enter a number (0 to 9999): '))
print('Digit place is %d.' % (digit(n)))
print('Tens place is %d.' % (tens(n)))
print('Hundreds place is %d.' % (hundreds(n)))
print('Thousands place is %d.' % (thousands(n)))
print('Sum of all digits is %d.' % sum_digits(n))