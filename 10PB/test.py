t = input().lower()
l = len(t)
count = 0
while True:
  g = input().lower()
  if len(g) == 1:
    if g == '0':
      break
  
    if g in t:
      count += t.count(g)
      t = t.replace(g,'')
      print(t,count)

print(f'{count}/{l}')