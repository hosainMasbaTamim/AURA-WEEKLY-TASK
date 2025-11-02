# variables and data types

# primitive
a = "a is a variable"   # string
b = 5                   # int
c = 2.4                 # float
d = True                # boolean  

# non-primitive
x = [1,2,3]             # list
y = (a,b,c)             # tuple
z = {                      
    "a":2,
    "b":4
}                       # dictionary

print(a,b,c,d,x,y,z)

# loops

# for loop
for i in range(5):      # looping through 0,1,2,3,4
    print(i)

# while loop
while b < 10:           # loopging through 5,6,7,8,9
    print(b)
    b+=1

# conditions
b = 2*5
c = 10
if b > c :
    print("b is  bigger")
elif b < c :
    print("c is bigger")
else :
    print("b c equal")

