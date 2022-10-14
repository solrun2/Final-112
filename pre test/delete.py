s = input()
check = True
while check :
    check = False
    for i in range(len(s)) :
        if i+1 < len(s) and s[i] == s[i+1] :
            s = s[:i] + s[i+2:]
            check = True
print(s)