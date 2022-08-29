def nb_year(p0, percent, aug, p) :
    day = 0
    while p0 < p :
        p0 = int(p0 + p0*percent/100 + aug)
        day += 1
    return day
