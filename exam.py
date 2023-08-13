import random
import time
import json
from colorama import Fore, Back, Style, init
init(autoreset=True)

def load_questions(student_name: str, exam_index: int) -> list:
    '''in this function i will load the data from questions file and return it as list of question'''
    with open('data/students.json', 'r') as students:
        student_dict = json.load(students)
    not_finished_exams = []
    for student in student_dict['students']:
        if student['student_name'] == student_name:
            for exam in student['student_exams']:
                if exam['exam_grade'] is None:
                    not_finished_exams.append(exam['exam_name'])
            break

    exam_name = not_finished_exams[exam_index - 1]

    with open(f'Exams/{exam_name}.json') as file:
        data = json.load(file)
    # here i want to shuffle the question, so every time we play the order of the questions will be different.
    random.shuffle(data["questions"])
    return [{"question": q['question'], "choices": q['choices'], "correct_answer": q['correct_answer'], "answer_duration_min": q['answer_duration_min']} for q in data['questions']]


def assign_grade(student_name: str, exam_index: int, new_exam_grade: int):
    with open('data/students.json', 'r') as students:
        student_dict = json.load(students)

    to_do_exams = []
    for student in student_dict['students']:
        if student['student_name'] == student_name:
            for i, exam in enumerate(student['student_exams']):
                if i == int(exam_index) - 1:
                    student['student_exams'][i]['exam_grade'] = new_exam_grade

    with open('data/students.json', 'w') as students:
        students.seek(0)
        json.dump(student_dict, students, indent=4)


def start_exam(student_name: str, exam_index: int) -> None:
    '''here the exam start and will set a score for the student and he will see how much he scored at the end'''
    questions = load_questions(student_name, exam_index)

    score = 0

    print("ok, let's start...")
    for i, question in enumerate(questions, 1):
        print("-"*50)
        print(f"Q{i}) {question['question']}")

        for i, choice in enumerate(question['choices'], 1):
            print(f"{i} - {choice}")

        start_time = time.time()

        user_answer = int(input("your answer (1, 2 or 3 ..) : "))

        end_time = time.time()
        elapsed_time = end_time - start_time
        

        if question['choices'].index(question['correct_answer']) + 1 == user_answer:
            if question['answer_duration_min']*60 >= elapsed_time:
                print(Fore.GREEN + "Correct !! +1")
                score += 1
            else:
                print(Fore.RED + F"You lost this point !!! the time is out'")
        else:
            print(
                Fore.RED + F"You lost this point !!! the correct answer was '{question['correct_answer']}'")

    print(Fore.CYAN + f"Good work you gain {score} / {len(questions)}")

    score = round(score/len(questions) * 100)

    assign_grade(student_name, exam_index, score)
