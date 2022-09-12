idx = [0]*11
og_list = []
for i in range(20):
  n = int(input(f"Enter score: "))
  if 0 <= n <= 10:
    og_list.append(n)
    idx[n] += 1
  else:
    print("Score is out of range.")
    continue
print("-----")
print("Original list:")
print(og_list)
print("Mode of scores:")

max_value = max(idx) - 1
max_list = []
for c in range(len(idx)):
    if idx[c] > max_value:
        max_list.append(c)
for c in max_list:
    print(c)