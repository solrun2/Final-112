score = []
i = 0
while i < 20 :
    n = int(input("Enter score: "))
    if n < 0 or n > 10 :
        print("Score is out of range.")
        continue
    score.append(n)
    i += 1
print("Original list:")
print(score)
for i in range(11) :
    print("{:2d}".format(i) ,end = "")
    print(" "+"*"*score.count(i))