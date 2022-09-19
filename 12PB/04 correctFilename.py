text = input()
if "." in text :
    text = text.rsplit(".",1)
    if len(text[0]) > 15 :
        name = text[0][:15]
    else :
        name = text[0]
    if len(text[1]) > 3 :
        surname = text[1][:3]
    else :
        surname = text[1]
else :
    surname = -1
    if len(text) > 15 :
        name = text[:15]
    else :
        name = text
new_name = ""
for i in name :
    if i in '\/*:|"<>. ' :
        new_name += "_"
    else :
        new_name += i
if type(surname) == int :
    print(new_name)
else :
    new_surname = ""
    for i in surname :
        if i in '\/*:|"<>. ' :
            new_surname += "_"
        else :
            new_surname += i    
    print(new_name+"."+new_surname)