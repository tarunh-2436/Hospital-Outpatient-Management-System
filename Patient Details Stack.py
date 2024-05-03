import random,pickle
from datetime import date

class Patient :

    def __init__(self,name,age,gender,first_visit=True) :
        self.Name = name
        self.Age = age
        self.Gender = gender
        self.First_Visit = first_visit
        if self.First_Visit :
            self.Patient_ID = self.generate_patient_ID()
            self.stack = []
             

    def generate_patient_ID(self) :
        while True :
            ID = random.randint(1,999999)
            if ID not in patient_ids :
                patient_ids.append(ID)
                print('Generated Patient ID :',ID)
                break
        return ID
    
    def Patient_Visit(self) :

        try :
            print('\nPATIENTS MEDICAL DETAILS',end='\n\n')
            print('Name :',self.Name)
            print('Age :',self.Age)
            print('Gender :',self.Gender)
            print()
            for i,j in self.Patient_Medical_Details.items() :
                if i != 'Surgery Details' or i != 'List Of Allergies' :
                    print(i,':',j)
                elif i == 'Surgery Details' :
                    print(i)
                    print(*j,sep = '\n')
                else :
                    print(i)
                    print(*j,sep = '\n')

        except :
            pass

        else :
            pass

        if len(self.stack) > 0 and len(self.stack) <= 3 :
            print('\nDETAILS OF PATIENTS LAST 3 VISITS',end='\n\n')
            for i in self.stack[::-1] :
                for Field,Data in i.items() :
                    print(Field,':',Data)
                print()

        elif len(self.stack) > 3 :
            print('\nDETAILS OF PATIENTS LAST 3 VISITS',end='\n\n')
            for i in self.stack[-1:-4:-1] :
                for Field,Data in i.items() :
                    print(Field,':',Data)
                print()
                

        if self.First_Visit :

            self.Patient_Medical_Details = {}

            Diabetes = input('Enter YES if patient has history of Diabetes : ').upper()
            self.Patient_Medical_Details['Diabetes'] = Diabetes

            if Diabetes == 'YES' :
                Diabetes_Duration = input('How long has the patient had Diabetes : ')
                self.Patient_Medical_Details['Diabetes Duration'] = Diabetes_Duration

            Hypertension = input('Enter YES if patient has history of Hypertension : ').upper()
            self.Patient_Medical_Details['Hypertension'] = Hypertension
            
            if Hypertension == 'YES' :
                Hypertension_Duration = input('How long has the patient had Hypertension : ')
                self.Patient_Medical_Details['Hypertension Duration'] = Hypertension_Duration
            
            Coronary_Artery_Disease = input('Enter YES if patient has history of Coronary Artery Disease : ').upper()
            self.Patient_Medical_Details['Coronary Artery Disease'] = Coronary_Artery_Disease
            
            if Coronary_Artery_Disease == 'YES' :
                Coronary_Artery_Disease_Duration = input('How long has the patient had Coronary Artery Disease : ')
                self.Patient_Medical_Details['Coronary Artery Disease Duration'] = Coronary_Artery_Disease_Duration

            Asthma = input('Enter YES if patient has history of Asthma : ').upper()
            self.Patient_Medical_Details['Asthma'] = Asthma
            
            if Asthma == 'YES' :
                Asthma_Duration = input('How long has the patient had Asthma : ')
                self.Patient_Medical_Details['Asthma Duration'] = Asthma_Duration

            Surgery = input('Enter YES if patient has undergone any Surgeries in the past : ').upper()
            self.Patient_Medical_Details['Surgery'] = Surgery
            
            if Surgery == 'YES' :
                n = int(input('How Many Surgeries has the patient undergone ? '))
                Surgery_Info = {}
                for i in range(n) :
                    Date = input('When was the Surgery done ? (DD/MM/YYYY) ')
                    Details = input('What was the Surgery For ? ')
                    Surgery_Info[Date] = Details
                self.Patient_Medical_Details['Surgery Details'] = Surgery_Info

            Allergy = input('Enter YES if patient has any Allergies : ').upper()
            self.Patient_Medical_Details['Allergy'] = Allergy
            
            if Allergy == 'YES' :
                n = int(input('How Many Allergies does the patient have ? '))
                Allergies = []
                for i in range(n) :
                    Allergen = input('What is the patient Allergic to ? ')
                    Allergies.append(Allergen)
                self.Patient_Medical_Details['List Of Allergies'] = Allergies

            Drinking = input('Enter YES if patient has habit of Drinking Alcohol : ').upper()
            self.Patient_Medical_Details['Drinking'] = Drinking
            
            Smoking = input('Enter YES if patient has habit of Smoking : ').upper()
            self.Patient_Medical_Details['Smoking'] = Smoking
            self.First_Visit = False

        Visit_Details = {'Date':date.today()}

        Patient_Complaints = input('Describe Complaints Of Pateint : ')
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

        Prescription = input('Enter Prescription Given To Patient (Medicine Name - Dosage - No. Of Times - No. Of Days) : ')
        Visit_Details['Prescription'] = Prescription

        self.stack.append(Visit_Details)

with open('Patient Details.pkl','rb') as f :
    Patients = pickle.load(f)
    patient_ids = [obj.Patient_ID for obj in Patients]
    print(Patients)
    print(patient_ids)

New_Patients = input('Enter "Y" If Any New Patients : ').upper()

if New_Patients == 'Y' :
    print('\nENTER DETAILS OF NEW PATIENTS')
    while True :
        Name = input('Enter Name Of Patient : ')
        Age = input('Enter Age Of Patient : ')
        Sex = input('Enter Sex Of Patient : ').upper()
        First_Visit = input('First Visit Of Patient ? (True/False) ')
        Patient_Object = Patient(Name,Age,Sex,First_Visit)
        Patients.append(Patient_Object)
        chk = input('Enter "N" If No More Patient Details : ').upper()
        if chk == 'N' :
            break        

while True :
    ID = int(input('Enter ID Of Patient Visiting  : '))
    if ID not in patient_ids :
        print('PATIENT ID NOT FOUND')
        continue
    Index = patient_ids.index(ID)
    Patient_Object = Patients[Index]
    Patient_Object.Patient_Visit()
    chk = input('Enter "N" If No More Patients : ').upper()
    if chk == 'N' :
        break
f = open('Patient Details.pkl','wb')
pickle.dump(Patients,f)
f.close()

  
