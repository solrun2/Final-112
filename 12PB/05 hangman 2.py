target = input()
ans = ["-"]*len(target)
while True :
    guess = input()
    if guess == "0" :
        break
    if guess in target :
        for i in range(len(target)) :
            if target[i] == guess :
                ans[i] = guess
print("".join(ans))