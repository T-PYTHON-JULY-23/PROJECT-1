from teacher import *

def main():

    while True:
        choice1 = int(input("hi, are you \n[1] - student \n[2] - teacher \n[0] - to exit the program \nPlease enter your choice : "))
        if choice1.isdigit():
            choice1 = int(choice1)
            
            if choice1 == 1:
                print("you have to be registered by your teacher")
                student_name = input("please enter your Student Fullname : ")
                while True:
                    if not student_name.isdigit() and search_student(student_name) is not None:
                        print(f"Welcome {student_name}, ")
                        break
                    else:
                        student_name = input(f"{student_name} is not registered please enter registered student or enter (0) to start over : ")
                        if student_name.isdigit():
                            if int(student_name) == 0:
                                main()
                        continue

                for chance in range(3, 0, -1):
                    print(f"You have {chance} chances be carefully the system will terminate after your last chance !!")
                    student_password = input(f"please enter your password : ")
                    
                    if check_student_password(student_name, student_password) is not None:
                        print(f"Welcome {student_name},happy to see you well, how can i help you today")
                        break
                        
                else:   
                    main()    
                while True:
                    print("[1] - View your profile\n[2] - View your exams and grades\n[0] - Go back ")
                    choice2 = input(f"{student_name} please enter your choice here : ")
                    if choice2.isdigit():
                        choice2 = int(choice2)
                        if choice2 == 1:
                            view_student_profile(student_name)
                        
                        elif choice2 == 2:
                            view_student_exams(student_name)
                            to_do_exams:list = exams_to_do(student_name)

                            if to_do_exams != None:
                                    while True:
                                        choice3 = input("do you want to start exam (Y/n)? ")

                                        if choice3.lower() == 'y':
                                            for i, exam in enumerate(to_do_exams, 1):
                                                print(f"{i} - {exam['exam_name']}")
                                            exam_choice = input("what exam you want to do : ")
                                    
                                            if exam_choice.isdigit():
                                                exam_choice = int(exam_choice)
                                                
                                                if exam_choice <= i:
                                                    start_exam(student_name, exam_choice)
                                                
                                                else:
                                                    print(ValueError, f"'{exam_choice}' is out of your exams boundary")
                                            
                                            else:
                                                print(ValueError, f"'{exam_choice}' is not integer value")
                                            break

                                        elif choice3.lower() == 'n':
                                            print('ok, as you like but you have to finish your exams asap.')
                                            break

                                        else:
                                            print(ValueError, f"'{choice3}' is not from the choices")
                            else:
                                print("you dont have any remaining exams ")

                        elif choice2 == 0:
                            print(f"thank you, see you again {student_name} .")
                            break
                        else:
                            print(ValueError, f"{choice2} is not from the choices")
                    else:
                        print(ValueError, f"{choice2} is not from the choices")

            elif choice1 == 2:
                print("hi, as a teacher you must have the teacher code,")
                teacher_code = input("please enter your code : ")
                teacher = check_teacher_code(teacher_code)
                if teacher is not None:
                    print(f"Hi Mr.{teacher['teacher_name']}, how i can help you to day ?")

                    while True:
                        print("[1] - View Students actions\n[2] - View Exam actions\n[0] - Go back")
                        choice4 = input("please enter your choice here : ")

                        if choice4.isdigit():
                            choice4 = int(choice4)
                            
                            if choice4 == 1:
                                while True:
                                    print("Students actions :")
                                    print("[1] - Add student\n[2] - View Students info\n[3] - Edit the grade for student\n[4] - View students grade\n[5] - Assign student to do Exam\n[0] - Go back ")
                                    
                                    choice5 = input("please enter your choice here : ") 
                                    
                                    if choice5.isdigit():
                                        choice5 = int(choice5)
                                        
                                        if choice5 == 1:
                                            student_name = input("Please Enter the Student Name : ")
                                            student_password = input("Please Enter the Student PassWord : ")
                                            add_student(student_name, student_password, teacher_code)
                                        
                                        elif choice5 == 2:
                                            view_students(teacher_code)
                                        
                                        elif choice5 == 3:
                                            edit_grade(teacher_code)
                                        
                                        elif choice5 == 4:
                                            view_students_grades(teacher_code)
                                       
                                        elif choice5 == 5:
                                            assign_student(teacher_code)
                                        
                                        elif choice5 == 0:
                                            break

                                        else:
                                            print(ValueError, f"'{choice5}' is not from the choices")
                                    else:
                                        print(ValueError, f"'{choice5}' is not an integer value")
                            elif choice4 == 2:
                                print("Exam Action : ")
                                print("[1] - Add Exam to your exams\n[2] - Add Question To Exam\n[3] - Delete Question From Exam\n[4] - View Exam\n[0] - Go back ")
                                
                                choice6 = input("please enter your choice here :")

                                if choice6.isdigit():
                                    choice6 = int(choice6)

                                    if choice6 == 1:
                                        add_exam(teacher_code)
                                    elif choice6 == 2:
                                        add_question(teacher_code)
                                    elif choice6 == 3:
                                        delete_question(teacher_code)
                                    elif choice6 == 4:
                                        view_exam(teacher_code)
                                        view_teacher_exams(teacher_code)
                                    elif choice6 == 0:
                                        break
                                    else:
                                        print(ValueError, f"{choice6} is not from the choices")
                                else:
                                    print(ValueError, f"{choice6} is not an integer value")

                            elif choice4 == 0:
                                break
                            else:
                                print(ValueError, f"{choice4} is not from the choices")
                        else:
                            print(ValueError, f"{choice4} is not an integer value")
            elif choice1 == 0:
                return
            else:
                print(ValueError, f"{choice1} is not an integer value")
        else: 
            print(ValueError, f"{choice1} is not from the choices")


main()