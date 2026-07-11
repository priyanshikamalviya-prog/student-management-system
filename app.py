from flask import Flask, render_template, request, redirect, flash

from database import (
    add_student,
    get_all_students,
    get_total_students,
    search_student,
    update_student,
    delete_student
)

app = Flask(__name__)
app.secret_key = "student123"


# =========================
# HOME PAGE
# =========================
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        student_id = request.form["student_id"]
        name = request.form["name"]
        age = int(request.form["age"])
        course = request.form["course"]
        email = request.form["email"]

        add_student(student_id, name, age, course, email)
        flash("Student Added Successfully!")

        return redirect("/")

    students = get_all_students()
    total_students = get_total_students()

    return render_template(
        "index.html",
        students=students,
        total_students=total_students
    )


# =========================
# SEARCH STUDENT
# =========================
@app.route("/search", methods=["POST"])
def search():

    student_id = request.form["student_id"]

    student = search_student(student_id)

    students = []

    if student:
        students.append(student)

    return render_template(
        "index.html",
        students=students,
        total_students=get_total_students()
    )


# =========================
# EDIT PAGE
# =========================
@app.route("/edit/<student_id>")
def edit(student_id):

    student = search_student(student_id)

    return render_template("edit.html", student=student)


# =========================
# UPDATE STUDENT
# =========================
@app.route("/update", methods=["POST"])
def update():

    student_id = request.form["student_id"]
    name = request.form["name"]
    age = int(request.form["age"])
    course = request.form["course"]
    email = request.form["email"]

    update_student(student_id, name, age, course, email)

    flash("Student Updated Successfully!")

    return redirect("/")


# =========================
# DELETE STUDENT
# =========================
@app.route("/delete/<student_id>")
def delete(student_id):

    delete_student(student_id)

    flash("Student Deleted Successfully!")

    return redirect("/")


# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)