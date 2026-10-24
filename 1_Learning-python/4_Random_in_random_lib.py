import random
# ------------------------------------------------------------------------------------------------------

a = [1, 2, 3, 4, 5, 6]          
print(random.choice(a))             # choose eveeytime different

s = "geeks"
print(random.choice(s))

tup = (1, 2, 3, 4, 5)
print(random.choice(tup))

# ------------------------------------------------------------------------------------------------------

# random.randint() method is used to generate random integers between the given range.
# Syntax:
# randint(start, end)

# ------------------------------------------------------------------------------------------------------

r1 = random.randint(5, 15)
print(r1)                           # r1 is a random number between 5 and 15.

r2 = random.randint(-10, -2)
print(r2)                           # r2 is a random number between -10 and -2.


# ------------------------------------------------------------------------------------------------------

# Generate a Random Float Between 0 and 1
# A random.random() method is used to generate random floats between 0.0 to 1.

# Syntax:
# random.random()

from random import random
print(random())

# ------------------------------------------------------------------------------------------------------

# Select Multiple Unique Random Items
# this example demonstrates the use of sample() to pick multiple items from sequences without repeating.

# Syntax:
# random.sample(sequence, length)

from random import sample

a = [1, 2, 3, 4, 5]     # list
print(sample(a,3))

b = (4, 5, 6, 7, 8)     # tuple
print(sample(b,3))

c = "45678"             # string
print(sample(c,3))                      # sample() returns a list of unique random elements from the input sequence.
