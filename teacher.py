import json
import os
from tabulate import tabulate
from colorama import Fore, Back, Style, init
from student import *
from exam import *
init(autoreset=True)


def add_student(student_name: str, student_password: str, teacher_code) -> None:
    with open('data/students.json', 'r') as students:
       students_dict = json.load(students)

    if search_student(student_name) is None:
        new_id = int(students_dict['students'][-1]['student_id']) + 1

        new_student = {
            "student_name": student_name,
            "student_password": student_password,
            "student_id": new_id,
            "student_exams": []
        }

        students_dict['students'].append(new_student)

        with open('data/students.json', 'w') as students:
            json.dump(students_dict, students, indent=4)
        add_student_to_teacher(student_name, teacher_code)
        print(f"{student_name} is successfully added !")
    else:
        print(f"'{student_name}' is already registered !!")


def add_student_to_teacher(student_name: str, teacher_code: str):
    with open('data/teachers.json', 'r') as teachers:
        teachers_dict = json.load(teachers)

    for teacher in teachers_dict['teachers']:
        if teacher['teacher_code'] == teacher_code:
            teacher['teacher_students'].append(student_name)

    with open('data/teachers.json', 'w') as teachers:
        json.dump(teachers_dict, teachers, indent=4)


def edit_grade(teacher_code: str):
    print("you can only edit the grads of your own student and exams".capitalize())

    teacher = search_teacher(teacher_code)

    for student in teacher['teacher_students']:
        print(f"- {student}")
    while True:
        student_name = input(
            "please enter the name of the student you want to edit the grade for 'in text' or enter '0' exit : ".capitalize())

        student = search_student(student_name)

        if student is not None:
            break
        elif student_name == '0':
            return

    print(f"this are the exams for {student_name}".capitalize())

    student_exams = student['student_exams']

    for i, exam in enumerate(student_exams, 1):
        print(f"[{i}] - {exam['exam_name']} / {exam['exam_grade']}".capitalize())

    while True:
        exam_index = input(
            f"please chose from the exams, what exam you want to edit the grade for {student_name} or enter 'None' to give the student another try to take the exam or '0' to exit  : ".capitalize())

        if exam_index == '0':
            return

        elif exam_index.isdigit():
            exam_index = int(exam_index)

            if exam_index < i+1:
                break
            else:
                print(ValueError,
                      f"{exam_index} is out of your exams boundary".capitalize())
        else:
            print(ValueError, f"{exam_index} is not integer value".capitalize())

    while True:
        new_exam_grade = input(
            f"please enter the new grade for {student_name} out of 100 'in int'or enter 'Q/q' to exit : ".capitalize())
        
        if new_exam_grade == 'None':
            break

        if new_exam_grade == 'q':
            return

        if new_exam_grade.isdigit():
            new_exam_grade = int(new_exam_grade)

            if new_exam_grade <= 100:
                break
            else:
                print(
                    ValueError, f"{exam_index} is more than 100, and 100 is a full mark".capitalize())
        else:
            print(ValueError, f"{exam_index} is not integer value".capitalize())

    assign_grade(student_name, exam_index, None if new_exam_grade == 'None' else new_exam_grade)

    print("new grade assigned, Done !!".capitalize())


def view_students_grades(teacher_code):
    teacher = search_teacher(teacher_code)

    for student in teacher['teacher_students']:
        view_student_exams(student)


def add_exam(teacher_code):
    print("the exam you will adding will be assigned to no student you have to assign them by your self.".capitalize())

    while True:
        exam_name = input(
            "please enter the name of the exam or enter 0 to exit: ".capitalize())
        if exam_name == '0':
            return
        else:
            exam_name_ = exam_name.replace(" ", "_")

            for file_name in os.listdir("Exams"):
                if exam_name_ == file_name[:-5]:
                    print(f"{exam_name} already exist try another one !!".capitalize())
            else:
                exam_data = {
                    "questions": []
                }
                
                with open('data/teachers.json', 'r') as teachers:
                    teachers_dict = json.load(teachers)

                for teacher in teachers_dict['teachers']:
                    if teacher['teacher_code'] == teacher_code:
                        teacher['teacher_exams'].append(exam_name_)

                with open('data/teachers.json', 'w') as teachers:
                    json.dump(teachers_dict, teachers, indent=4)
               

                with open(f"Exams/{exam_name_}.json", 'w') as exams:
                    json.dump(exam_data, exams, indent=4)
                break
    print(f"{exam_name} is added successfully!".capitalize())


def view_students(teacher_code: str) -> None:
    with open('data/teachers.json', 'r') as teachers:
        teachers_dict = json.load(teachers)

    student_list = []

    for teacher in teachers_dict['teachers']:
        if teacher['teacher_code'] == teacher_code:
            for student in teacher['teacher_students']:
                student = search_student(student)
                if student is not None:
                    student_row = [student['student_id'],
                                   student['student_name']]
                    student_list.append(student_row)

    if len(student_list) > 0:
        print("Students Information:")
        print(tabulate(student_list, headers=[
              "ID", "Name"], tablefmt="rounded_outline"))
    else:
        print("No students found for the given teacher code.".capitalize())


