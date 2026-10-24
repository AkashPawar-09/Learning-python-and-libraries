# ---------------------------------------------------------------------------------------------------------------
class Dog:
    species = "Canine"              # Class attribute

    def __init__(self, name, age):
        self.name = name            # Instance attribute
        self.age = age              # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
print(dog1.name) 
print(dog1.species)

# ---------------------------------------------------------------------------------------------------------------
# Buddy
# Canine
# ---------------------------------------------------------------------------------------------------------------

class Student:
    school = "ABC School"   # Class variable

s1 = Student()
s2 = Student()

print(s1.school)
print(s2.school)

# ---------------------------------------------------------------------------------------------------------------
# ABC School
# ABC School
# ---------------------------------------------------------------------------------------------------------------  

class Dog:
    def __init__(self, breed, age, color):
        self.breed = breed
        self.age = age
        self.color = color

    # Behaviors
    def bark(self):
        print(f"{self.breed} says: Woof! Woof!")

    def sleep(self):
        print(f"{self.breed} is sleeping... Zzz")

    def eat(self, food):
        print(f"{self.breed} is eating {food}")

# Creating dog objects
dog1 = Dog("Labrador", 5, "Black")
dog2 = Dog("Beagle", 3, "Brown")

# Accessing attributes
print(dog1.breed)  
print(dog2.age)    

# Using behaviors
dog1.bark()        
dog2.sleep()       
dog1.eat("bone")



""" ---------------------------------------------------------------------------------------------------------------
Labrador
3
Labrador says: Woof! Woof!
Beagle is sleeping... Zzz
Labrador is eating bone
--------------------------------------------------------------------------------------------------------------- """


class CSStudent:
    stream = 'cse'          # Class variable

    def __init__(self, name, roll):
        self.name = name    # Instance variable
        self.roll = roll    # Instance variable

# Creating objects
a = CSStudent('Rose', 1)
b = CSStudent('Nat', 2)

print(a.stream)
print(b.stream)
print(a.name)
print(b.name)



""" ---------------------------------------------------------------------------------------------------------------
cse
cse
Rose
Nat
--------------------------------------------------------------------------------------------------------------- """

a.stream = 'ece'
print(a.stream)
print(b.stream)


""" ---------------------------------------------------------------------------------------------------------------
ece
cse
--------------------------------------------------------------------------------------------------------------- """

CSStudent.stream = 'mech'
print(a.stream)
print(b.stream)

""" ---------------------------------------------------------------------------------------------------------------
ece 
mech 
--------------------------------------------------------------------------------------------------------------- """