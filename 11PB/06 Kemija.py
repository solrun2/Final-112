text = input("Enter text : ")
text += "  "
ans = ""
i = 0
while i<len(text) : 
    ans += text[i]
    if text[i] in "aeiou" and text[i+1] == "p" and text[i+2] == text[i] :
        i += 3
    else :
        i += 1
print(ans[:-2])