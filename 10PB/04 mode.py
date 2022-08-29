l = []
cnt = [0]*11
i = 0
while i<20 :
    n = int(input("Enter score: "))
    if n < 0 or n > 10 :
        print("Score is out of range.")
        continue
    l.append(n)
    cnt[n] += 1
    i += 1
print("-----")
print("Original list:")
print(l)
print("Mode of scores:")
for i in range(11) :
    if cnt[i] == max(cnt) :
        print(i)