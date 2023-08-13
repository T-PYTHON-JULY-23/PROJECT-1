import json
from tabulate import tabulate


# class Student:

#     def __init__(self, student_name: str) -> None:
#         self.student_name = student_name
#         self.exams = []

def search_student(search_key: str | int) -> dict | None:

    with open('data/students.json') as students:
        students_dict: dict = json.load(students)

    if isinstance(search_key, int):
        for student in students_dict['students']:
            if search_key == student['student_id']:
                return student
        else:
            return None

    elif isinstance(search_key, str):
        for student in students_dict['students']:
            if search_key.lower() == student['student_name']:
                return student
        else:
            return None

def check_student_password(student_name: str, student_password: str) -> dict | None:
    with open("data/students.json") as students:
        students_dict: dict = json.load(students)

        for student in students_dict["students"]:
            if student["student_name"] == student_name.lower() and student["student_password"] == student_password:
                return student
        else:
            return None

def view_student_profile(student_name: str):
    student = search_student(student_name)

    student_name = student['student_name']
    student_id = student['student_id']

    student_list = [[student_id, student_name]]

    print("Student Information:")
    print(tabulate(student_list, headers=[
          "ID", "Name"], tablefmt="rounded_outline"))


def view_student_exams(student_name: str):
    student = search_student(student_name)

    exam_list = []

    for exam in student['student_exams']:
        exam_name = exam['exam_name']
        exam_grade = exam['exam_grade'] if exam['exam_grade'] is not None else 'not-taken'
        exam_list.append([exam_name, exam_grade])

    print(f"{student['student_name']} Grades Information:")
    print(tabulate(exam_list, headers=[
          "Exam", "Grade %"], tablefmt="rounded_grid"))



def exams_to_do(student_name: str) -> list | None:
    student = search_student(student_name)

    to_do_exams = []

    for exam in student['student_exams']:
        if exam['exam_grade'] is None:
            to_do_exams.append(exam)

    return to_do_exams if to_do_exams != [] else None
