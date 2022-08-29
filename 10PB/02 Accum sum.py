def accum_sum(l) :
    new_l = []
    x = 0
    for i in l :
        x += i
        new_l.append(x)
    print("Original list:")
    print(l)
    print("Accumulative Sum:")
    for i in new_l :
        print(i)

l = []
while True :
    n = int(input("Enter a number (0 to end): "))
    if n == 0 :
        break
    elif n < 1 or n > 999 :
        print("Number is out of range.")
    else :
        l.append(n)
accum_sum(l)
