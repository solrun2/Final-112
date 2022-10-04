def cloth_size(width_list) :
    dict = {
        "S" : 0 ,
        "M" : 0 ,
        "L" : 0 
    }
    for i in width_list :
        if i <= 36 :
            dict["S"] += 1
        elif i <= 44 :
            dict["M"] += 1
        else :
            dict["L"] += 1
    return dict