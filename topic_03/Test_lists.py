def extend(list):
    list.extend([1, 11])
    print("Function extend(): ", list)

def append(list):
    list.append(99)
    print("Function append(): ", list)

def insert(list):
    list.insert(6, 200)
    print("Function insert(): ", list)

def remove(list):
    list.remove(2)
    print("Function remove(): ", list)

def clear(list):
    list.clear()
    print("Function clear(): ", list)

def sort(list):
    list.sort()
    print("Function sort(): ", list)

def reverse(list):
    list.reverse()
    print("Function reverse(): ", list)

def copy(list):
    copy_list = list.copy()
    print("Function copy(): ", copy_list)

list = [0, 2, 4, 6, 22, 10, 11, 88, 100]
print("Original list: ", list)

extend(list.copy())
append(list.copy())
insert(list.copy())
remove(list.copy())
clear(list.copy())
sort(list.copy())
reverse(list.copy())
copy(list)

