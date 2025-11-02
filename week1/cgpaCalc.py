# a python script to calculate cgpa

prev_cg = 0.0           # base value is 0 for new students
prev_credit = 0.0
new_gp = 0.0
new_credit = 0.0
n = 0

print ("\n\n\nenter current cgpa, completed credits and number of course taken this semester")

prev_cg = float(input())
prev_credit = float(input())
n = int(input())

numerator = 0
denominator = 0

# input for each course
for i in range(n):      
    print("course "+ str(i+1) + "\nenter credit")
    x = float(input())
    print("enter grade point")
    y = float(input())
    numerator+= x*y
    denominator+=x

# calculate term gpa
new_gp = numerator/denominator
new_credit = denominator
#calculate overall cgps
new_cg = ((prev_cg*prev_credit)+(new_gp)*new_credit)/(prev_credit+new_credit)

print("your current cgpa is", new_cg)