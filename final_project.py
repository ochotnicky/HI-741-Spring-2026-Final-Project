# health system user interface 

import csv
import random
from datetime import datetime, timedelta

NUM_PATIENTS = 200
NUM_PROVIDERS = 20
NUM_ENCOUNTERS = 400
NUM_PROCEDURES = 250
NUM_NOTES = 350

random.seed(42)


def generate_credentials():
    rows = [
        ["alice", "pass123", "clinician"],
        ["brandon", "pass124", "clinician"],
        ["carmen", "pass125", "clinician"],
        ["nina", "pass201", "nurse"],
        ["omar", "pass202", "nurse"],
        ["paige", "pass203", "nurse"],
        ["dave", "pass000", "admin"],
        ["erin", "admin456", "admin"],
        ["frank", "admin789", "admin"],
        ["carol", "pass789", "management"],
        ["mia", "mgmt456", "management"],
        ["sam", "mgmt789", "management"],
    ]

    with open("credentials.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["username", "password", "role"])
        writer.writerows(rows)


def generate_patients():
    genders = ["Male", "Female", "Non-binary"]
    rows = []

    for i in range(NUM_PATIENTS):
        patient = [
            f"P{i+1}",
            random.randint(18, 90),
            random.choice(genders),
            round(random.uniform(18, 40), 1),
            "" if random.random() < 0.1 else round(random.uniform(4.5, 10.0), 1),
            random.randint(100, 170),
            random.randint(60, 100),
            random.choice([True, False]),
        ]
        rows.append(patient)

    with open("patients.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "patient_id", "age", "gender",
            "bmi", "a1c", "bp_sys", "bp_dia", "smoking"
        ])
        writer.writerows(rows)


def generate_providers():
    specialties = [
        "Cardiology",
        "Primary Care",
        "Endocrinology",
        "Pulmonology",
        "Oncology",
        "Pediatric",
        "Emergency Medicine",
    ]

    rows = []

    for i in range(NUM_PROVIDERS):
        rows.append([
            f"PR{i+1}",
            f"Dr_{i+1}",
            random.choice(specialties),
            f"D{random.randint(1, 4)}",
        ])

    with open("providers.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "provider_id",
            "name",
            "specialty",
            "department_id",
        ])
        writer.writerows(rows)


def generate_departments():
    departments = [
        ("D1", "Cardiology", "Building A"),
        ("D2", "Primary Care", "Building B"),
        ("D3", "Endocrinology", "Building C"),
        ("D4", "Pulmonology", "Building D"),
    ]

    with open("departments.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "department_id",
            "name",
            "location",
        ])
        writer.writerows(departments)


def generate_encounters():
    encounter_types = ["Outpatient", "Inpatient", "Emergency"]
    rows = []
    for i in range(NUM_ENCOUNTERS):
        date = datetime.today() - timedelta(days=random.randint(0, 365))

        patient_id = f"P{random.randint(1, NUM_PATIENTS)}"
        provider_id = f"PR{random.randint(1, NUM_PROVIDERS)}"
        department_id = f"D{random.randint(1, 4)}"

        rows.append([
            f"E{i+1}",
            patient_id,
            provider_id,
            department_id,
            date.strftime("%Y-%m-%d"),
            random.choice(encounter_types),
        ])

    with open("encounters.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "encounter_id",
            "patient_id",
            "provider_id",
            "department_id",
            "encounter_date",
            "encounter_type",
        ])
        writer.writerows(rows)

    return rows


