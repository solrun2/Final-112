def remove_duplicates(t) :
    ans = []
    for i in t :
        if i not in ans :
            ans.append(i)
    return ans