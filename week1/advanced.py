# some advanced python conditions and loops 

# break 
x = {
    "a":"x",
    "b":"y",
    "c":"z"
}


for key,value in x.items():
    if key == "b":
        print(value)
        break
else:
        print("not found")


# pass
y = 5
if y>=5:
    pass            # does nothing

#ternary operator
cg = 3.8
remark = "good" if cg>=3.5 else "not so good"
print(remark)

# nested loops
a = int(input())

for i in range(a):
    if i == 0 or i == a-1:
        continue
    else:
        for j in range(a):
            print("*", end="")      # end="" keeps printing on the same line
    print()


# switch
number = int(input())

match number:
    case n if 90 <= n <= 100:
        print("a")
    case n if 80 <= n < 90:
        print("-a")
    case _:
        print("not good enough")


