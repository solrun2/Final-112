variableDict = {}
print("Enter variables and values:")
while True :
    s = input()
    if s == "-1" :
        break
    s = s.split(" = ")
    variableDict[s[0]] = s[1]
print("Enter your program:")
ans = []
while True :
    s = input()
    if s == "-1" :
        break
    ans.append(s)
print("Result:")
for i in ans :
    for j in variableDict :
        i = i.replace("{"+j+"}",variableDict[j])
    print(i)