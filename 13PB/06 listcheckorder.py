def check_list(list):
    n = list[0]
    check = True
    for i in list :
        if i != n :
            check = False
            break
    return check

def check_order(list):
    if list == [] :
        print("The list is empty.")
    elif check_list(list) :
        print("The list is in non-increasing and non-decreasing order.")
    elif list == sorted(list):
        print("The list is in non-decreasing order.")
    elif list == sorted(list, reverse=True):
        print("The list is in non-increasing order.")
    else:
        print("The list is in random order.")

list = []
while True :
    n = int(input("Enter a number (-1 to end): "))
    if n == -1 :
        break
    if n < 0 or n > 100 :
        print("Number is out of range.")
        continue
    list.append(n)
print("-----\nOriginal list:")
print(list)
check_order(list)