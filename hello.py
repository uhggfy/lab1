def add_student(name, age):
    return f"Sinh viên: {name}, Tuổi: {age}"


def show_student(name, age, major):
    print("===== THÔNG TIN SINH VIÊN =====")
    print(f"Họ tên: {name}")
    print(f"Tuổi: {age}")
    print(f"Ngành học: {major}")


student_name = "Nguyen Van A"
student_age = 20
student_major = "Cong nghe thong tin"

print(add_student(student_name, student_age))
show_student(student_name, student_age, student_major)