ans = []
max_left = 0
max_right = 0
while True:
    equation = input()
    equation_list = []
    if equation == "-1":
        break
    if equation.count("=") == 1:
        equation_list = equation.split("=")
        temp = []
        for i in equation_list:
            temp.append(i.strip())
        
        if len(temp[0]) > max_left:
            max_left = len(temp[0])
        if len(temp[1]) > max_right:
            max_right = len(temp[1])
                
        equation_list = temp
        ans.append(equation_list)
    
    else:
        ans.append(equation.strip())

for i in ans:
    if len(i) == 2:
        print("{0:>{a}s} = {1:<{b}s}".format(i[0], i[1], a=max_left, b=max_right))
    else:
        print(" " * (max_left + 1) + i)