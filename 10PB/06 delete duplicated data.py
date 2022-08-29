def remove_duplicates(t) :
    ans = []
    for e in t :
        if e not in ans :
            ans.append(e)
    return ans