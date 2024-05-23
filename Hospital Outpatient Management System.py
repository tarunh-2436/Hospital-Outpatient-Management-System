import random, pickle
from datetime import date

class Hospital :

  def __init__(self) :
    self.Patient_Stack = []
    
  def Retrieve_Patients() :
    Patients = []
    Patient_IDs = []
    with open('Patient Details.pkl','rb') as f :
      while True :
        try :
          Patient = pickle.load(f)
        except EOFError :
          break
        else :
          Patients.append(Patient)
          Patient_IDs = [obj.Patient_ID for obj in Patients]
    return Patients, Patient_IDs
      

class Patient(Hospital) :
  def __init__(self) :
    super().__init__()

  def generate_patient_ID(self) :
        Patients, Patient_IDs = Hospital.Retrieve_Patients()
        while True :
            ID = random.randint(1,999999)
            if ID not in Patient_IDs :
                print('Generated Patient ID :',ID)
                break
        return ID

def register() :

  New_Patient = Patient()
    
  New_Patient.Name = input('Enter Patient Name : ')
  New_Patient.Age = int(input('Enter Patient Age : '))
  New_Patient.Gender = input('Enter Patient Gender : ')
  New_Patient.Phone_No = int(input('Enter Patient Phone No : '))
  New_Patient.Address = input('Enter Patient Address : ')
  New_Patient.Patient_Medical_Details = {}

  Diabetes = input('Enter YES if patient has history of Diabetes : ').upper()
  New_Patient.Patient_Medical_Details['Diabetes'] = Diabetes

  if Diabetes == 'YES' :
    Diabetes_Duration = input('How long has the patient had Diabetes : ')
    New_Patient.Patient_Medical_Details['Diabetes Duration'] = Diabetes_Duration

  Hypertension = input('Enter YES if patient has history of Hypertension : ').upper()
  New_Patient.Patient_Medical_Details['Hypertension'] = Hypertension
          
  if Hypertension == 'YES' :
    Hypertension_Duration = input('How long has the patient had Hypertension : ')
    New_Patient.Patient_Medical_Details['Hypertension Duration'] = Hypertension_Duration
          
  Coronary_Artery_Disease = input('Enter YES if patient has history of Coronary Artery Disease : ').upper()
  New_Patient.Patient_Medical_Details['Coronary Artery Disease'] = Coronary_Artery_Disease
          
  if Coronary_Artery_Disease == 'YES' :
    Coronary_Artery_Disease_Duration = input('How long has the patient had Coronary Artery Disease : ')
    New_Patient.Patient_Medical_Details['Coronary Artery Disease Duration'] = Coronary_Artery_Disease_Duration

  Asthma = input('Enter YES if patient has history of Asthma : ').upper()
  New_Patient.Patient_Medical_Details['Asthma'] = Asthma
          
  if Asthma == 'YES' :
    Asthma_Duration = input('How long has the patient had Asthma : ')
    New_Patient.Patient_Medical_Details['Asthma Duration'] = Asthma_Duration

  Surgery = input('Enter YES if patient has undergone any Surgeries in the past : ').upper()
  New_Patient.Patient_Medical_Details['Surgery'] = Surgery
          
  if Surgery == 'YES' :
    n = int(input('How Many Surgeries has the patient undergone ? '))
    Surgery_Info = {}
    for i in range(n) :
      Date = input('When was the Surgery done ? (DD/MM/YYYY) ')
      Details = input('What was the Surgery For ? ')
      Surgery_Info[Date] = Details
      New_Patient.Patient_Medical_Details['Surgery Details'] = Surgery_Info

  Allergy = input('Enter YES if patient has any Allergies : ').upper()
  New_Patient.Patient_Medical_Details['Allergy'] = Allergy
          
  if Allergy == 'YES' :
    n = int(input('How Many Allergies does the patient have ? '))
    Allergies = []
    for i in range(n) :
      Allergen = input('What is the patient Allergic to ? ')
      Allergies.append(Allergen)
    New_Patient.Patient_Medical_Details['List Of Allergies'] = Allergies

  Drinking = input('Enter YES if patient has habit of Drinking Alcohol : ').upper()
  New_Patient.Patient_Medical_Details['Drinking'] = Drinking
          
  Smoking = input('Enter YES if patient has habit of Smoking : ').upper()
  New_Patient.Patient_Medical_Details['Smoking'] = Smoking

  New_Patient.Patient_ID = New_Patient.generate_patient_ID()
  print('YOUR PATIENT ID IS', New_Patient.Patient_ID, '\nUse This ID To Login To The Website In Future')
  
  while True :
    password = input('''
Your Password Must Contain :
Minimum 1 Uppercase Alphabet
Minimum 1 Lowercase Alphabet
Minimum 1 Number
No Other Space Or Character Is Allowed

Enter Password To Use With Patient ID To Log In : ''')
    confirm_password = input('Re-Enter Password For COnformation : ')

    if password != confirm_password :
      print('Passwords Dont Match')
      continue
    
    elif len([x for x in password if x.isupper()]) == 0 :
      print('Password Must Contain Minimum 1 Uppercase Alphabet')
      continue

    elif len([x for x in password if x.islower()]) == 0 :
      print('Password Must Contain Minimum 1 Lowercase Alphabet')
      continue

    elif len([x for x in password if x.isdigit()]) == 0 :
      print('Password Must Contain Minimum 1 Number')
      continue

    elif len([x for x in password if x.isalnum()]) < len(password) :
      print('Password Must Not Contain Any Spaces or Any Other Characters')
      continue

    else :
      New_Patient.Password = password
      print('Password Set Succesfully')
      break

  f = open('Patient Details.pkl','ab') 
  pickle.dump(New_Patient,f)
  f.close()
  print('REGISTRATION SUCCESFUL')


