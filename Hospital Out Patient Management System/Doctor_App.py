from flask import Flask, render_template, request, redirect, url_for
import random, pickle, datetime, os
from functions.classes import TreeNode,Hospital,Patient,Doctor

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('doctor_home.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("doctor_login.html")
    
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        Doctors = Hospital.Retrieve_Doctors()[0]
        for doctor in Doctors:
            if doctor.Username == username and doctor.Password == password:
                return redirect(url_for('choosepatient',doctor=doctor.Name))
            
        return render_template('doctor_login.html')

@app.route('/choosepatient/<doctor>',methods=['GET','POST'])
def choosepatient(doctor) :
    Doctors=Hospital.Retrieve_Doctors()[0]
    for Doctor in Doctors :
        if Doctor.Name == doctor :
            Doctor_Obj = Doctor
    date=datetime.date.today().isoformat()
    try :
        Appointments = str(Doctor_Obj.Appointments[date])[1:-1]
    except KeyError :
        return redirect(url_for('noappointments'))
    else :
        if request.method == 'GET' :
            return render_template('paid.html',doctor=doctor,appointments = Appointments)
        if request.method == 'POST' :
            patient_id = int(request.form['Patient ID'])
            Patients = Hospital.Retrieve_Patients()
            for Patient in Patients :
                if Patient.Patient_ID == patient_id :
                    Patient_Obj=Patient
                    return redirect(url_for('patientvisit',doctor=doctor,patient=patient_id))
            return render_template('paid.html',doctor=doctor,appointments = Appointments) 
            
        
@app.route('/patientvisit/<doctor>/<patient>',methods=['GET','POST'])
def patientvisit(doctor,patient) :
    Doctors=Hospital.Retrieve_Doctors()[0]
    for Doctor in Doctors :
        if Doctor.Name == doctor :
            Doctor_Obj = Doctor
            break
    Patients = Hospital.Retrieve_Patients()
    for Patient in Patients :
        if Patient.Patient_ID == int(patient) :
            Patient_Obj=Patient
            break
    if request.method == 'GET' :
        Name = Patient_Obj.Name
        Age = Patient_Obj.Age
        Gender = Patient_Obj.Gender
        Hypertension = Patient_Obj.Medical_Details['Hypertension']+' ('+Patient_Obj.Medical_Details['Hypertension Duration']+')'
        Diabetes = Patient_Obj.Medical_Details['Diabetes']+' ('+Patient_Obj.Medical_Details['Diabetes Duration']+')'
        Heart_Disease = Patient_Obj.Medical_Details['Heart Disease']+' ('+Patient_Obj.Medical_Details['Heart Disease Duration']+')'
        Asthma = Patient_Obj.Medical_Details['Asthma']+' ('+Patient_Obj.Medical_Details['Asthma Duration']+')'
        Epilepsy = Patient_Obj.Medical_Details['Epilepsy']+' ('+Patient_Obj.Medical_Details['Epilepsy Duration']+')'
        Stroke = Patient_Obj.Medical_Details['Stroke']+' ('+Patient_Obj.Medical_Details['Stroke Duration']+')'
        Peptic_Ulcer = Patient_Obj.Medical_Details['Peptic Ulcer']+' ('+Patient_Obj.Medical_Details['Peptic Ulcer Duration']+')'
        Tuberculosis = Patient_Obj.Medical_Details['Tuberculosis']+' ('+Patient_Obj.Medical_Details['Tuberculosis Duration']+')'
        Surgery = Patient_Obj.Medical_Details['Surgery']+' ('+Patient_Obj.Medical_Details['Surgery Detailsn']+')'
        Allergy = Patient_Obj.Medical_Details['Allergy']+' ('+Patient_Obj.Medical_Details['Allergy Details']+')'
        Smoking = Patient_Obj.Medical_Details['Smoking']
        Drinking = Patient_Obj.Medical_Details['Drinking']
        if Patient_Obj.Patient_Stack != [] :
            Last_Visit = Patient_Obj.Patient_Stack[-1]
            Last_Visit_Date = Last_Visit['Date']
            Last_Visit_Notes = Last_Visit["Doctor's Notes"]
            Last_Visit_Prescription = Last_Visit['Prescription']
            return render_template('patient_visit.html',doctor=doctor,patient=patient,Name=Name,Age=Age,Gender=Gender,Hypertension=Hypertension,Diabetes=Diabetes,Heart_Disease=Heart_Disease,Asthma=Asthma,Epilepsy=Epilepsy,Stroke=Stroke,Peptic_Ulcer=Peptic_Ulcer,Tuberculosis=Tuberculosis,Surgery=Surgery,Allergy=Allergy,Smoking=Smoking,Drinking=Drinking,Last_Visit_Date=Last_Visit_Date,Last_Visit_Notes=Last_Visit_Notes,Last_Visit_Prescription=Last_Visit_Prescription)
        else :
            return render_template('patient_visit.html',doctor=doctor,patient=patient,Name=Name,Age=Age,Gender=Gender,Hypertension=Hypertension,Diabetes=Diabetes,Heart_Disease=Heart_Disease,Asthma=Asthma,Epilepsy=Epilepsy,Stroke=Stroke,Peptic_Ulcer=Peptic_Ulcer,Tuberculosis=Tuberculosis,Surgery=Surgery,Allergy=Allergy,Smoking=Smoking,Drinking=Drinking,Last_Visit_Notes='',Last_Visit_Prescription='')
    if request.method == 'POST' :
        Visit_Notes=request.form['notes']
        Visit_Prescription=request.form['prescription']
        Visit_Details={"Date":datetime.date.today().isoformat(), "Doctor's Notes":Visit_Notes, 'Prescription':Visit_Prescription}
        Patient_Obj.Patient_Stack.append(Visit_Details)
        f = open('Patient Details.pkl','rb')
        g = open('Dummy.pkl','wb')
        while True :
            try :
                Patient = pickle.load(f)
            except EOFError :
                break
            else :
                if Patient.Patient_ID == Patient_Obj.Patient_ID :
                    pickle.dump(Patient_Obj,g)
                else :
                    pickle.dump(Patient,g)
        f.close()
        g.close()
        os.remove('Patient Details.pkl')
        os.rename('Dummy.pkl','Patient Details.pkl')
        return redirect(url_for('choosepatient',doctor=doctor))
    
@app.route('/noappointments', methods=['GET','POST'])
def noappointments() :
    if request.method == 'GET' :
        return render_template('no_app.html')


if __name__ == '__main__':
    app.run(debug=True)

