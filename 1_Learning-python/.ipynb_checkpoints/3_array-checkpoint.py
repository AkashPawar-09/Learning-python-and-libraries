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


lst.sort()
print(lst)    # [10, 25, 50]


lst.reverse()
print(lst)    # [50, 25, 10]


numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)


nums = [5,6,7,8,9,10,11,12,13,14]
x = 13
idx = 0

for i in nums :
    if i == x :
        print("target is found at : ",idx)
        break
    idx = idx +1 


# What is a Set?
# A set is an unordered collection of unique elements

my_set = {1, 2, 2, 2, 3}
print(my_set)               # {1, 2, 3}
print(type(my_set))         # <class 'set'>
print(len(my_set))          # 3
empty_set = set()


# Set Characteristics
# 1. Sets can only have unique elements.
# 2. They are unordered - no indexing or slicing.
# 3. They are mutable - we can add or remove elements.
# 4. Set elements must be immutable (like strings, numbers, tuples).


# Set Methods
# Let’s have a look at some of the important set methods:
# 1. add(val) - adds an element to set
# 2. remove(val) - removes an element (raises error if not found)
# 3. clear(val) - removes all elements
# 4. pop() - removes and returns a random element (since sets are unordered)
# 5. s1.union(s2) - returns new union (union is collection of all unique values in both sets)
# 6. s1.ntersection(s2) - returns new union (intersection is collection of all common&
# uniquevalues inbothsets)