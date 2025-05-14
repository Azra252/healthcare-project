import datetime

patients = []
appointments = []

def add_patient():
    name = input("Enter patient name: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")
    contact = input("Enter contact number: ")
    patient_id = len(patients) + 1
    patients.append({
        'id': patient_id,
        'name': name,
        'age': age,
        'gender': gender,
        'contact': contact
    })
    print(f"Patient {name} added with ID {patient_id}.")

def view_patients():
    if not patients:
        print("No patient records found.")
    for patient in patients:
        print(f"ID: {patient['id']}, Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}, Contact: {patient['contact']}")

def schedule_appointment():
    patient_id_
