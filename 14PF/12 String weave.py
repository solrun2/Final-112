text = input()
s = [0]*len(text)
if len(text) % 2 == 0 :
    length = len(text) // 2
else :
    length = len(text) // 2 + 1
s[::2] = [i for i in text[:length]]
s[1::2] = [i for i in text[:length-1:-1]]
for i in s :
    print(i, end="")