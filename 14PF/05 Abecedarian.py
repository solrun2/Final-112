def abecedarianCount(word):
    count = 0
    for i in range(len(word)-1):
        if word[i] <= word[i+1]:
            count += 1
        else :
            count += 1
            break
    return count

text = input()
print(abecedarianCount(text))