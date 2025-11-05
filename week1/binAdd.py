# a simple binary adder

print("Note keep the length of the numbers same")
a = input("enter first number")
b = input("enter second number")

carry = 0                  
binSum = ""                 # binary sum 

for i in range(len(a)-1,-1,-1):     # inerating from right->left
    b1=int(a[i])
    b2=int(b[i])

    sum = b1+b2+carry
    if sum == 0:                    # adding 2 0's and carry = 0
        binSum+="0"                 # updating the sum
        carry = 0
    elif sum == 1:                  # adding 1 & 0 and carry = 0 
        binSum+="1"
        carry = 0
    elif sum == 2:                  # adding 2 1's and carry = 0
        binSum+="0"
        carry = 1
    elif sum == 3:                  # addign 2 1's and carry = 1
        binSum+="1"
        carry = 1


if carry == 1:                      # handling the last carry
    binSum+="1"

print("sum: ", binSum[::-1])        # reversing the final sum