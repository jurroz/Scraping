# Data Types
# # Int
23737
-65454

# Float - If you see a decimal point mostlikely a float.
2723.0
61.31
-264.525

# String
'hello'
"hello"

# Bool
True 1
False 0

# Output and Printing
print('blah blah blah')
print(4.5, "hello")
print("hello", 'end', 87, False, end='\n') # or a pip end="|"

# Variables
hello = 'jose'
world = 'world'
world = hello
print(hello, world)

hello_world = 

# User input
name = input('Name: ')
age = input('Age: ')
print('Hello', name, 'you are', age, 'years old')

# Arithmetic Operators
x = 9
y = 3
results = x + y # or convert to a int int(x / y) or multiple same ( x % y) * 2
print(results)

B Bracket
E Exponens
D Division
M Multiplication
A addition
S subtraction

# input example
num = input('Number: ') --> String
print(int(num) - 5) # or use a (float(num) - 5)

# String method
hello = 'hello'
print(type(hello)) # class string

hello = 'hello'.upper() # upper case 
print(hello) # or print(hello.upper()) can also user .lower .capptalize or count('ll') <-- will count ll

# Conditional Operators

== 
!=
<=
>=
<
>

x = "hello"
y = 'hello' #'heLl0'
print(x != y)
# false are the same
# true are the same

print('a' > 'Z')
True
print(ord('Z')) # ordenal = 90


# string multiplication and 
x = 'hello'
y = 'yes'
print(x * y)
#helloyes <--


# chained conditionals - combining mutiple conditional to creat a larger condition
x = 7
y = 8
z = 0
results1 = x == y
results2 = y > x
results3 = z - 2 < x + 2

results4 = results1 or results2 or results3 # if one of them is true output true both wrong false
results4 = results1 or results2 or not results3 # the not will do the oppesite 
results4 = results1 or results2 or and results3 # and  what sin the left hand side and right hand side

# if else elif - allows us to check something accors or condition is true do something specific.
x = input('Name: ')

if x == 'Tim'"
    print('You are great!')
elif x == 'Joe':
    print('Bye Joe')
elif x == 'Sara':
    print('Random')
else:
    print('NO')

# list and tuples - can store different elements and collection
x = [4, True, 'hi']
y = 'hi'
x.append('hello') # adds to the list
x.extend([4,3,4,5,5,6,6,6,]) # takes all of the elements and extends it end of the list
print(len(x), len(y) #Len us to get Leght of something

print(x.pop(0)) # remove starts 0 then 1 2 3 = this removes 4
print(x[1]) # this will access element is "true"


# tuple
x = (0,0,2,2)
print(x[0])
x = [[], (), [[], [], [3,4,5,]]]

# for loops  -  start, stop , step
for i in range(1,10):
    print(i)

for i in [3,4,5,6,6,4,]:  # loops with list
    print(i)

x = [3,4,5,24,2]
for i in range(len(x)):
    print(x[i])

x = [3,4,5,24,2]
for i, element in enumerate(x):
    print(i, element)

# while loops