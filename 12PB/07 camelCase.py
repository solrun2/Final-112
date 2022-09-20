s = input().strip()
for i in "-=_.$" :
    s = s.replace(i,".")
s = s.strip(".").split(".")
print(s[0].lower() + "".join([i.capitalize() for i in s[1:]]))