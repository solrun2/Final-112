def bi(t):
     sol = [t[i:i+2] for i in range(len(t)-1)]
     return sorted(sol)
def remove(t):
    ans = []
    for i in t:
        if i not in ans:
            ans.append(i)
    return ans


t = input().lower()

for i in remove((bi(t))) :
    print(i)