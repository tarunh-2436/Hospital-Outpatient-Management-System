import random, pickle, datetime

class TreeNode :
  def __init__(self,name) :
    self.name = name
    self.children = []


class Hospital :

  def __init__(self,name) :
    self.root = TreeNode(name)

  def add_department(self,department_name) :
    parent=self.root
    department=TreeNode(department_name)
    parent.children.append(department)

  def add_doctor(self,doctor) :
    for i in self.root.children :
      if i.name == doctor.Department :
        i.children.append(doctor)
    
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
    return Patients
  
  def Retrieve_Doctors() :
    f=open('Hospital Details.pkl','rb')
    BSS = pickle.load(f)
    f.close()
    doctors = []
    Usernames = []
    def traverse(node) :
      try :
        for child in node.children :
          traverse(child)
      except AttributeError :
        doctors.append(node)
    traverse(BSS.root)
    for i in doctors :
      Usernames.append(i.Username)
    return doctors, Usernames      

class Patient() :

  def __init__(self) :
    self.Patient_Stack = []

  def generate_patient_ID(self) :
        Patients = Hospital.Retrieve_Patients()
        while True :
            ID = random.randint(1,999999)
            for Patient in Patients :
              if int(Patient.Patient_ID) == ID :
                continue
            break
        return ID
  
  def book_appointment(self) :
    f = open('Hospital Details.pkl','rb')
    BSS = pickle.load(f)
    f.close()
    Doctors = []
    for Department in BSS.root.children :
      for Doctor in Department.children :
        Doctors.append(Doctor)
    Required_Dept = input('''
The Departments In The Hospital Are
1.Cardiology
2.General Medicine
3.Surgery
                          
Enter Department To Book Appointment In : ''')
    print('Doctors In',Required_Dept,'Are :',end = '\n\n')
    for i in Doctors :
      if i.Department == Required_Dept :
        print(i.Name)
        print('Appointment Slots : ',end='')
        print(*i.Slots,sep = ', ')
        print()

    Required_Doctor = input('Enter Name Of Required Doctor : ').upper()
    for i in Doctors :
      if i.Name.upper() == Required_Doctor.upper() :
        Required_Date = input('Enter Required Date Of Appointment (DD/MM/YYYY) : ')
        Required_Time = input('Enter Required Time Of Appointment (24hrs) : ')
        availability = i.Add_Appointment(Required_Date, Required_Time, self)
        if availability == False :
          self.book_appointment()
        else :
          print(i.Appointments)
          f = open('Hospital Details.pkl','wb')
          pickle.dump(BSS,f)
          f.close()
          print('Appointment Booked')
        
  
class Doctor() :
  def __init__(self) :
    self.Username = None
    self.Password = None
    self.Appointments = {}
  
  def Add_Appointment(self,date,time,patient) :
    date_str = date
    date = datetime.datetime(int(date_str[6:]),int(date_str[3:5]),int(date_str[:2]))
    day_of_week = date.weekday()
    if self.Department != 'General Medicine' :
      if day_of_week == 6 :
        print(self.Name, 'Not Available On Sunday')
        return False
    if date_str not in self.Appointments :
      self.Appointments[date_str] = {time:patient}
    else :
      for booked_time in self.Appointments[date_str] :
        if time == booked_time :
          print(self.Name, 'Not Available On Given Time Slot')
          return False
        self.Appointments[date_str][time] = patient
        return True
