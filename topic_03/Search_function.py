def sortPosition(list, numder):
    position = 0
    for elem in list:
        if numder > elem:
            position += 1
        else:
            break
    return position

list = [1, 6, 9, 11, 22, 23, 200, 545]
print("List of numbers:", list)

numder = int(input("Enter a new number whose location you want to know: "))
position = sortPosition(list, numder)

if position == 0:
    print("The number will be first")
elif position == len(list):
    print("This numder will be last")
else:
    print(f"This numder will be between {list[position - 1]} and {list[position]}.")

    