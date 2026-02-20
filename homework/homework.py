from flask import Flask, render_template, request, redirect, url_for

from exercises.ninja_exercise import grades

app = Flask(__name__)

# In-memory storage
students = []


@app.route("/")
def home():
    return redirect(url_for("add_student"))


# ---------------------------------
# TODO: IMPLEMENT THIS ROUTE
# ---------------------------------

@app.route("/add", methods=["GET", "POST"])
def add_student():

    error = None
    name = ""
    grade = ""

    if request.method == "POST":
        name = request.form.get("name")
        grade = request.form.get("grade")

        # TODO:
        # 1. Validate name
        if not name:
            error = "Name is empty"

        # 2. Validate grade is number
        else:
            try:
                grade = float(grade)
            except ValueError:
                error = "Grade is not a number"
        # 3. Validate grade range 0–100
        if not error and (grade < 0 or grade > 100):
            error = "Grade is out of range"
        # 4. Add to students list as dictionary
        if not error:
            students.append({"name": name, "grade" : grade})

        # 5. Redirect to /students
            return redirect(url_for("display_students"))




    return render_template("add.html", error=error, name=name, grade=grade)


# ---------------------------------
# TODO: IMPLEMENT DISPLAY
# ---------------------------------
@app.route("/students")
def display_students():
    return render_template("students.html", students=students)


# ---------------------------------
# TODO: IMPLEMENT SUMMARY
# ---------------------------------
@app.route("/summary")
def summary():
    # TODO:
    # Calculate:
    # - total students
    friendly_message=None
    if len(students) == 0:
        friendly_message = "There are no students"
        return render_template("summary.html", friendly_message=friendly_message)
    grades = []
    for student in students:
        grades.append(student["grade"])
    total = len(students)

    # - average grade
    avg = sum(grades)/ total


    # - highest grade
    highest = max(grades)

    # - lowest grade
    lowest = min(grades)

    return render_template("summary.html", total=total, average=avg, highest=highest, lowest=lowest, friendly_message=friendly_message)


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
