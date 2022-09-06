def bigram(s):
    return [s[i:i+2] for i in range(len(s)-1)]

def remove_duplicates(t) :
    ans = []
    for i in t :
        if i not in ans :
            ans.append(i)
    return ans

s = input().lower()
ans = remove_duplicates(sorted(bigram(s)))
for i in ans :
    print(i)

