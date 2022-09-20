text = input()
if "." in text :
    text = text.rsplit(".",1)
    if len(text[0]) > 15 :
        name = text[0][:15]
    else :
        name = text[0]
    if len(text[1]) > 3 :
        extension = text[1][:3]
    else :
        extension = text[1]
else :
    extension = -1
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
if type(extension) == int :
    print(new_name)
else :
    new_extension = ""
    for i in extension :
        if i in '\/*:|"<>. ' :
            new_extension += "_"
        else :
            new_extension += i    
    print(new_name+"."+new_extension)