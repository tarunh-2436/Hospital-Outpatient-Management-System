# Hospital Outpatient Management System
The Hospital Outpatient Management System is a software solution developed for BSS Hospital to streamline and digitize the process of managing outpatient appointments and patient data. The system provides a user-friendly interface for both patients and doctors, simplifying patient registration, appointment scheduling, and the maintenance of medical records.

## ✨ Features
### Patient Module
**New Patient Registration:** New patients can register by providing their basic details and filling out a medical history form. A unique Patient ID is generated upon successful registration.

**Secure Login:** Registered patients can log in to their accounts.

**Appointment Scheduling:** Patients can view a list of available doctors, their specializations, and their consultation time slots, and book an appointment accordingly.

**Data Submission:** Collects preliminary information from the patient, which is made available to the doctor before the consultation.

### Doctor Module
**Secure Doctor Login:** Doctors have a separate login to access their dashboard.

**Daily Schedule View:** Doctors can view their list of appointments for the current day, including patient IDs and scheduled times.

**Patient Information Access:** Doctors can retrieve and view a patient's complete medical history and details from their previous visits.

**Consultation Notes:** Provides an interface for doctors to enter and save their diagnosis and prescription for the current visit.

## 🛠️ Technology Stack
**Backend:** Python

**Web Framework:** Flask (Used to create the web server and handle routing)

**Frontend:** HTML5 & CSS3 (For structuring and styling the web pages)

**Data Storage:** Pickle Module (Used for serializing Python objects and storing data in binary files for persistent backup)

## 🚀 Setup and Usage
To run this project on your local machine, please follow these steps.

### Prerequisites
Python 3.x and pip installed.

### Installation
Clone the repository:
```
git clone https://github.com/your-username/hospital-management-system.git
cd hospital-management-system
```
Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install the required dependencies:
```
pip install Flask
```
Run the application:
```
python app.py  # Or your main Python file name
```
The application will be running at http://127.0.0.1:5000. Open this URL in your web browser.

### Project Link: https://github.com/tarunh-2436/Hospital-Outpatient-Management-System
