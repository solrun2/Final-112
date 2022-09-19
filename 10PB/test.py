t = input().lower()
ls = list(t)
count = 0
while True:
  g = input().lower()
  if len(g) == 1:
    if g == '0':
      break
  
    elif g in ls:
      if ls.count(g) > 1:
        count += ls.count(g)
        while g in ls:  
          ls.remove(g)
      elif ls.count(g) == 1:
        count += 1

print(f'{count}/{len(t)}')