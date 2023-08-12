def save_patients_to_file(self, filename):
        patient_data = []
        for patient in self.patients:
            patient_data.append({
                "Name": patient.Name,
                "Age": patient.age,
                "File Number": patient.file_number,
                "Medical History": patient.medical_history,
                "Chief Complaint": patient.chief_complaint
            })
        
        with open(filename, "w") as file:
            json.dump(patient_data, file, indent=4)
        
        print("Patients saved to file.")

def load_patients_from_file(self, filename):
        with open(filename, "r") as file:
            patient_data = json.load(file)
        
        self.patients = []
        for data in patient_data:
            patient = Patient(data["Name"], data["Age"], data["File Number"], data["Medical History"], data["Chief Complaint"])
            self.add_patient(patient)
        
        print("Patients loaded from file.")
