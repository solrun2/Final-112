def count_char(word) :
    dict = {}
    for i in word :
        i = i.lower()
        if 97 <= ord(i) <= 122 :
            if i in dict :
                dict[i] += 1
            else :
                dict[i] = 1
    return dict