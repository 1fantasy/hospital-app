from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

DB_CONFIG = {
    "host": "localhost",
    "database": "hospital_db",
    "user": "postgres",
    "password": "adrielandme2007",
    "port": "5432"
}

def get_data(query):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

@app.route("/")
def index():
    patients = get_data("SELECT Name, Age, Gender, Admission_Status FROM Patients;")
    doctors = get_data("SELECT Name, Specialty FROM Doctors;")
    wards = get_data("SELECT Ward_Name, Capacity, Current_Occupancy FROM Wards;")
    appointments = get_data("""
        SELECT a.Appointment_ID, p.Name, d.Name, a.Date, a.Time, a.Purpose
        FROM Appointment a
        JOIN Patients p ON a.Patient_ID = p.Patient_ID
        JOIN Doctors d ON a.Doctor_ID = d.Doctor_ID;
    """)
    billing = get_data("""
        SELECT b.Bill_ID, p.Name, b.Total_Amount, b.Payment_Status
        FROM Billing b
        JOIN Patients p ON b.Patient_ID = p.Patient_ID;
    """)

    return render_template("index.html",
                           patients=patients,
                           doctors=doctors,
                           wards=wards,
                           appointments=appointments,
                           billing=billing)

if __name__ == "__main__":
    app.run(debug=True)
