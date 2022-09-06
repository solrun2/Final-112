text = input()
s = [0]*len(text)
if len(text) % 2 == 1 :
    s[len(text)//2] = text[len(text)//2]
half = len(text)//2
s[:half] = [i for i in text[half-1::-1]]
if len(text)%2 == 0 :
    s[half:] = [i for i in text[-1:half-1:-1]]
else :
    s[half+1:] = [i for i in text[-1:half:-1]]
for i in s :
    print(i, end="")