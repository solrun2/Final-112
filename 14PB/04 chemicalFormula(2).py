def extract(formula) :
    list = []
    s = ""
    for i in range(len(formula)) :
        if formula[i].isalpha() and formula[i].isupper() :
            if i+1 < len(formula) :
                if formula[i+1].isalpha() :
                    if formula[i+1].isupper() :
                        list.append(formula[i])
                    elif formula[i+1].islower() :
                        list.append(formula[i]+formula[i+1])
                elif formula[i+1].isnumeric() :
                    list.append(formula[i])
            else :
                list.append(formula[i])
        elif formula[i].isalpha() and formula[i].islower() :
            continue
        elif formula[i].isnumeric() :
            if i+1 < len(formula) :
                s += formula[i]
                if formula[i+1].isnumeric() :
                    pass
                elif formula[i+1].isalpha() :
                    list.append(s)
                    s = ""
            else :
                s += formula[i]
                list.append(s)
                s = ""
    return list

formula = input()
list = extract(formula)
element = input()
count = 0
for i in range(len(list)) :
    if i+1 < len(list) :
        if list[i] == element and list[i+1].isnumeric() :
            count += int(list[i+1])
        elif list[i] == element and list[i+1].isalpha() :
            count += 1
    else :
        if list[i] == element :
            count += 1
print(count)