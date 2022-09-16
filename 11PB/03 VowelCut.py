text = input()
ans = ""
for i in text :
    if i not in "aeiouAEIOU" :
        ans += i
print(ans)