def assign_student(teacher_code: str) -> None:
    teacher = search_teacher(teacher_code)
    print("what exam you want to add the student to ?".capitalize())
    for student in teacher['teacher_students']:
        print(f"{student}")

    student_name = input("please enter the student name you want to add exam to : ".capitalize())
    student = search_student(student_name)
    while True:
        if student is not None:
            for exam in teacher['teacher_exams']:
                print(exam)
            
            while True:
                exam_name = input("the name of the exam : ".capitalize())
                if exam_name in teacher['teacher_exams']:
                    break
                elif exam_name == '0':
                    return
                print(f"{exam_name} is not exam from the list try agin or enter '0' to exit".capitalize())

            with open('data/students.json', 'r') as students:
                students_dict: dict = json.load(students)
            
            exam_dict = {
                "exam_name": exam_name,
                "exam_grade": None
            }
            for student in students_dict['students']:
                if student['student_name'] == student_name:
                    student['student_exams'].append(exam_dict)
            break
        else:
            print(f"'{student_name}' is not found")

    with open('data/students.json', 'w') as student:
        json.dump(students_dict, student, indent=4)



def search_teacher(search_key: str | int) -> dict | None:
    with open('data/teachers.json', 'r') as teachers:
        teachers_dict: dict = json.load(teachers)

    for teacher in teachers_dict['teachers']:
        if search_key == teacher['teacher_name'] or search_key == teacher['teacher_code']:
            return teacher
    else:
        return None


def view_exam(teacher_code:str) -> None:
    teacher = search_teacher(teacher_code)

    exam_list = []

    for i, exam in enumerate(teacher['teacher_exams'], 1):
        exam_list.append([i, exam])
    
    print(tabulate(exam_list, headers=['#', 'Exam Title'], tablefmt="rounded_outline"))


def view_teacher_exams(teacher_code) -> None:
    
    teacher = search_teacher(teacher_code)
    exams =teacher['teacher_exams']

    for exam in exams:
        with open(f"Exams/{exam}.json") as exam_file:
            exam_dict = json.load(exam_file)
        table_data = []
        for question in exam_dict.get('questions', []):
            table_data.append([
                question.get('question', ''),
                question.get('correct_answer', ''),
                question.get('answer_duration_min', ''),
                ", ".join(question.get('choices', []))
            ])
        print(f"{exam} exam :")
        print(tabulate(table_data, headers=['Question', 'Correct Answer', 'Answer Duration (min)', 'Choices']))


def add_question(teacher_code:str) -> None:
    teacher = search_teacher(teacher_code)
    print("from the list of exams you can edit : ")
    for i, exam in enumerate(teacher['teacher_exams'], 1):
        print(f"[{i}] - {exam}")
    while True:
        choice = input("please select which exam you want to add question to :")
        if choice.isdigit():
            choice = int(choice)

            if choice <= i:
                exam_name = teacher['teacher_exams'][choice-1]
                count = int(input("how many question you want to add : "))
                i = 1
                while count >0:
                    title = input(f"please enter question {i} title :")
                    choices = input("please enter the choices make sure to include only coma between the choices no spaces and include the correct answer \n  \"e.g.. choise1,choice2,pla pla pla,....\" : ")
                    duration = input("please enter the duration of the question in minuets : ")
                    if not duration.isdigit():
                        print(ValueError, f"{duration} is not an integer value")
                        continue
                    correct_answer = input("pleas enter the correct answer : ")
                    choices = choices.split(",")
                    count -=1
                    i +=1

                new_question = {
                    "question": title,
                    "correct_answer": correct_answer,
                    "answer_duration_min": duration,
                    "choices": choices
                }
                with open(f"Exams/{exam_name}.json",'r+') as file:
                    # First we load existing questions into a dict.
                    file_data = json.load(file)
                    # Join new_data with file_data inside emp_details
                    file_data["questions"].append(new_question)
                    # Sets file's current position at offset.
                    file.seek(0)
                    # convert back to json.
                    json.dump(file_data, file, indent = 4)
                break
            else:
                print(ValueError, f"'{choice}' is not from the choices")
        else:
            print(ValueError, f"{choice} is not an integer value")



def delete_question(teacher_code:str) -> None:
    teacher = search_teacher(teacher_code)

    print("from the list of exams you can edit : ")
    for i, exam in enumerate(teacher['teacher_exams'], 1):
        print(f"[{i}] - {exam}")
    while True:
        choice = input("please select which exam you want to delete question from :")
        if choice.isdigit():
            choice = int(choice)

            if choice < i:
                exam_name = teacher['teacher_exams'][choice-1]
                with open(f"Exams/{exam_name}.json", 'r') as exam:
                    exam_dict = json.load(exam)
                
                questions_titles = []
                for j, question in enumerate(exam_dict['questions'], 1):
                    questions_titles.append([j, question['question']])
                
                print(tabulate(questions_titles, headers=["#", 'Question Title'], tablefmt="rounded_outline"))

                while True:
                    choice1 = input("please select which question you want to delete :")
                    if choice1.isdigit():
                        choice1 = int(choice1)

                        if choice1 < j:
                            delete_question_title = questions_titles[choice1-1][1]

                            for question in exam_dict['questions']:
                                if question['question'] == delete_question_title:
                                    exam_dict['questions'].remove(question)
                            else:
                                with open(f"Exams/{exam_name}.json", 'w') as exam:
                                    json.dump(exam_dict, exam, indent=4)
                            break
                        else:
                            print(ValueError, f"'{choice}' is not from the choices")
                    else:
                        print(ValueError, f"{choice} is not an integer value")

                    break
                break
            else:
                print(ValueError, f"'{choice}' is not from the choices")
        else:
            print(ValueError, f"{choice} is not an integer value")



def check_teacher_code(teacher_code: str) -> dict | None:
    with open("data/teachers.json") as teachers:
        teacher_dict = json.load(teachers)

    for teacher in teacher_dict['teachers']:
        if teacher['teacher_code'] == teacher_code:
            return teacher
    else:
        return None


