# 🤖 AI-Based Assignment Evaluation System

An AI-powered web application that automatically evaluates student assignments using Natural Language Processing (NLP), semantic similarity, keyword/concept coverage, and automated feedback.

## 📌 Project Overview

The AI-Based Assignment Evaluation System is designed to reduce the manual effort required to evaluate student assignments.

Teachers can create assignments with questions, model answers, keywords, and maximum marks. Students can submit their answers through the web application. The system uses an NLP model to compare student answers with model answers and automatically generates scores and feedback.

## ✨ Features

* Teacher assignment creation
* Multiple questions per assignment
* Model answer configuration
* Keyword/concept configuration
* Student assignment submission
* AI-based semantic similarity
* Keyword/concept coverage analysis
* Automatic marks calculation
* Automated feedback generation
* SQLite database
* Simple web-based interface
* Flask backend
* Sentence Transformers NLP model

## 🛠️ Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### AI / NLP

* Sentence Transformers
* `all-MiniLM-L6-v2`
* Semantic similarity
* Keyword/concept matching

### Database

* SQLite

### Deployment

* AWS Elastic Beanstalk
* Gunicorn

## 📂 Project Structure

```text
AI-Assignment-Evaluation-System/
│
├── app.py
├── database.py
├── evaluator.py
├── schema.sql
├── requirements.txt
├── README.md
├── Procfile
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── create.html
│   ├── submit.html
│   └── result.html
│
└── static/
    └── style.css
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Assignment-Evaluation-System.git
```

### 2. Open the project

```bash
cd AI-Assignment-Evaluation-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

### 7. Open in browser

```text
http://127.0.0.1:5000
```

## 🧠 How AI Evaluation Works

The system compares the student's answer with the model answer using semantic embeddings.

The evaluation process is:

```text
Student Answer
       ↓
Text Processing
       ↓
Sentence Transformer
       ↓
Semantic Embedding
       ↓
Similarity Calculation
       ↓
Keyword/Concept Coverage
       ↓
Rubric-Based Score
       ↓
Feedback Generation
```

The current scoring approach uses:

* 70% semantic similarity
* 30% keyword/concept coverage

The final score is calculated based on the maximum marks assigned to each question.

## 📊 Example

### Question

> What is Artificial Intelligence?

### Model Answer

> Artificial Intelligence is a branch of computer science that develops systems capable of performing tasks that normally require human intelligence.

### Student Answer

> Artificial Intelligence is a field of computer science that allows machines to learn, reason and solve problems similar to humans.

The system analyzes the semantic relationship between the two answers and generates a score and feedback.

## 🖥️ Main Modules

### Teacher Module

* Create assignment
* Add questions
* Add model answers
* Add keywords
* Set maximum marks

### Student Module

* View assignment
* Enter student name
* Submit answers
* Receive evaluation results

### AI Evaluation Module

* Semantic similarity
* Concept/keyword coverage
* Score calculation
* Feedback generation

## 🔮 Future Enhancements

* User authentication
* Teacher and student dashboards
* PDF assignment upload
* DOCX assignment upload
* OCR for scanned assignments
* Handwritten answer recognition
* Advanced LLM-based evaluation
* Plagiarism detection
* Email notifications
* Student performance analytics
* Graphs and reports
* PostgreSQL/MySQL database
* AWS RDS integration
* AWS S3 file storage
* Teacher approval of AI-generated marks

## ⚠️ Important Note

AI-generated scores are intended to assist evaluation. Teachers should review and approve scores before using them as final academic grades.

## 👨‍💻 Author

**YOUR NAME**

GitHub: `https://github.com/YOUR_USERNAME`

## 📄 License

This project is intended for educational and academic purposes.
