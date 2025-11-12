# this file is for input taking
def take_input():
    while True:
        try:
            full_name = input("enter full name: ").strip()
            if not full_name.replace(" ", "").isalpha():
                raise ValueError("full name must contain only letters")

            admission_year_input = input("enter year: ").strip()
            if not admission_year_input.isdigit():
                raise ValueError("year must be a number")
            admission_year = int(admission_year_input)

            admission_session = input("enter session: ").strip()
            if not admission_session.isalpha():
                raise ValueError("session must be letters only")

            dept = input("enter department: ").strip()
            if not dept.isalpha():
                raise ValueError("department must be letters only")

            last_name = full_name.split()[-1]
            first_alpha = full_name[0]

        except ValueError as e:
            print("invalid input:", e)
            continue
        else:
            print("succesfully taken")
            return last_name, first_alpha, admission_year, admission_session, dept
