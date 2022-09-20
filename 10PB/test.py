r = input()
a = input()

count = 0
for i in list(r):
  if i in a:
    count += 1

  elif '-' in r:
    pass
    

res = (count * 100) / (len(r) - 2)
print(f'{count}\n{res:.2f}')