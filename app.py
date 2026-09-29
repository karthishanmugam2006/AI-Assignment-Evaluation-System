from flask import Flask, render_template, request, redirect, url_for, abort
from database import get_connection, init_db
from evaluator import evaluate_answer

app = Flask(__name__)

@app.route("/")
def index():
    conn = get_connection()
    assignments = conn.execute("SELECT * FROM assignments ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("index.html", assignments=assignments)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"].strip()
        description = request.form["description"].strip()

        conn = get_connection()
        cur = conn.execute(
            "INSERT INTO assignments(title, description) VALUES (?, ?)",
            (title, description)
        )
        assignment_id = cur.lastrowid

        i = 1
        while request.form.get(f"question_{i}"):
            conn.execute(
                """INSERT INTO questions
                (assignment_id, question, model_answer, keywords, max_marks)
                VALUES (?, ?, ?, ?, ?)""",
                (
                    assignment_id,
                    request.form[f"question_{i}"],
                    request.form[f"model_answer_{i}"],
                    request.form.get(f"keywords_{i}", ""),
                    int(request.form.get(f"max_marks_{i}", 10))
                )
            )
            i += 1

        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    return render_template("create.html")

@app.route("/submit/<int:assignment_id>", methods=["GET", "POST"])
def submit(assignment_id):
    conn = get_connection()
    assignment = conn.execute(
        "SELECT * FROM assignments WHERE id=?", (assignment_id,)
    ).fetchone()
    questions = conn.execute(
        "SELECT * FROM questions WHERE assignment_id=? ORDER BY id",
        (assignment_id,)
    ).fetchall()

    if not assignment:
        conn.close()
        abort(404)

    if request.method == "POST":
        student = request.form["student_name"].strip()
        cur = conn.execute(
            "INSERT INTO submissions(assignment_id, student_name) VALUES (?,?)",
            (assignment_id, student)
        )
        submission_id = cur.lastrowid

        for q in questions:
            answer = request.form.get(f"answer_{q['id']}", "").strip()
            sim, cov, score, feedback = evaluate_answer(
                answer, q["model_answer"], q["keywords"], q["max_marks"]
            )
            conn.execute(
                """INSERT INTO answers
                (submission_id, question_id, student_answer, similarity,
                 keyword_score, final_score, feedback)
                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (submission_id, q["id"], answer, sim, cov, score, feedback)
            )

        conn.commit()
        conn.close()
        return redirect(url_for("result", submission_id=submission_id))

    conn.close()
    return render_template("submit.html", assignment=assignment, questions=questions)

@app.route("/result/<int:submission_id>")
def result(submission_id):
    conn = get_connection()
    submission = conn.execute(
        "SELECT * FROM submissions WHERE id=?", (submission_id,)
    ).fetchone()
    answers = conn.execute(
        """SELECT a.*, q.question, q.max_marks
           FROM answers a JOIN questions q ON a.question_id=q.id
           WHERE a.submission_id=? ORDER BY a.id""",
        (submission_id,)
    ).fetchall()
    conn.close()

    if not submission:
        abort(404)

    total = sum(x["final_score"] for x in answers)
    maximum = sum(x["max_marks"] for x in answers)
    percentage = round(total * 100 / maximum, 2) if maximum else 0

    return render_template(
        "result.html", submission=submission, answers=answers,
        total=total, maximum=maximum, percentage=percentage
    )

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