def generate_procedures(encounters):
    procedure_catalog = [
        ("93000", "Electrocardiogram"),
        ("80053", "Metabolic Panel"),
        ("83036", "Hemoglobin A1C Test"),
        ("71020", "Chest X-Ray"),
        ("85025", "Complete Blood Count"),
        ("80048", "Basic Metabolic Panel"),
        ("84443", "Thyroid Stimulating Hormone Test"),
        ("80061", "Lipid Panel"),
        ("85610", "Prothrombin Time Test"),
        ("81001", "Urinalysis"),
        ("82565", "Creatinine Blood Test"),
        ("82947", "Glucose Blood Test"),
        ("83540", "Iron Test"),
        ("84153", "Prostate Specific Antigen Test"),
        ("90658", "Influenza Vaccination"),
        ("90471", "Immunization Administration"),
        ("90715", "Tdap Vaccination"),
        ("90732", "Pneumococcal Vaccination"),
        ("71045", "Chest X-Ray Single View"),
        ("71250", "CT Scan Chest"),
        ("70450", "CT Scan Head"),
        ("74176", "CT Scan Abdomen"),
        ("93306", "Echocardiogram"),
        ("93880", "Carotid Ultrasound"),
        ("76700", "Abdominal Ultrasound"),
        ("45378", "Colonoscopy"),
        ("43235", "Upper GI Endoscopy"),
        ("99213", "Office Visit Established Patient"),
        ("12001", "Simple Wound Repair"),
        ("17000", "Skin Lesion Removal"),
        ("20610", "Joint Injection"),
    ]

    rows = []
    for i in range(NUM_PROCEDURES):
        code, name = random.choice(procedure_catalog)

        encounter = random.choice(encounters)
        encounter_id = encounter[0]
        patient_id = encounter[1]

        rows.append([
            f"PROC{i+1}",
            encounter_id,
            patient_id,
            code,
            name,
            round(random.uniform(100, 2000), 2),
        ])

    with open("procedures.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "procedure_id",
            "encounter_id",
            "patient_id",
            "procedure_code",
            "procedure_name",
            "cost",
        ])
        writer.writerows(rows)


def generate_notes(encounters):
    note_types = [
        "Progress",
        "Discharge",
        "Nursing",
        "Consult",
        "Oncology",
        "Emergency",
    ]

    note_templates = [
        "Patient was evaluated during this encounter. Symptoms were reviewed and care plan was discussed.",
        "Patient reports ongoing symptoms. Medication and follow-up instructions were provided.",
        "Clinical assessment completed. Patient advised to return if symptoms worsen.",
        "Care team reviewed patient history, current concerns, and treatment options.",
        "Patient tolerated the visit well. Follow-up appointment recommended.",
        "Provider discussed test results and answered patient questions.",
    ]

    rows = []

    for i in range(NUM_NOTES):
        encounter = random.choice(encounters)
        encounter_id = encounter[0]
        patient_id = encounter[1]
        encounter_date = encounter[4]

        rows.append([
            f"N{i+1}",
            patient_id,
            encounter_id,
            encounter_date,
            random.choice(note_types),
            random.choice(note_templates),
        ])

    with open("notes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "note_id",
            "patient_id",
            "encounter_id",
            "note_date",
            "note_type",
            "note_text",
        ])
        writer.writerows(rows)


def main():
    generate_credentials()
    generate_patients()
    generate_providers()
    generate_departments()

    encounters = generate_encounters()
    generate_procedures(encounters)
    generate_notes(encounters)

    print("Synthetic dataset generated.")
    print("Generated files:")
    print("- credentials.csv")
    print("- patients.csv")
    print("- providers.csv")
    print("- departments.csv")
    print("- encounters.csv")
    print("- procedures.csv")
    print("- notes.csv")


if __name__ == "__main__":
    main()

import pandas as pd
import csv
from datetime import datetime
from getpass import getpass

def log_usage(username, role, event_type, details, log_file='usage_log.csv'):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        # Check if file is empty to write header
        f.seek(0, 2) # Go to the end of the file
        if f.tell() == 0:
            writer.writerow(['timestamp', 'username', 'role', 'event_type', 'details'])
        writer.writerow([timestamp, username, role, event_type, details])

def login_user(username, password):

    try:
        credentials_df = pd.read_csv('credentials.csv')
        # Check if username and password match any entry
        user_entry = credentials_df[
            (credentials_df['username'] == username) &
            (credentials_df['password'] == password)
        ]
        if not user_entry.empty:
            role = user_entry['role'].iloc[0]
            log_usage(username, role, 'Login Success', 'User logged in successfully.')
            return True, role
        else:
            log_usage(username, 'N/A', 'Login Failed', 'Incorrect username or password.')
            return False, None
    except FileNotFoundError:
        print("Error: credentials.csv not found. Please run the data generation cell first.")
        log_usage(username, 'N/A', 'Login Failed', 'credentials.csv not found.')
        return False, None

