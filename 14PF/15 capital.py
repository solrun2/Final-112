text = input().split()
for i in text :
    if i not in ["for","and","with","of"] :
        i = i[0].upper() + i[1:]
    print(i, end=" ")