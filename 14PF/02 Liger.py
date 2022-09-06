Dad = input()
Mom = input()
Son = ""
cnt = 0
for i in Dad :
    if i in "aeiou" :
        cnt += 1
    if cnt == 2 :
        break
    Son += i
if cnt == 0:
    Son = Dad
cnt = 0
for i in Mom : 
    if cnt >= 1 :
        Son += i
    if i in "aeiou" :
        cnt += 1
if cnt == 0 :
    Son += Mom
print(Son)