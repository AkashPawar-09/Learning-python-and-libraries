import math 

print(math.e)
# 2.718281828459045

print(math.pi)
# 3.141592653589793

print (math.nan)
# nan


# ------------------------------------------------------------------------------------------------------

a = 2.45

print("the floor value of a is :",math.floor(a))    # 2
print("the ceil value of a is :",math.ceil(a))      # 3

# ------------------------------------------------------------------------------------------------------

a = 6 
print("factorial of a is :" , math.factorial(a))    # 720

print("The factorial of 5 is : ", end="")
print(math.factorial(a))

# ------------------------------------------------------------------------------------------------------

a = 10 
b = 5 

print("GCD of a and b is :" , math.gcd(a,b))        # 5

# ------------------------------------------------------------------------------------------------------

a = -10
print ("The absolute value of -10 is : ", end="") 
print (math.fabs(a))                                # 10

# ------------------------------------------------------------------------------------------------------

print ("The value of 3**4 is : ",end="")            # 3 raised to 4
print (pow(3,4))                                    # 81

# ------------------------------------------------------------------------------------------------------

print ("The value of log 2 with base 3 is : ", end="") 
print (math.log(2,3)) 
print ("The value of log2 of 16 is : ", end="") 
print (math.log2(16)) 
print ("The value of log10 of 10000 is : ", end="") 
print (math.log10(10000))

"""     OUTPUT 
The value of log 2 with base 3 is : 0.6309297535714574
The value of log2 of 16 is : 4.0
The value of log10 of 10000 is : 4.0
"""
# ------------------------------------------------------------------------------------------------------

print(math.sqrt(0))         # 0.0
print(math.sqrt(4))         # 2.0
print(math.sqrt(3.5))       # 1.8708286933869707

print(math.floor(math.sqrt(3)))         # 1
print(math.floor(math.sqrt(4)))         # 2
print(math.floor(math.sqrt(5)))         # 2

# ------------------------------------------------------------------------------------------------------

a = math.pi/6
print ("The value of sine of pi/6 is : ", end="") 
print (math.sin(a)) 
print ("The value of cosine of pi/6 is : ", end="") 
print (math.cos(a)) 
print ("The value of tangent of pi/6 is : ", end="") 
print (math.tan(a))

"""
The value of sine of pi/6 is : 0.49999999999999994
The value of cosine of pi/6 is : 0.8660254037844387
The value of tangent of pi/6 is : 0.5773502691896257
"""

# ------------------------------------------------------------------------------------------------------