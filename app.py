from flask import Flask, render_template, request, redirect, url_for, jsonify 
from transformers import pipeline
from werkzeug.utils import secure_filename
import os
import json
import time
from datetime import datetime

# 🔧 Import only recognize_faces (not recognize_multiple_faces)
from attendance import recognize_faces

app = Flask(__name__, static_folder='static')

uploads_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)

data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

users_db_path = os.path.join(data_dir, 'users.json')
attendance_db_path = os.path.join(data_dir, 'attendance.json')

if not os.path.exists(users_db_path):
    with open(users_db_path, 'w') as f:
        json.dump([], f)

if not os.path.exists(attendance_db_path):
    with open(attendance_db_path, 'w') as f:
        json.dump([], f)

# 🧹 Removed local face_recognition pipeline - handled in attendance.py

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if request.method == 'POST':
        if 'image' not in request.files:
            return render_template('attendance.html', error='No file part')
        
        file = request.files['image']
        if file.filename == '':
            return render_template('attendance.html', error='No selected file')
        
        filename = secure_filename(file.filename)
        file_path = os.path.join(uploads_dir, filename)
        file.save(file_path)

        attendance_mode = request.form.get('mode', 'individual')

        try:
            with open(users_db_path, 'r') as f:
                users = json.load(f)

            recognized_users = []
            results_text = ""

            # 🔧 Treat both individual and group as same (since only one face recog function exists)
            recognition_results = recognize_faces(file_path)

            if not recognition_results:
                results_text = "No faces detected in the image."
            else:
                recognized_count = 0
                for result in recognition_results:
                    label = result['label']
                    score = result['score']
                    
                    for user in users:
                        if user.get('face_id') and label.lower() in user['face_id'].lower():
                            record_attendance(user['username'])
                            recognized_users.append({
                                'username': user['username'],
                                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            })
                            recognized_count += 1
                            break

                if recognized_count > 0:
                    results_text = f"Attendance marked successfully! Recognized {recognized_count} user(s)."
                else:
                    results_text = "No registered users recognized. Please register first."

            return render_template('attendance.html', 
                                  results=results_text, 
                                  recognized_users=recognized_users,
                                  mode=attendance_mode)
        except Exception as e:
            return render_template('attendance.html', error=str(e))
    
    return render_template('attendance.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        if 'photo' not in request.files:
            return render_template('register.html', error='No photo uploaded')
        
        photo = request.files['photo']
        if photo.filename == '':
            return render_template('register.html', error='No photo selected')
        
        filename = secure_filename(f"{username}_{int(time.time())}.jpg")
        photo_path = os.path.join(uploads_dir, filename)
        photo.save(photo_path)

        try:
            results = recognize_faces(photo_path)
            face_id = results[0]['label'] if results else "unknown"

            users = []
            if os.path.exists(users_db_path):
                with open(users_db_path, 'r') as f:
                    users = json.load(f)

            new_user = {
                'username': username,
                'email': email,
                'face_id': face_id,
                'photo_path': photo_path,
                'registered_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            users.append(new_user)

            with open(users_db_path, 'w') as f:
                json.dump(users, f, indent=4)

            return render_template('register.html', success=f"User {username} registered successfully!")
        except Exception as e:
            return render_template('register.html', error=f"Error processing face: {str(e)}")
    
    return render_template('register.html')

def record_attendance(username):
    attendance_records = []
    if os.path.exists(attendance_db_path):
        with open(attendance_db_path, 'r') as f:
            attendance_records = json.load(f)

    new_record = {
        'username': username,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'date': datetime.now().strftime('%Y-%m-%d')
    }

    attendance_records.append(new_record)

    with open(attendance_db_path, 'w') as f:
        json.dump(attendance_records, f, indent=4)

@app.route('/attendance_summary')
def attendance_summary():
    return render_template('attendance_summary.html')

@app.route('/user_profile')
def user_profile():
    return render_template('user_profile.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

if __name__ == '__main__':
    app.run(debug=True)
