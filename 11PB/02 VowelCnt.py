text = input()
cnt = 0
for i in text :
    if i in "aeiouAEIOU" :
        cnt += 1
print(cnt)