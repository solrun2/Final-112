n = int(input())
bankNote = []
for i in range(n) :
    bankNote.append(int(input()))
bankNote.sort(reverse = True)
money = int(input())
for i in bankNote :
    print("{}: {}".format(i,money//i))
    money %= i