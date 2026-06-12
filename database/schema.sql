CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role ENUM('patient','doctor','admin','staff'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    age INT,
    gender VARCHAR(10),
    weight FLOAT,
    height FLOAT,
    blood_group VARCHAR(10),
    allergies TEXT,
    medical_history TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    specialization VARCHAR(100),
    experience INT,
    qualification VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    appointment_date DATETIME,
    status VARCHAR(30),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

CREATE TABLE medical_records (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    diagnosis TEXT,
    prescription TEXT,
    report_path VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

CREATE TABLE prescriptions (
    prescription_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    medicines TEXT,
    dosage TEXT,
    instructions TEXT
);

CREATE TABLE reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    report_type VARCHAR(100),
    file_path VARCHAR(255),
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE beds (
    bed_id INT AUTO_INCREMENT PRIMARY KEY,
    ward_name VARCHAR(50),
    bed_type VARCHAR(50),
    status VARCHAR(30)
);

CREATE TABLE resources (
    resource_id INT AUTO_INCREMENT PRIMARY KEY,
    resource_name VARCHAR(100),
    quantity INT,
    available_quantity INT
);

CREATE TABLE staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    staff_name VARCHAR(100),
    department VARCHAR(100),
    role VARCHAR(100)
);

CREATE TABLE schedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    staff_id INT,
    shift_date DATE,
    shift_type VARCHAR(50),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
);

CREATE TABLE notifications (
    notification_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    message TEXT,
    status VARCHAR(30),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE disease_predictions (
    prediction_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    disease_name VARCHAR(100),
    risk_score FLOAT,
    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE treatment_recommendations (
    recommendation_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    disease_name VARCHAR(100),
    specialist VARCHAR(100),
    recommended_tests TEXT,
    medications TEXT
);

CREATE TABLE outcome_predictions (
    outcome_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    recovery_probability FLOAT,
    icu_risk FLOAT,
    expected_stay_days INT
);

CREATE TABLE chatbot_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    user_query TEXT,
    bot_response TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE emergency_alerts (
    alert_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    alert_type VARCHAR(100),
    alert_status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE audit_logs (
    audit_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action_performed TEXT,
    action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
