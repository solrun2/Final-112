text = input().lower()
text = text + "`"
a = "`"
cnt = 0
for i in text :
    if i > a :
        cnt += 1
        a = i
    else :
        print(cnt)
        break