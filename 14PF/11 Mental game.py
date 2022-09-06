target = input()
guess = input()
post_list = []
for i in range(len(target)) :
    if target[i] == guess[i] :
        post_list.append(target[i])
char_list = []
for i in target :
    if i in guess :
        char_list.append(i)
new_list = []
for i in char_list :
    if i not in post_list and i not in new_list :
        new_list.append(i)
post_cnt = len(post_list)
new_cnt = len(new_list)
print("{}-{}".format(post_cnt, new_cnt))