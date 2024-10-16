def update_test(dictionary):
    dictionary.update({'D': 4, 'E': 5, 'F': 6})
    print("Function update(): ", dictionary)

def del_test(dictionary):
    del dictionary['A']
    print("Function del(): ", dictionary)

def clear_test(dictionary):
    dictionary.clear()
    print("Function clear(): ", dictionary)

def keys_test(dictionary):
    print("Function keys(): ", dictionary.keys())

def values_test(dictionary):
    print("Function values(): ", dictionary.values())

def items_test(dictionary):
    print("Function items(): ", dictionary.items())

dictionary = {'A': 1, 'B': 2, 'C': 3}
print("Original dictionary: ", dictionary)

update_test(dictionary.copy())
del_test(dictionary.copy())
clear_test(dictionary.copy())
keys_test(dictionary.copy())
values_test(dictionary.copy())
items_test(dictionary.copy())

