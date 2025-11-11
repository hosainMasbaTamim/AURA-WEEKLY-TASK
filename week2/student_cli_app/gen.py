import input as ip
import errors as er

session = {
    "fall": 3,
    "summer": 2,
    "spring": 1
}

department = {
    "cse": "011",
    "ds": "015"
}

programm = {
    "cse": "bscse",
    "ds": "bsds"
}

def verify_session(ses):
    try:
        ses_lower = ses.lower()
        if ses_lower not in session:
            raise er.NotValidSession(f"invalid session: {ses}")
        return session[ses_lower]
    except er.BaseError as e:
        print("error", e)
        return None


def verify_department(dept):
    try:
        dept_lower = dept.lower()
        if dept_lower not in department:
            raise er.NotValidDepartment(f"invalid department: {dept}")
        return department[dept_lower]
    except er.BaseError as e:
        print("error", e)
        return None

def gen_student_id(dept_id, year, session_number, unique_identifier):
    return str(dept_id) + str(year)[2:] + str(session_number) + str(unique_identifier)


def gen_student_mail(first_alpha, last_name, id, dept):
    return first_alpha + last_name + str(id)[3:] + "@" + programm[dept.lower()] + ".uiu.ac.bd"
