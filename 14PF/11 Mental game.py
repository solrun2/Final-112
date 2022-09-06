target = input()
guess = input()
post_cnt = 0
for i in range(len(target)) :
    if target[i] == guess[i] :
        post_cnt += 1
char_cnt = 0
new = ""
for i in target :
    if i not in new :
        new += i
for i in new :
    if i in guess :
        char_cnt += 1

char_cnt -= post_cnt
print("{}-{}".format(post_cnt, char_cnt))