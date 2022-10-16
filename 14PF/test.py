def check_order(l):
  res = 'tesdt'
  if l == []:
    res = 'The list is empty.'
  else:
    c = 1
    for i in l:
      if l[0] == i and c == 1:
        res = 'The list is in non-increasing and non-decreasing order.'
      else:
        c = 2
        if l[0] > i:
          res = 'The list is in non-increasing order.'
        elif l[0] < i:
          res = 'The list is in non-decreasing order.'
        else:
          res = 'The list is in random order.'
          break

  return res

ls = []
while True:
  n = int(input('Enter a number (-1 to end): '))
  if n == -1:
    break
  if n < 0 or n > 100:
    print('Number is out of range.')
  else:
    ls.append(n)

print(f'-----\nOriginal list:\n{ls}')
print(check_order(ls))