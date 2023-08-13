from Dental import *
from art import *
from colorama import *

print(Fore.BLUE+(text2art("Dental  C linic  program",font='swan')))
print(Style.RESET_ALL)


d=Dental()
while True:
    print("\nDentist Program")
    print("1. Collect Patient Information")
    print("2. Display All Patients")
    print("3. Find Patient by File Number")
    print("4. Remove Patient by File Number")
    print("5. Exit")
    choice = input("select your choice (1-5): ")
    
    if choice == "1":
        name= input("Enter patient Name: ")
        age= input ("Enter patient age: ")
        file_number= input("Enter patient file number (number must be a 7-digit number): ")
        medical_history= input ("Enter patient medical history or Enter 'Within normal limits' ")
        chief_complient=input  ( "Enter patient chief complaint: ")

        New_patient= Patient(name,age,file_number,medical_history,chief_complient) #Patients_list
        print("Patient information collected successfully!")
        d.add_patient(New_patient)
    
    
    elif choice == "2":
        d.display_all_patients()

    
    elif choice == "3":
        try:
            file_number = input("Use the patient's file number: ")
            if len(str(file_number)) != 7:
                raise ValueError("File number must be a 7-digit number.")
            d.find_patient(file_number)
        except ValueError as e:
            print(f"Invalid file number: {e}")
    
    elif choice == "4":
        try:
            file_number = input("Use the patient's file number: ")
            if len(str(file_number)) != 7:
                raise ValueError("File number must be a 7-digit number.")
            d.remove_patient(file_number)
        except ValueError as e:
            print(f"Invalid file number: {e}")    

    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

