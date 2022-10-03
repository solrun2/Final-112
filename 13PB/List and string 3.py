def extract_string(text) :
    if text == "" :
        return []
    else :
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

print(extract_string(""))