# try-except block

try:
    x = int(input("enter number "))
    print(5/x)
except ZeroDivisionError:
    print("zero division error")
except ValueError:
    print("invalid input")
finally:
    print("done!")

print()
print()

# user defined error

user = [1,2,3,4]

class InvalidIdError(Exception):
    # raised when given id is invalid
    pass

def verifyLogin(u_id):
    if u_id not in user:
        raise InvalidIdError("invalid user id {u_id}")
    else:
        print("user found")

try:
    verifyLogin(5)
except InvalidIdError as e:
    print("user not found", e)