def display_clinician_menu():
    print("\n--- Clinician/Nurse Menu ---")
    print("1. Retrieve Patient")
    print("2. Add Patient")
    print("3. Remove Patient")
    print("4. Count Visits")
    print("5. View Note")
    print("6. Exit")

def display_management_menu():
    print("\n--- Management Menu ---")
    print("1. Generate Key Statistics")
    print("2. Exit")

def display_admin_menu():
    print("\n--- Admin Menu ---")
    print("1. Count Encounters Per Patient")
    print("2. Count Encounters By Department")
    print("3. Monitor Provider Workload")
    print("4. Monitor Revenue")
    print("5. Exit")

def retrieve_patient(patient_id, patients_df, encounters_df, procedures_df, notes_df):
    patient_info = patients_df[patients_df['patient_id'] == patient_id]

    if patient_info.empty:
        print(f"Patient with ID {patient_id} not found.")
        return

    print(f"\n--- Patient Information for {patient_id} ---")
    display(patient_info)

    patient_encounters = encounters_df[encounters_df['patient_id'] == patient_id].copy()
    if patient_encounters.empty:
        print(f"No encounters found for patient {patient_id}.")
        return
    # Get date for the most recent encounter
    patient_encounters['encounter_date'] = pd.to_datetime(patient_encounters['encounter_date'])
    most_recent_encounter = patient_encounters.sort_values(by='encounter_date', ascending=False).iloc[0]

    print("\n--- Most Recent Encounter Details ---")
    display(pd.DataFrame([most_recent_encounter]))

    recent_encounter_id = most_recent_encounter['encounter_id']

    # Get procedures for the most recent encounter
    recent_procedures = procedures_df[procedures_df['encounter_id'] == recent_encounter_id]
    if not recent_procedures.empty:
        print("\n--- Procedures for Most Recent Encounter ---")
        display(recent_procedures)
    else:
        print("No procedures recorded for this encounter.")

    # Get notes for the most recent encounter
    recent_notes = notes_df[notes_df['encounter_id'] == recent_encounter_id]
    if not recent_notes.empty:
        print("\n--- Notes for Most Recent Encounter ---")
        display(recent_notes)
    else:
        print("No notes recorded for this encounter.")

def add_patient(patients_df):
    print("\n--- Add New Patient ---")

    # generate new patient ID
    max_patient_id_num = patients_df['patient_id'].str.extract(r'P(\d+)').astype(int).max()[0]
    new_patient_id = f"P{max_patient_id_num + 1}"
    print(f"Assigning new Patient ID: {new_patient_id}")

    # validation
    while True:
        try:
            age = int(input("Enter Age (e.g., 30): "))
            if age <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid age. Please enter a positive integer.")

    genders = ["Male", "Female", "Non-binary"]
    while True:
        gender = input(f"Enter Gender {genders} (e.g., Male): ").strip()
        if gender in genders:
            break
        else:
            print("Invalid gender. Please choose from Male, Female, or Non-binary.")

    while True:
        try:
            bmi_input = input("Enter BMI (e.g., 25.5): ").strip()
            bmi = float(bmi_input)
            if bmi <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid BMI. Please enter a positive number.")

    while True:
        try:
            a1c_input = input("Enter A1C (e.g., 6.0, leave blank if unknown): ").strip()
            if a1c_input == '':
                a1c = '' # empty string for unknown
                break
            a1c = float(a1c_input)
            if a1c <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid A1C. Please enter a positive number or leave blank.")

    while True:
        try:
            bp_sys = int(input("Enter Systolic Blood Pressure (e.g., 120): "))
            if bp_sys <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid Systolic BP. Please enter a positive integer.")

    while True:
        try:
            bp_dia = int(input("Enter Diastolic Blood Pressure (e.g., 80): "))
            if bp_dia <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid Diastolic BP. Please enter a positive integer.")

    while True:
        smoking_input = input("Is patient a smoker? (yes/no): ").strip().lower()
        if smoking_input == 'yes':
            smoking = True
            break
        elif smoking_input == 'no':
            smoking = False
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    new_patient_data = {
        'patient_id': new_patient_id,
        'age': age,
        'gender': gender,
        'bmi': bmi,
        'a1c': a1c,
        'bp_sys': bp_sys,
        'bp_dia': bp_dia,
        'smoking': smoking
    }

    # Append new patient to DataFrame
    new_patient_df = pd.DataFrame([new_patient_data])
    updated_patients_df = pd.concat([patients_df, new_patient_df], ignore_index=True)

    # Save updated DataFrame to CSV
    updated_patients_df.to_csv('patients.csv', index=False)
    print(f"Patient {new_patient_id} added successfully and patients.csv updated.")
    display(new_patient_df) # Display the newly added patient

    return updated_patients_df # Return the updated DataFrame

