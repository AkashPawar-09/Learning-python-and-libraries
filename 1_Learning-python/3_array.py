# array

lst = [10, 20, 30, 40, 50]
print(lst)


lst.append(60)
print(lst) # [10, 20, 30, 40, 50, 60]


print(lst.pop(), lst) # 60 [10, 20, 30, 40, 50]
print(lst) # [10, 20, 30, 40, 50]


print(lst.pop(1), lst) # 20 [10, 30, 40, 50]
print(lst) # [10, 30, 40, 50]


lst.insert(1, 25)
print(lst) # [10, 25, 30, 40, 50]


del lst[2]
print(lst) # [10, 25, 40, 50]


lst.remove(40)
print(lst) # [10, 25, 50]


print(lst[0]) # 10
print(lst[1]) # 25
print(lst[2]) # 50


print(50 in lst, 99 in lst) # True False


print(len(lst)) # 3