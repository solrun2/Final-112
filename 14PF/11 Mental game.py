target = input().lower()
guess = input().lower()
position = []
new_target = ""
new_guess = ""
for i in range(len(target)) :
    if target[i] == guess[i] :
        position.append(target[i])
    else :
        new_target += target[i]
        new_guess += guess[i]
character = []
for i in new_guess :
    if i in new_target :
        character.append(i)
        new_target = new_target.replace(i,"",1)

print("{}-{}".format(len(position),len(character)))