money = input()
check = money
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',',','.']
ans = ''
back = money[money.find('.')+1:]
if money.count('.') > 1 or (len(back) > 2 and money.count('.') == 1): #จำนวน . กับ หลักหลัง .
  ans = "ERROR"
for i in money: #เช็คเลข
  if i not in num:
    ans = "ERROR"
    break

if ',' in money:
  i=0
  while i < len(check): #24,134
    if check.find(',') > 4:
      ans = "ERROR"
      break
    elif check.count(',') == 0:
      if len(check) > 3:
        ans = "ERROR"
        break
    else:
      check = check[check.find(',')+1:len(check)]
    i += 1
if ans == "ERROR":
  print(ans)
else:
  money = money.replace(',' , '')
  if '.' in money:
    money = float(money) + 1
    print("{:.2f}".format(money))
  else:
    money = int(money) +1 
    print(money)
