from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Courses Page
@app.route("/courses")
def courses():
    return render_template("courses.html")


# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/computer_fundamentals")
def computer_fundamentals():
    return render_template("computer_fundamentals.html")


@app.route("/OSandFM")
def OSandFM():
    return render_template("OSandFM.html")


@app.route("/internet_browsing")
def internet_browsing():
    return render_template("internet_browsing.html")


@app.route("/file_management")
def file_management():
    return render_template("file_management.html")


@app.route("/typing_skills")
def typing_skills():
    return render_template("typing_skills.html")


@app.route("/msword")
def msword():
    return render_template("msword.html")


@app.route("/mspowerpoint")
def mspowerpoint():
    return render_template("mspowerpoint.html")


@app.route("/mssheets")
def mssheets():
    return render_template("mssheets.html")

@app.route("/websitecreation")
def websitecreation():
    return render_template("websitecreation.html")

@app.route("/intro_to_coding")
def intro_to_coding():
    return render_template("intro_to_coding.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)