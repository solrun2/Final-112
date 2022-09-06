text = input()
n = int(input())
while abs(n) > len(text) :
    if n > 0 :
        n -= len(text)
    else :
        n += len(text)
s = text[-n::] + text[:-n:]
print(s)