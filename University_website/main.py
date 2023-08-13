from administrator import *
from art import *
    
while True:
 try:
    
        print(text2art("\n Welcome To Student Management System","fancy63	 "))
        print(text2art("\n1.administrator page \n2.Student page\n3.Exit ","fancy62"))
        
        start_up = int(input("Enter your choose:"))
    
        if start_up == 1:
            
            while True:
                print(text2art("\n1.add Student data\n2.Display Student data\n3.search data of a Student\n4.Delete data of Student\n5.Update Student data\n6.back to the main page ","smallcaps2"))

                choose = int(input("Enter your choose:"))
                if(choose == 1):
                    id = int(input ("enter student id :"))
                    for i in range(len(list)):
                            if(list[i].id == id):
                                        print("student aleady exit")
                                        break
                        
                    else:
                        name = input(" enter student name : ")
                    while True:
                        try:
                            subject_1 = int(input("enter student marks in Statistics :"))
                            subject_2 = int(input(" enter student marks in Physics : "))
                            subject_3 = int(input("enter student marks in Python :"))
                            subject_4 = int(input(" enter student marks in artificial intelligence : "))
                            subject_5 = int(input(" enter student marks in Web development  : "))
                        
                            assert 1 <= subject_1 <= 100
                            assert 1 <= subject_2 <= 100
                            assert 1 <= subject_3 <= 100
                            assert 1 <= subject_4 <= 100
                            assert 1 <= subject_5 <= 100
                            break
                        except Exception as e:
                            print("Input must be an integer between 1 and 100.",e.__class__)
                    data_student.add(name, id, subject_1, subject_2, subject_3,subject_4,subject_5)
                    print("student add successfully ")
                                        

                elif(choose == 2):
                    print("\n")
                    print("\nList of Students\n")
                    for i in range(len(list)):
                        data_student.display(list[i])

                elif(choose == 3):
                    id= int(input("enter student id that you are looking for : "))
                    f=data_student.search(id)
                    if f !=None:
                        data_student.display(list[f])
                    
                                

                elif(choose == 4):
                    id =int(input("inter student id to delete : "))
                    data_student.delete(id)
                    
                    
                

                elif(choose == 5):
                    id= int(input("enter student id you want to update : "))
                    f=data_student.search(id)
                    if f !=None:
                        subject_1 = input("enter marks for Statistics : ")
                        subject_2 = input("enter marks for Physics : ")
                        subject_3 = input("enter student Python :")
                        subject_4 = input(" enter student artificial intelligence : ")
                        subject_5 = input(" enter student Web development  : ")
                        data_student.update(id, subject_1, subject_2, subject_3, subject_4, subject_5)
                        print(len(list))
                        print("List after updation")
                        for i in range(len(list)):
                             data_student.display(list[i])
                            
                    
                    
                    
                    
                        


                elif(choose==6):
                    print("back to the main page  !")
                    break 
                else:
                 print(" inter number from 1-5 or press 6 exit")
        elif start_up == 2:
            while True:
                print(text2art("\n1.Signed in  \n2.back to the mian page  ","smallcaps2"))
                choose = int(input("Enter your choose:"))
                
                if(choose == 1):
                    id = int(input ("enter your id :"))
                    hold_data=data_student.search(id)
                    if hold_data !=None:
                     while True:
                        name_student= list[hold_data].name
                        print(text2art(f"\nwelcome to your page {name_student}","smallcaps2"))
                        print(text2art("\n1.display your data  \n2.calculat your GPA \n3.delete your account \n4.Signed out ","smallcaps2"))
                        choose=int(input("Enter your your choose:"))
                        if choose==1:
                                data_student.display(list[hold_data])
                        elif choose == 2:
                                sub_1=list[hold_data].Statistics 
                                sub_2=list[hold_data].Physics 
                                sub_3=list[hold_data].python 
                                sub_4=list[hold_data].artificial_intelligence 
                                sub_5=list[hold_data].Web_development 

                                # lambda function 
                                GPA_calculater= lambda sub_1,sub_2,sub_3,sub_4,sub_5 : (sub_1+sub_2+sub_3+sub_4+sub_5)/100

                                print(f'your GPA is : {GPA_calculater(sub_1, sub_2,sub_3,sub_4,sub_5)}')
                                
                        elif choose == 3:
                                data_student.delete(id)
                                print("your account have been deleted ")
                                break
                        elif choose == 4:
                                print("Signed out successfully")
                                break
                        else:
                                print("please selcet only the numbers from the list ")
                elif(choose == 2):
                 break
        elif start_up == 3:
            print(text2art("\n think you for using our website","full_width"))
            
            break
        else:
            print("please selcet only the numbers from the list ")
 except Exception as e:
     print("something went wrong", e.__class__)
     

            
                
                
