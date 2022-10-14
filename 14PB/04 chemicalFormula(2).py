def seperate(formula) :
    # seperate the formula into elements and numbers
    elements = []
    numbers = []
    for i in range(len(formula)) :
        if formula[i].isupper() :
            elements.append(formula[i])
            numbers.append(1)
        elif formula[i].islower() :
            elements[-1] += formula[i]
        elif i+1 < len(formula) and formula[i].isdigit() and formula[i+1].isdigit() :
            numbers[-1] = int(formula[i]+formula[i+1])
        elif formula[i].isdigit() :
            numbers[-1] = int(formula[i])
    return elements,numbers

formula = input()
formula = seperate(formula)
print(formula)
element = input()
count = 0
for i in range(len(formula[0])) :
    if formula[0][i] == element :
        count += formula[1][i]
print(count)