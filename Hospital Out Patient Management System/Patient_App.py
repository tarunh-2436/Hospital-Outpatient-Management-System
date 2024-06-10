from flask import Flask, render_template, request, redirect, url_for
import random, pickle, datetime
from functions.classes import TreeNode,Hospital,Patient,Doctor

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('patient_home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        Patients = Hospital.Retrieve_Patients()
        for Patient_Obj in Patients :
            if Patient_Obj.Username == username and Patient_Obj.Password == password :
                return redirect(url_for('doctors',patient=Patient_Obj.Name))
        return render_template('patient_log.html')
    return render_template('patient_log.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        New_Patient = Patient()
        New_Patient.Name = request.form['Name']
        New_Patient.Age = request.form['Age']
        New_Patient.Gender = request.form['Gender']
        New_Patient.Phone_No = request.form['Phone No']
        New_Patient.Address = request.form['Address']
        New_Patient.Username = request.form['Username']
        New_Patient.Password = request.form['Password']
        medical_history = request.form.getlist('Medical History')   
        Medical_Details = {}         
        if 'Hypertension'.upper() in medical_history :
            Medical_Details['Hypertension'] = 'YES'
            Medical_Details['Hypertension Duration'] = request.form['Hypertension Duration']
        else :
            Medical_Details['Hypertension'] = 'NO'
            Medical_Details["Hypertension Duration"] = 'NA'
        if 'Diabetes'.upper() in medical_history :
            Medical_Details['Diabetes'] = 'YES'
            Medical_Details['Diabetes Duration'] = request.form['Diabetes Duration']
        else :
            Medical_Details['Diabetes'] = 'NO'
            Medical_Details["Diabetes Duration"] = 'NA'
        if 'Heart Disease'.upper() in medical_history :
            Medical_Details['Heart Disease'] = 'YES'
            Medical_Details['Heart Disease Duration'] = request.form['Heart Disease Duration']
        else :
            Medical_Details['Heart Disease'] = 'NO'
            Medical_Details["Heart Disease Duration"] = 'NA'
        if ' Bronchial Asthma'.upper() in medical_history :
            Medical_Details['Asthma'] = 'YES'
            Medical_Details['Asthma Duration'] = request.form['Asthma Duration']
        else :
            Medical_Details['Asthma'] = 'NO'
            Medical_Details["Asthma Duration"] = 'NA'
        if 'Epilepsy'.upper() in medical_history :
            Medical_Details['Epilepsy'] = 'YES'
            Medical_Details['Epilepsy Duration'] = request.form['Epilepsy Duration']
        else :
            Medical_Details['Epilepsy'] = 'NO'
            Medical_Details["Epilepsy Duration"] = 'NA'
        if 'Stroke'.upper() in medical_history :
            Medical_Details['Stroke'] = 'YES'
            Medical_Details['Stroke Duration'] = request.form['Stroke Duration']
        else :
            Medical_Details['Stroke'] = 'NO'
            Medical_Details["Stroke Duration"] = 'NA'
        if 'Peptic Ulcer'.upper() in medical_history :
            Medical_Details['Peptic Ulcer'] = 'YES'
            Medical_Details['Peptic Ulcer Duration'] = request.form['Peptic Ulcer Duration']
        else :
            Medical_Details['Peptic Ulcer'] = 'NO'
            Medical_Details["Peptic Ulcer Duration"] = 'NA'
        if 'Tuberculosis'.upper() in medical_history :
            Medical_Details['Tuberculosis'] = 'YES'
            Medical_Details['Tuberculosis Duration'] = request.form['Tuberculosis Duration']
        else :
            Medical_Details['Tuberculosis'] = 'NO'
            Medical_Details["Tuberculosis Duration"] = 'NA'
        if 'Surgical'.upper() in medical_history :
            Medical_Details['Surgery'] = 'YES'
            Medical_Details['Surgery Detailsn'] = request.form['Surgery Details']
        else :
            Medical_Details['Surgery'] = 'NO'
            Medical_Details["Surgery Details"] = 'NA'
        if 'Allergy'.upper() in medical_history :
            Medical_Details['Allergy'] = 'YES'
            Medical_Details['Allergy Details'] = request.form['Allergy Details']
        else :
            Medical_Details['Allergy'] = 'NO'
            Medical_Details["Allergy Details"] = 'NA'
        if 'Smoking'.upper() in medical_history :
            Medical_Details['Smoking'] = 'YES'
        else :
            Medical_Details['Smoking']='NO'
        if 'Drinking'.upper() in medical_history :
            Medical_Details['Drinking'] = 'YES'
        else :
            Medical_Details['Drinking'] = 'NO'
        New_Patient.Medical_Details = Medical_Details
        New_Patient.Patient_ID = New_Patient.generate_patient_ID()

        f = open('Patient Details.pkl','ab')
        pickle.dump(New_Patient,f)
        f.close()

        return redirect(url_for('doctors',patient=New_Patient.Name))
    return render_template('regis.html')

@app.route('/doctors/<patient>', methods=['GET','POST'])
def doctors(patient):
    if request.method=='POST' :
        required_doctor=request.form["Doctor"]
        doctors = Hospital.Retrieve_Doctors()[0]
        for doctor_obj in doctors :
            if doctor_obj.Name == required_doctor :
                return redirect(url_for('appointment',patient=patient, doctor=doctor_obj.Name))
        return render_template('docs(1).html',patient=patient)

    return render_template('docs(1).html',patient=patient)

@app.route('/appointment/<patient>/<doctor>',methods=['GET','POST'])
def appointment(doctor,patient):
    f = open('Hospital Details.pkl','rb')
    BSS = pickle.load(f)
    f.close()
    for Department in BSS.root.children :
            for Doctor in Department.children :
                if Doctor.Name == doctor :
                    Doctor_Obj = Doctor
    for Patient in Hospital.Retrieve_Patients() :
        if Patient.Name == patient :
            Patient_Obj = Patient
            break
    slots = str(Doctor_Obj.Slots)[1:-1]
    if request.method=='GET' :
        return render_template('app.html',name=doctor, slots=slots, patient=patient, doctor=doctor)
    if request.method=='POST' :
        Required_Date = request.form['Date']
        Required_Time = request.form['Time']
        date=datetime.datetime(int(Required_Date[:4]),int(Required_Date[5:7]),int(Required_Date[8:]))
        day_of_week=date.weekday()
        '''Doctor_Obj.Department != 'General Medicine' and day_of_week == 6 or '''
        if Required_Time not in Doctor_Obj.Slots :
            return redirect(url_for('unavailable',patient=patient,doctor=doctor))
        else :
            if Required_Date not in Doctor_Obj.Appointments :
                Doctor_Obj.Appointments[Required_Date] = {Required_Time:Patient_Obj.Patient_ID}
                f = open('Hospital Details.pkl','wb')
                pickle.dump(BSS,f)
                f.close()
                return render_template('success.html')
            else :
                for booked_time in Doctor_Obj.Appointments[Required_Date] :
                    if Required_Time==booked_time :
                        return redirect(url_for('unavailable',patient=patient,doctor=doctor))
                Doctor_Obj.Appointments[Required_Date][Required_Time] = Patient_Obj.Patient_ID
                f = open('Hospital Details.pkl','wb')
                pickle.dump(BSS,f)
                f.close()
                return render_template('success.html')
        
@app.route('/unavailable/<patient>/<doctor>',methods=['GET','POST'])
def unavailable(patient,doctor) :
    if request.method == 'GET' :
        return render_template('fail.html',patient=patient,doctor=doctor)
    if request.method == 'POST' :
        return redirect(url_for('appointment',patient=patient,doctor=doctor))


if __name__ == "__main__" :

    app.run(debug=True)
