note = input().split(",")
note.pop()
n = int(input())
index = n%7 - 1
print(note[index])