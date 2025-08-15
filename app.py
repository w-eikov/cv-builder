from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST": #if the user accesses the link through /form, we use the normal method to input data
        name = request.form.get("name") #request.form.get() will return data from the identifier specified in brackets
        email = request.form.get("email")
        phone = request.form.get("phone")
        experiences = request.form.getlist("experience")
        skills = [s.strip() for s in request.form.get("skills", "").split(",") if s.strip()] #since skills is comma separated, we will loop through each skill which has now been separated through commas
        goals = [s.strip() for s in request.form.get("goals", "").split(",") if s.strip()]
        interests = request.form.get("interests")
        return render_template(
            "cv_template.html",
            name=name,
            email=email,
            phone=phone,
            experiences=experiences,
            skills=skills,
            goals = goals,
            interests = interests 
        )
    return render_template("form.html") #if not, (e.g. they go straight to /cv_template) we redirect them back to /form

if __name__ == "__main__":
    app.run(debug=True)