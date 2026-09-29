# AI-Based Assignment Evaluation System

A Flask + SQLite project that evaluates assignment answers using NLP semantic similarity and a simple rubric.

## Features
- Create assignments and questions
- Add model answers, keywords and maximum marks
- Student submission page
- AI/NLP semantic evaluation using Sentence Transformers
- Automatic score and feedback
- SQLite database
- Simple responsive web UI

## Run
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

The first evaluation downloads the `all-MiniLM-L6-v2` model.

AI scores should be reviewed by a teacher before final publication.
