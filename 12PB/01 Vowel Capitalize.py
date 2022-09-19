text = input()
ans = ""
for i in text :
    if i in "aeiouAEIOU" :
        ans += i.upper()
    else :
        ans += i.lower()
print(ans)