def remove_patient(patient_id_to_remove, patients_df):
    print(f"\n--- Remove Patient {patient_id_to_remove} ---")

    if patient_id_to_remove not in patients_df['patient_id'].values:
        print(f"Error: Patient with ID {patient_id_to_remove} not found.")
        return patients_df

    # Remove the patient from the DataFrame
    updated_patients_df = patients_df[patients_df['patient_id'] != patient_id_to_remove]

    # Save updated DataFrame to CSV
    updated_patients_df.to_csv('patients.csv', index=False)
    print(f"Patient {patient_id_to_remove} removed successfully and patients.csv updated.")

    return updated_patients_df # Return the updated DataFrame

def count_visits(patient_id, encounters_df, procedures_df):
    print(f"\n--- Counting Visits and Procedures for {patient_id} ---")

    patient_encounters = encounters_df[encounters_df['patient_id'] == patient_id]
    num_encounters = len(patient_encounters)

    patient_procedures = procedures_df[procedures_df['patient_id'] == patient_id]
    num_procedures = len(patient_procedures)

    if num_encounters > 0 or num_procedures > 0:
        print(f"Patient {patient_id} has had {num_encounters} encounters.")
        print(f"Patient {patient_id} has had {num_procedures} procedures.")
    else:
        print(f"No encounters or procedures found for patient {patient_id}.")

def view_note(note_id, notes_df):
    print(f"\n--- Viewing Note {note_id} ---")

    note_info = notes_df[notes_df['note_id'] == note_id]

    if note_info.empty:
        print(f"Error: Note with ID {note_id} not found.")
        return

    # Display the full note details
    display(note_info)
    print(f"Note Text: {note_info['note_text'].iloc[0]}")

def generate_key_statistics(patients_df, encounters_df, procedures_df, notes_df):
    print("\n--- Generating Key Statistics ---")

    # total number of patients, encounters, procedures, and notes
    print(f"Total Patients: {len(patients_df)}")
    print(f"Total Encounters: {len(encounters_df)}")
    print(f"Total Procedures: {len(procedures_df)}")
    print(f"Total Notes: {len(notes_df)}")
    print("\n")

    # total number of encounters by department
    print("--- Encounter Statistics ---")
    print("Encounters by Department:")
    display(encounters_df['department_id'].value_counts().reset_index())
    print("Encounter Type Distribution:")
    display(encounters_df['encounter_type'].value_counts().reset_index())

    # average encounters per patient
    encounters_per_patient = encounters_df.groupby('patient_id').size().mean()
    print(f"Average Encounters per Patient: {encounters_per_patient:.2f}")
    print("\n")

    # top 5 most common procedures
    print("--- Procedure Statistics ---")
    print("Top 5 Most Common Procedures:")
    display(procedures_df['procedure_name'].value_counts().head(5).reset_index())
    print(f"Average Procedure Cost: {procedures_df['cost'].mean():.2f}")
    print("\n")

def count_encounters_per_patient(encounters_df):
    print("\n--- Counting Encounters Per Patient ---")
    encounter_counts = encounters_df.groupby('patient_id').size().reset_index(name='encounter_count')
    display(encounter_counts.sort_values(by='encounter_count', ascending=False))

