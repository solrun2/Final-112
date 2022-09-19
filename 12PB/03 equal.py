front = []
back = []
while True :
    s = input()
    if s == "-1" :
        break
    s = s.split("=",1) 
    front.append(s[0].strip())
    back.append(s[1].strip())
length = 0
for i in front :    
    if len(i) > length :
        length = len(i)
for i in range(len(front)) :
    print(front[i].rjust(length)+" = "+back[i])