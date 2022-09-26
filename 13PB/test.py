def extract_string(text) :
    ans = []
    s = ""
    for i in range(len(text)) :
        if i+1 < len(text) :
            if text[i].isnumeric() and not text[i+1].isnumeric() or not text[i].isnumeric() and text[i+1].isnumeric() :
                s += text[i]
                ans.append(s)
                s = ""
            else :
                s += text[i]
        else :
            s += text[i]
            ans.append(s)
        new_ans = []
        for i in ans :
            if i.isnumeric() :
                new_ans.append(int(i))
            else :
                new_ans.append(i)
    return new_ans
print( extract_string("3.14") )
print( extract_string("AB12XY23") )
print( extract_string("Number 4, Privet Drive") )
print( extract_string("1 2 3 4 5 I love you.") )