list = [int(i) for i in input().split()]
post = [int(i) for i in range(len(list))]
i = 0
while len(post) > 1 :
    i = (i+list[i])%len(list)
    post.pop(i)
    list.pop(i)
    if i == len(list) :
        i = 0
print(post[0])