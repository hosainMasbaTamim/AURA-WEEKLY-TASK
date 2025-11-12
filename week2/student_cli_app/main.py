import gen
import input as ip
import errors as er

last_name, first_alpha, yr, ses, dept = ip.take_input()

unique_identifier = "0231"

try:
    dept_id = gen.verify_department(dept)
    session_no = gen.verify_session(ses)
    s_id = gen.gen_student_id(dept_id,yr,session_no,unique_identifier)
    s_mail = gen.gen_student_mail(first_alpha,last_name,s_id,dept)
except er.BaseError as e:
    print("error",e)

print(f"ID: {s_id}, mail: {s_mail}")

