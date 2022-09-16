case = input()
passcase = input()
allCase = len(case)-2
cnt = 0
for i in case[1:-1] :
    if i in passcase :
        cnt += 1
print(cnt)
if allCase != 0 :
    print("{:.2f}".format(cnt/allCase*100))
else :
    print("0.00")