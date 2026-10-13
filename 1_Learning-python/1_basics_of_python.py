# printing something...
print("Akash")
print("Laxman")
print("Pawar")


#variables
name = "Akash"
age = 19
cgpa = 7.5


# printing variables
print(name)
print(age)
print(cgpa)


# printing vaiables in sentence
print("Hello , I am ",name)
print("My age is ",age)
print("I have",cgpa,"in MIT AOE college")
print("In short",name,"loves to code at age of",age,"with CGPA",cgpa)


# variables overwrite (changing values of vairiables)
name = "Arya"
age = 20
beauty = 99.999
girl = True
disadvantages = None


# printing every variables
print("A girl named",name,"is",age,"years old and having beauty",beauty,"is girl that is",girl,"with disadvantages are",disadvantages)


# types of variables
print(type(name))
print(type(age))
print(type(beauty))
print(type(girl))
print(type(disadvantages))


# taking user input and print it back
name = input("Enter name : ")
age = int(input("age : "))
percentage = float(input("enter percentage : "))
print("My name is :",name,"AND age is :", age,"with percentage :",percentage,"%")


# operations on string

a,b = 2,3
text = "@"
text2 = "#"
print("Here , multiplying a string with number",text*a*b)
# print("adding string and integer causes error",text+a)
print("addition of 2 string",text+text2)


# number operations
a = 10
b = 13
c = 5
print(a+b*c)


# int * float = float
a = 15
b = 2.0
c = a * b
print(c)


# float * float = float
a = 3.99
b = 5.02
c = a*b
print(c)


# integer division / division using floor
a = 12
b = 5
c = a / b
d = a // b
print(c)
print(d)


# printing 2 numbers at a time
a = 100.2
b = 20
print(a,b)


# remainder operation %
a = 100
b = 8
print(a%b)


# a raised to b operation
a = 5
b = 3
print(a**b)



"""
this is
used for
multiline
comments
"""


# Types of Operators

# 1) Arithmetic Operator: (+, -, *, /, //, %, **)

# 2) Relation / Comparison: (==, !=, >, <, >=, <=)

# 3) Assignment: (=, -=, *=, /=, %=, //=, **=)

# 4) Logical Operator: (not, and, or)

# 5) Membership Operator: (in, not in)

# 6) Identity Operator: (is, is not)

# 7) Bitwise Operator: (&, |, ^)




# conditional statemant

"""
if(condition1):
statement1
elif(condition2):
statement2
else:
statement3
"""


# conditional statements

num1 = int(input("Enter 1st number :"))
num2 = int(input("Enter 2nd number :"))

if(num1 == num2):
    print("Both numbers are equal !!!")
elif (num1 > num2):
    print("1st number is greater than 2nd")
else :
    print("2nd number is greater than 1st")


# finding average of 2 numbers
print("Average of 2 numbers",(num1+num2)/2)

# finding area of reactange
print("Area of rectangle (1st number * 2nd number)",num1*num2)



# String Methods

str1 = "My name is Akash"
str2 = "NOW , I am 19 years old"
print(str1 + ". " + str2)
print("Length of string 1 :",len(str1))
print("Length of string 2 :",len(str2))


# indexing in string
ch1 = str1[0]
ch2 = str1[1]
ch3 = str1[2]


print(ch1)
print(str1[0])

print(str1[ : ])
print(str1[0:7])
print(str1[ :7])
print(str1[8: ])
print(str1[8:15])
print(str1[8:len(str1)])






# important string functions


# strings are immutable -> methods return a NEW string, original stays same

str1 = "My name is Akash"
# index : M0 y1 _2 n3 a4 m5 e6 _7 i8 s9 _10 A11 k12 a13 s14 h15

# case
print(str1.upper()) # MY NAME IS AKASH
print(str1.lower()) # my name is akash
print(str1.capitalize()) # My name is akash
print(str1.title()) # My Name Is Akash


# remove spaces from edges
s = " hello "
print(s.strip()) # hello
print(s.lstrip()) # hello (left only)
print(s.rstrip()) # hello (right only)


# searching
print(str1.find("is")) # 8 (-1 if not found)
print(str1.count("a")) # 2 (a at index 4 and 13, case sensitive)
print(str1.startswith("My")) # True
print(str1.endswith("Akash")) # True


# replace
print(str1.replace("Akash", "Arya")) # My name is Arya


# split and join
words = str1.split() # ['My', 'name', 'is', 'Akash']
print(words)
print("-".join(words)) # My-name-is-Akash
print("a,b,c".split(",")) # ['a', 'b', 'c']


# checking (True / False)
print("Akash".isalpha()) # True (only letters)
print("2024".isdigit()) # True (only digits)
print("Akash19".isalnum()) # True (letters + digits)
print("ABC".isupper()) # True
print("abc".islower()) # True


# formatting
print("My name is {} and age is {}".format("Akash", 19)) # My name is Akash and age is 19
name = "Akash"
age = 19
print(f"My name is {name} and age is {age}") # f-string (most used)


# padding
print("42".zfill(5)) # 00042
print("Akash".center(11, "*")) # ***Akash***