import json

#program for dental public health to facilitate collecting patient information 
class Patient: 
    def __init__(self,name:str , age:int , file_number:int  , medical_history:str,chief_complient:str):
        self.name=name 
        self.age=age
        self.file_number=file_number
        self.medical_history=medical_history   #medical history or Within normal limits
        self.chief_complient=chief_complient   #from patient words or his parents ..  
         
class Dental:
    def __init__(self):
        self.load_patients()
      
    def load_patients(self):
        with open("patients.txt", "r") as file:
            self.patients_list = []
            content = file.readline()
            patients_list = json.loads(content if len(content) > 0 else "[]")
            for patient in patients_list:
                self.patients_list.append(Patient(patient["name"], patient["age"], patient["file_number"], patient["medical_history"], patient["chief_complient"]))       
    
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
            file.write(json.dumps(patients_list)+ "\n")
    
    def add_patient(self, patient):
        self.patients_list.append(patient) 
        self.save_patients() 
        
    def display_all_patients(self):
        print("All Patients:")
        for patient in self.patients_list:
            print(f"Name: {patient.name}, Age: {patient.age}, file_number: {patient.file_number}, medical_history: {patient.medical_history}, chief_complient: {patient.chief_complient}")
    
    #find patient by file number       
    def find_patient(self, file_number):
        for patient in self.patients_list:
            if patient.file_number == file_number:
                print("Patient Found:")
                print(f"Name: {patient.name}, Age: {patient.age}, file_number: {patient.file_number}, medical_history: {patient.medical_history}, chief_complient: {patient.chief_complient}")
                return        
        print("Patient not found.")
    
    #find patient by file number
    def remove_patient(self, file_number):
        for patient in self.patients_list:
            if patient.file_number == file_number:
                self.patients_list.remove(patient)
                print("Patient removed successfully.")
                self.save_patients()
                return
        print("Patient not found.")
        
        