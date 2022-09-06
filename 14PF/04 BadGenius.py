text = input()
text_list = []
for i in text :
    if i != " " and i not in text_list :
        text_list.append(i)
code = input()
code_list = []
for i in code :
    code_list.append(i)
ans = input()
decode = ""
for i in ans :
    if i in code_list :
        decode += text_list[code_list.index(i)]
    else :
        decode += i
print(decode)
