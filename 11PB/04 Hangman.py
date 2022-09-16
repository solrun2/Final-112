text = input()
allLen = len(text)
while True :
    guess = input()
    if guess == "0" :
        break
    if guess not in text :
        text = text.replace(guess, "")
restLen = allLen - len(text)
print("{}/{}".format(restLen, allLen))