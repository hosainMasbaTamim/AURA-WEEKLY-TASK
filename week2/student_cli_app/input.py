# take inputs for the students

def take_input():

    try:
        full_name = input("enter full name ").strip()
        admission_year = int(input("enter year ").strip())
        admission_session = input("enter session ").strip()
        dept = input("enter department ")

        last_name = full_name.split()[-1]               # extarcting last name
        first_alpha = full_name[0]                      # extracting last alphabet

    except ValueError:
        print("invalid input")
        return None
    except TypeError:
        print("invalid input type")
        return None
    else:
        print("succesfully taken")
        return last_name,first_alpha,admission_year,admission_session,dept