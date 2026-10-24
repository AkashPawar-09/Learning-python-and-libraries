# for loop


# printing 0 to 5
for i in range(6):
    print(i)

print()



# printing 1 to 5
for i in range(1,6):
    print(i)

print()



# printing even numbers from 1 to 13
for i in range(2,13,2): # start , stop , step
    print(i)    

print()



# prining table of 4
for i in range(1,11):
    print(i*4)

print()



# printing 10 to 1
for i in range(10 , 0 , -1):
    print(i)

print()




# factorial of n
n = 6
ans = 1
for i in range(n,1,-1):
    ans = ans*i
print(ans)


print()

# while loop

# count 1 to 5

count = 1
while(count<=5):
    print(count)
    count = count+1

print()




# count 10 to 5

count = 10
while(count >= 5):
    print(count)
    count = count-1

print()



# print table of 12

num = 1
while(num<=10):
    print(num*12)
    num = num+1

print()



# factorial of n = 6
n = 6
fact = 1
while(n >= 1):
    fact = fact * n
    n = n - 1
print(fact)

print()



# lambda function
square = lambda x: x ** 2
print(square(5)) # 25