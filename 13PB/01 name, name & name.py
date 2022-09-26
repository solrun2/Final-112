def namelist(names) :
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return names[0] + ' & ' + names[1]
    else:
        return names[0] + ', ' + namelist(names[1:]) 