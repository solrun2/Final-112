n = input()
if n.isnumeric() :
    n = int(n)
    hundred = n//100
    ten = (n%100)//10
    one = (n%100)%10
    one_list = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    ten_list = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    hundred_list = ["one-hundred","two-hundred","three-hundred","four-hundred","five-hundred","six-hundred","seven-hundred","eight-hundred","nine-hundred"]
    if n < 20 :
        print(one_list[n])
    elif n < 100 :
        if one == 0 :
            print(ten_list[ten-2])
        else :
            print(ten_list[ten-2] + "-" + one_list[one])
    elif n < 1000 :
        if ten == 0 and one == 0 :
            print(hundred_list[hundred-1])
        elif ten == 0 :
            print(hundred_list[hundred-1] + "-" + one_list[one])
        elif ten == 1 :
            print(hundred_list[hundred-1] + "-" + one_list[ten*10+one])
        elif one == 0 :
            print(hundred_list[hundred-1] + "-" + ten_list[ten-2])
        else :
            print(hundred_list[hundred-1] + "-" + ten_list[ten-2] + "-" + one_list[one])
    else :
        print("ERROR")
else :
    print("ERROR")