def count_encounters_by_department(encounters_df):
    print("\n--- Counting Encounters By Department ---")
    department_counts = encounters_df['department_id'].value_counts().reset_index(name='encounter_count')
    display(department_counts)

def monitor_provider_workload(encounters_df, providers_df):
    print("\n--- Monitoring Provider Workload ---")
    # Count encounters per provider
    encounter_counts_by_provider = encounters_df['provider_id'].value_counts().reset_index()
    encounter_counts_by_provider.columns = ['provider_id', 'encounter_count']

    # get provider names and specialty
    merged_df = pd.merge(encounter_counts_by_provider, providers_df, on='provider_id', how='left')

    # Select relevant columns and sort by encounter count
    result_df = merged_df[['provider_id', 'name', 'specialty', 'encounter_count']].sort_values(by='encounter_count', ascending=False)

    print("Providers ranked by number of encounters handled:")
    display(result_df)

def monitor_revenue(procedures_df, encounters_df):
    print("\n--- Monitoring Revenue by Department ---")
    # Merge procedures with encounters to link costs to departments
    merged_df = pd.merge(procedures_df, encounters_df, on='encounter_id', how='left')

    # Group by department and sum the costs
    revenue_by_department = merged_df.groupby('department_id')['cost'].sum().reset_index()
    revenue_by_department.columns = ['department_id', 'total_revenue']

    # Sort by total revenue in descending order
    result_df = revenue_by_department.sort_values(by='total_revenue', ascending=False)

    print("Total procedure costs generated by each department:")
    display(result_df)

def handle_clinician_action(choice, patients_df, encounters_df, procedures_df, notes_df, username, role):
    exit_status = False
    updated_patients_df = patients_df

    if choice == '1':
        patient_id = input("Enter Patient ID (e.g., P1): ").strip()
        retrieve_patient(patient_id, patients_df, encounters_df, procedures_df, notes_df)
        log_usage(username, role, 'Action Performed', f'Retrieved patient {patient_id}.')
    elif choice == '2':
        updated_patients_df_before = patients_df.shape[0]
        updated_patients_df = add_patient(patients_df)
        if updated_patients_df.shape[0] > updated_patients_df_before:
            new_patient_id = updated_patients_df.iloc[-1]['patient_id']
            log_usage(username, role, 'Action Performed', f'Added new patient {new_patient_id}.')
        else:
            log_usage(username, role, 'Action Failed', 'Attempted to add patient but no changes detected.')
    elif choice == '3':
        patient_id_to_remove = input("Enter Patient ID to remove (e.g., P1): ").strip()
        updated_patients_df_before = patients_df.shape[0]
        updated_patients_df = remove_patient(patient_id_to_remove, patients_df)
        if updated_patients_df.shape[0] < updated_patients_df_before: # Check if patient was actually removed
            log_usage(username, role, 'Action Performed', f'Removed patient {patient_id_to_remove}.')
        else:
            log_usage(username, role, 'Action Failed', f'Attempted to remove patient {patient_id_to_remove} but not found.')
    elif choice == '4':
        patient_id_to_count = input("Enter Patient ID to count visits for (e.g., P1): ").strip()
        count_visits(patient_id_to_count, encounters_df, procedures_df)
        log_usage(username, role, 'Action Performed', f'Counted visits for patient {patient_id_to_count}.')
    elif choice == '5':
        note_id_to_view = input("Enter Note ID to view (e.g., N1): ").strip()
        view_note(note_id_to_view, notes_df)
        log_usage(username, role, 'Action Performed', f'Viewed note {note_id_to_view}.')
    elif choice == '6':
        print("Exiting application.")
        exit_status = True # Indicates exit
        log_usage(username, role, 'Action Performed', 'Exited clinician menu.')
    else:
        print("Invalid choice. Please try again.")
        log_usage(username, role, 'Action Failed', f'Invalid choice in clinician menu: {choice}.')
    return exit_status, updated_patients_df

