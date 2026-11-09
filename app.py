import os
import sqlite3
from pathlib import Path

from flask import Flask, flash, g, redirect, render_template, request, url_for
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "local-development-key-change-me")
CSRFProtect(app)


def get_db():
    if "db" not in g:
        db_path = Path(os.environ.get("DATABASE_PATH", "instance/gradebook.sqlite3"))
        db_path.parent.mkdir(parents=True, exist_ok=True)
        g.db = sqlite3.connect(db_path)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


@app.teardown_appcontext
def close_db(_error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def initialize_database():
    db = get_db()
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL COLLATE NOCASE UNIQUE
        );
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
            subject TEXT NOT NULL,
            grade REAL NOT NULL CHECK (grade >= 0 AND grade <= 100)
        );
        """
    )
    db.commit()


with app.app_context():
    initialize_database()


@app.get("/")
def index():
    students = get_db().execute(
        """
        SELECT s.id, s.name, COUNT(g.id) AS grade_count,
               ROUND(AVG(g.grade), 2) AS average
        FROM students AS s
        LEFT JOIN grades AS g ON g.student_id = s.id
        GROUP BY s.id
        ORDER BY s.name COLLATE NOCASE
        """
    ).fetchall()
    return render_template("index.html", students=students)


@app.post("/students")
def add_student():
    name = request.form.get("name", "").strip()
    if not name:
        flash("Enter a student name.", "error")
    elif len(name) > 100:
        flash("Student names must be 100 characters or fewer.", "error")
    else:
        try:
            db = get_db()
            db.execute("INSERT INTO students (name) VALUES (?)", (name,))
            db.commit()
            flash(f"Added {name}.", "success")
        except sqlite3.IntegrityError:
            flash("A student with that name already exists.", "error")
    return redirect(url_for("index"))


@app.post("/students/<int:student_id>/grades")
def add_grade(student_id):
    db = get_db()
    student = db.execute("SELECT name FROM students WHERE id = ?", (student_id,)).fetchone()
    if student is None:
        flash("Student not found.", "error")
        return redirect(url_for("index"))

    subject = request.form.get("subject", "").strip()
    grade_text = request.form.get("grade", "").strip()
    try:
        grade = float(grade_text)
    except ValueError:
        grade = None

    if not subject or len(subject) > 100:
        flash("Enter a subject (100 characters or fewer).", "error")
    elif grade is None:
        flash("Enter a numeric grade.", "error")
    elif not 0 <= grade <= 100:
        flash("Grades must be between 0 and 100.", "error")
    else:
        db.execute(
            "INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)",
            (student_id, subject, grade),
        )
        db.commit()
        flash(f"Added a grade for {student['name']}.", "success")
    return redirect(url_for("index"))


@app.post("/students/<int:student_id>/delete")
def delete_student(student_id):
    db = get_db()
    cursor = db.execute("DELETE FROM students WHERE id = ?", (student_id,))
    db.commit()
    flash("Student removed." if cursor.rowcount else "Student not found.", "success" if cursor.rowcount else "error")
    return redirect(url_for("index"))


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
