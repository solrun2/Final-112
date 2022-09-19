text = input().strip().split(",")
ans = []
for i in text :
    ans.append(i.strip())
print('"' + '","'.join(ans) + '"')