def handle_management_action(choice, patients_df, encounters_df, procedures_df, notes_df, username, role):
    if choice == '1':
        generate_key_statistics(patients_df, encounters_df, procedures_df, notes_df)
        log_usage(username, role, 'Action Performed', 'Generated key statistics.')
    elif choice == '2':
        print("Exiting application.")
        log_usage(username, role, 'Action Performed', 'Exited management menu.')
        return True # Indicates exit
    else:
        print("Invalid choice. Please try again.")
        log_usage(username, role, 'Action Failed', f'Invalid choice in management menu: {choice}.')
    return False

def handle_admin_action(choice, encounters_df, providers_df, procedures_df, username, role):
    if choice == '1':
        count_encounters_per_patient(encounters_df)
        log_usage(username, role, 'Action Performed', 'Counted encounters per patient.')
    elif choice == '2':
        count_encounters_by_department(encounters_df)
        log_usage(username, role, 'Action Performed', 'Counted encounters by department.')
    elif choice == '3':
        monitor_provider_workload(encounters_df, providers_df)
        log_usage(username, role, 'Action Performed', 'Monitored provider workload.')
    elif choice == '4':
        monitor_revenue(procedures_df, encounters_df)
        log_usage(username, role, 'Action Performed', 'Monitored revenue by department.')
    elif choice == '5':
        print("Exiting application.")
        log_usage(username, role, 'Action Performed', 'Exited admin menu.')
        return True
    else:
        print("Invalid choice. Please try again.")
        log_usage(username, role, 'Action Failed', f'Invalid choice in admin menu: {choice}.')
    return False

# --- system login ---
print("\n--- system login ---")
print("enter your credentials for the health system:")
input_username = input("Username: ").strip() # Added .strip() to remove leading/trailing whitespace
input_password = getpass("Password: ")

# Before the login attempt, ensure the log file exists with headers
log_file_name = 'usage_log.csv'
try:
    with open(log_file_name, 'x', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'username', 'role', 'event_type', 'details'])
except FileExistsError:
    pass

is_authenticated, user_role = login_user(input_username, input_password)
if is_authenticated:
    print(f"Login successful! Welcome, {input_username}. Your role is {user_role}.")

    # Load all necessary dataframes
    try:
        patients_df = pd.read_csv('patients.csv')
        encounters_df = pd.read_csv('encounters.csv')
        procedures_df = pd.read_csv('procedures.csv')
        notes_df = pd.read_csv('notes.csv')
        providers_df = pd.read_csv('providers.csv') # Load providers_df
        print("Patient, encounter, procedure, and note information loaded successfully.")

        exit_program = False
        while not exit_program:
            if user_role == 'management':
                display_management_menu()
                choice = input("Enter your choice: ")
                # Pass all dataframes and user info to the management handler
                exit_program = handle_management_action(choice, patients_df, encounters_df, procedures_df, notes_df, input_username, user_role)
            elif user_role in ['nurse', 'clinician']:
                display_clinician_menu()
                choice = input("Enter your choice: ")
                # Pass all dataframes and user info to the clinician handler and update patients_df
                temp_exit_program, patients_df = handle_clinician_action(choice, patients_df, encounters_df, procedures_df, notes_df, input_username, user_role)
                exit_program = temp_exit_program
            elif user_role == 'admin':
                display_admin_menu()
                choice = input("Enter your choice: ")
                # Pass encounters_df, providers_df, procedures_df, and user info to the admin handler
                exit_program = handle_admin_action(choice, encounters_df, providers_df, procedures_df, input_username, user_role)
            else:
                print("No specific actions defined for your role. Exiting.")
                exit_program = True
                log_usage(input_username, user_role, 'Application Exit', 'Exited application from undefined role.')

    except FileNotFoundError:
        print("Error: one or more CSV files not found. Please run the data generation cell first.")
        log_usage(input_username, user_role, 'Error', 'Missing data files during application run.')

else:
    print(f"Login failed for {input_username}. Incorrect username or password.")

usage_log_df = pd.read_csv('usage_log.csv')
display(usage_log_df)

