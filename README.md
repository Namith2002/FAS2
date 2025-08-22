## 👤 Face Attendance System (FAS2)

This is a simple Flask-based **Face Attendance System** that allows users to register with a photo and mark attendance by uploading an image. It uses a pre-trained image classification model (`microsoft/resnet-50`) from Hugging Face Transformers for basic face/image recognition.

---

### 📁 Project Structure

```
FAS2/
│
├── app.py                  # Main Flask application
├── attendance.py           # Handles face recognition logic
├── data/                   # Stores users and attendance records (JSON files)
│   ├── users.json
│   └── attendance.json
├── uploads/                # Stores uploaded photos
├── templates/              # HTML templates (home.html, register.html, etc.)
├── static/                 # Static files like CSS or JS (optional)
└── README.md               # Project overview and usage instructions
```

---

### 🚀 Features

* ✅ User Registration with photo
* ✅ Login and Dashboard (placeholder UI)
* ✅ Image-based attendance marking (Individual & Group mode)
* ✅ JSON-based user and attendance data storage
* ✅ Summary and profile pages (template placeholders)

---

### 🛠️ Tech Stack

* **Backend:** Python, Flask
* **AI/ML:** Hugging Face Transformers (`microsoft/resnet-50`)
* **Templating:** Jinja2 (via Flask)
* **Data Storage:** JSON files (no DB required)

---

### 📦 Requirements

* Python 3.8+
* Install dependencies:

```bash
pip install flask transformers torch torchvision
```

---

### ▶️ How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/Namith2002/FAS2.git
cd FAS2
pip install -r requirements.txt
```

2. **Run the app:**

```bash
python app.py
```

3. **Open in browser:**

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### 📸 How It Works

1. **Register** a new user with name, email, and face photo.
2. The image is classified using `resnet-50`, and the top label is stored as the user's `face_id`.
3. During **attendance**, the uploaded image is classified again.
4. If the label matches any user’s `face_id`, attendance is marked.

---

### 📝 Limitations

* The system uses a general-purpose image classifier (`resnet-50`), not a true face recognition model.
* It only simulates face matching via image labels, which may not work reliably in real-world face recognition use cases.
* Not suitable for production without integrating a proper face recognition library like:

  * `face_recognition`
  * `DeepFace`
  * `OpenCV + Dlib`

---

### ✅ To-Do / Suggestions

* [ ] Replace `resnet-50` with real face embedding & matching (e.g., DeepFace)
* [ ] Add password hashing and login verification
* [ ] Use a database (e.g., SQLite or MongoDB)
* [ ] Add attendance summary charts
* [ ] Support webcam-based attendance

---

### 📃 License

This project is for educational/demo purposes and is **MIT licensed**.

---

Let me know if you'd like me to generate the `README.md` file for download or edit anything else.