def login() :

    Patients, Patient_IDs = Hospital.Retrieve_Patients()
    patient_id = int(input('Enter Patient ID : '))
    password = input('Enter Password : ')
    if patient_id not in Patient_IDs :
      print('INVALID PATIENT ID')
    else :
      for i in Patients :
        if i.Patient_ID == patient_id and i.Password == password :
          print('LOGIN SUCCESFUL')
          return
      print('INVALID PASSWORD')
      login()

def Patient_Visit() :

  patient_id = int(input('Enter ID Of Patient Visiting : '))
  Patients, Patient_IDs = Hospital.Retrieve_Patients()
  if patient_id not in Patient_IDs :
    Patient_Visit()
    return
  else :
    for Patient in Patients :
      if Patient.Patient_ID == patient_id :
        Visiting_Patient = Patient

  print('\nPATIENTS MEDICAL DETAILS',end='\n\n')
  print('Name :',Visiting_Patient.Name)
  print('Age :',Visiting_Patient.Age)
  print('Gender :',Visiting_Patient.Gender)
  print()
  for i,j in Visiting_Patient.Patient_Medical_Details.items() :
      if i != 'Surgery Details' or i != 'List Of Allergies' :
          print(i,':',j)
      elif i == 'Surgery Details' :
          print(i)
          for k in j :
            print(k,':',j[k])
      else :
          print(i)
          print(*j,sep = '\n')

  print('\nDETAILS OF PATIENTS LAST 3 VISITS',end='\n\n')
  for i in Visiting_Patient.Patient_Stack[-1:-4:-1] :
      for Field,Data in i.items() :
          if Field != 'Prescription' :
            print(Field,':',Data)
          else :
            print(Field)
            print(*Data, sep='\n')
      print()

  Visit_Details = {'Date':date.today()}

  Patient_Complaints = input('Describe Complaints Of Patient : ')
  Visit_Details['Complaints'] = Patient_Complaints

  Blood_Pressure = input('Enter Blood Pressure Value (Eg. "120/80") : ') + ' mm of HG'
  Visit_Details['Blood Pressure'] = Blood_Pressure

  Pulse = input('Enter Pulse Rate Value : ') +  ' bpm'
  Visit_Details['Pulse Rate'] = Pulse

  Temperature = input('Enter Body Temperature Value : ') + ' F'
  Visit_Details['Body Temperature'] = Temperature

  Other_Findings = input('Describe Any Other Findings : ')
  Visit_Details['Other Findings'] = Other_Findings

  Diagnosis = input('Enter Diagnosis : ')
  Visit_Details['Diagnosis'] = Diagnosis

  Instructions = input('Enter Instructions Given To Patient : ')
  Visit_Details['Instructions'] = Instructions

  Prescription = []
  while True :
    Medicine = input('Enter Prescription Given To Patient (Medicine Name - Dosage - No. Of Times - No. Of Days) : ')
    Prescription.append(Medicine)
    chk = input('Any More Medicines (Y/N) : ').upper()
    if chk == 'N' :
      break
    
  Visit_Details['Prescription'] = Prescription

  Visiting_Patient.Patient_Stack.append(Visit_Details)

#register()
#login()
Patient_Visit()
