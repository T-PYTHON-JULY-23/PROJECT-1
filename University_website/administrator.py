
#import administrator



list = []

class administrator:
  

    
    def __init__(self, name, id, Statistics, Physics, python ,artificial_intelligence ,Web_development):
        self.name = name
        self.id = id
        self.Statistics = Statistics
        self.Physics = Physics
        self.python = python
        self.artificial_intelligence = artificial_intelligence
        self.Web_development = Web_development
       

       

	# Function to create and append new student
    def add(self, Name, id, marks1, marks2, marks3,marks4,marks5):         
        value_students = administrator(Name, id, marks1, marks2, marks3,marks4,marks5)
        list.append(value_students)

	# Function to display student data
    def display(self, value_students):
        print("Name : ", value_students.name)
        print("id : ", value_students.id)
        print("Statistics : ", value_students.Statistics)
        print("Physics : ", value_students.Physics)
        print("python : ", value_students.python)
        print("artificial intelligence : ", value_students.artificial_intelligence)
        print("Web development : ", value_students.Web_development)
        print("\n")


    # search Function
    def search(self, id):
        for i in range(len(list)):
            if list[i].id== id:
                
                return i
        else:
            return print("student not found")

	# Delete Function
    def delete(self,  id):
        i = data_student.search(id)
        if i!=None:
            del list[i]
            return print("sududent data deleted  successfully")

	# Update Function  
    def update(self, id, sub_1,sub_2, sub_3,sub_4, sub_5): 
        i = data_student.search(id) 
        subject_1 = sub_1
        subject_2 = sub_2
        subject_3 = sub_3
        subject_4 = sub_4
        subject_5 = sub_5
        list[i].Statistics = subject_1
        list[i].Physics = subject_2
        list[i].python = subject_3
        list[i].artificial_intelligence = subject_4
        list[i].Web_development = subject_5

data_student = administrator('', 0, 0, 0, 0, 0 ,0)
