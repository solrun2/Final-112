def abecedarianCount(word):
    count = 0
    for i in range(len(word)-1):
        if word[i] <= word[i+1]:
            count += 1
        else :
            break
    count += 1
    return count
text = input()
if text.isspace() :
    print(0)
else :
    print(abecedarianCount(text))