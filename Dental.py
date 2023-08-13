import json

#Dental clinic program to facilitate collecting patient information ..
#### As a Dentist I should be able to do the following :

class Patient: 
    def __init__(self,name:str , age:int , file_number:int  , medical_history:str,chief_complient:str): #collect patient information ..
        self.name=name 
        self.age=age
        self.file_number=file_number
        self.medical_history=medical_history   #medical history or Within normal limits  ..
        self.chief_complient=chief_complient   #from patient words or his parents ..  

class Dental:
    def __init__(self):
        self.load_patients()                  

#save patients 
    def save_patients(self):
        patients_list = []
        for patient in self.patients_list:
            patients_list.append(
                {
                    "name" : patient.name,
                    "age" : patient.age,
                    "file_number" : patient.file_number,
                    "medical_history" : patient.medical_history,
                    "chief_complient" : patient.chief_complient
                }
            )

        with open("patients.txt", "w") as file:
            file.write(json.dumps(patients_list , indent=4)+ "\n")  #Using `indent=4` in JSON formatting to improve the readability . It adds 4 spaces of indentation for each level in the JSON data hierarchy, making it easier to understand and navigate the data when viewed by humans.
#load patients
    def load_patients(self):
        with open("patients.txt", "r") as file:
            self.patients_list = []
            content = file.read()
            patients_list = json.loads(content if len(content) > 0 else "[]")
            for patient in patients_list:
                self.patients_list.append(Patient(patient["name"], patient["age"], patient["file_number"], patient["medical_history"], patient["chief_complient"]))       


    def add_patient(self, patient):       #to add a New patient
        self.patients_list.append(patient) 
        self.save_patients() 

# display all patients:
    def display_all_patients(self):      
        print("All Patients:")
        for patient in self.patients_list:
            print(f"Name: {patient.name}, Age: {patient.age}, file_number: {patient.file_number}, medical_history: {patient.medical_history}, chief_complient: {patient.chief_complient}")

#find patient by file number:       
    def find_patient(self, file_number):
        for patient in self.patients_list:
            if patient.file_number == file_number:
                print("Patient Found:")
                print(f"Name: {patient.name}, Age: {patient.age}, file_number: {patient.file_number}, medical_history: {patient.medical_history}, chief_complient: {patient.chief_complient}")
                return        
        print("Patient not found.")

#remove patient by file number
    def remove_patient(self, file_number):
        for patient in self.patients_list:
            if patient.file_number == file_number:
                self.patients_list.remove(patient)
                print("Patient removed successfully.")
                self.save_patients()
                return
        print("Patient not found.")
