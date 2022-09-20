money = input().strip()
if "".join("".join(money.split(".")).split(",")).isdigit() :
    if "," in money and "." in money :
        dotCheck = money.split(".")
        if len(dotCheck[1]) > 2 or money[-1] == "." or money[-1] == "," :
            print("ERROR")
        elif len(dotCheck[1]) > 2 :
            print("ERROR")
        else :
            commaCheck = dotCheck[0].split(",")
            cnt = 0
            for i in commaCheck[1::] :
                if len(i) != 3 :
                    cnt = -1
                    print("ERROR")
                    break
            if cnt == 0 :
                if len(commaCheck[0]) > 3 :
                    cnt = -1
                    print("ERROR")
            if cnt == 0 :
                ans = ""
                ans += "".join(commaCheck) + "." + dotCheck[1]
                if len(dotCheck[1]) == 2 :
                    print("{:.2f}".format(float(ans)+1))
                else :
                    print(float(ans)+1)
    elif "," in money :
        commaCheck = money.split(",")
        cnt = 0
        for i in commaCheck :
            if len(i) > 3 or money[-1] == "." or money[-1] == ",":
                cnt = -1
                print("ERROR")
                break
        if cnt == 0 :
            for i in commaCheck[1::] :
                if len(i) != 3 :
                    cnt = -1
                    print("ERROR")
                    break
        if cnt == 0 :
            if len(commaCheck[0]) > 3 :
                cnt = -1
                print("ERROR")
        if cnt == 0 :
            ans = ""
            ans += "".join(commaCheck)
            print(int(ans)+1)
    elif "." in money :
        dotCheck = money.split(".")
        if len(dotCheck[1]) > 2 or money[-1] == "." or money[-1] == "," :
            print("ERROR")
        else :
            if len(dotCheck[1]) == 2 :
                print("{:.2f}".format(float(money)+1))
            else :
                print(float(money)+1)
    else :
        print(int(money)+1)
else :
    print("ERROR")