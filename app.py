from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Replace these with your MySQL database credentials
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="utkarsh"  # Change to your database name
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    first_name = request.form.get("firstName")
    last_name = request.form.get("lastName")
    email = request.form.get("email")
    course = request.form.get("course")
    class_name = request.form.get("class")
    rating1 = request.form.get("rating1")
    rating2 = request.form.get("rating2")
    rating3 = request.form.get("rating3")
    rating4 = request.form.get("rating4")
    rating5 = request.form.get("rating5")
    hour = request.form.get("hour")
    minute = request.form.get("minute")
    ampm = request.form.get("ampm")
    review = request.form.get("review")
    comments = request.form.get("comments")

    cursor = db.cursor()
    insert_query = """
    INSERT INTO feedback (first_name, last_name, email, course, class_name, rating1, rating2, rating3, rating4, rating5, hour, minute, ampm, review, comments)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (first_name, last_name, email, course, class_name, rating1, rating2, rating3, rating4, rating5, hour, minute, ampm, review, comments)
    cursor.execute(insert_query, values)
    db.commit()
    cursor.close()

    return "Feedback submitted successfully."

if __name__ == "__main__":
    app.run(debug=True)
