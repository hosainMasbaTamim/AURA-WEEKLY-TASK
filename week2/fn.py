# basic functions

# function with out parameters
def oh_start_up():
    print("hello world")

# function with parameter
def add(a,b):               # a,b are parameter
    print(a+b)

add(2,2)                    # calling the function, 2,2 are argument

# function with return
def sub(a,b):
    return(a-b)             # return the value of a-b

print(sub(10,2))            # the function is being called inside  print() as sub just returns the value, not print it

x = sub(5,2)                # the return value is being saved in a variabe and then being print

print(x)


# scope

global_variable = 10

def incriment_by_2(a):
    local_variable = 2
    return a + local_variable

print(global_variable)                  
print(incriment_by_2(global_variable))
#print(local_variable)      # this throws an error as local_varable is defined inside a function and thus can not be accessed from outside


if __name__ == "__main__":  # this ensures when this file is being imported this function calls dosent get automatically called
    oh_start_up()
    add(1,2)
    sub(1,2)
    incriment_by_2(3)