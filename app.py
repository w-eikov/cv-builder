from flask import Flask, request, render_template, send_file
import pdfkit
import tempfile
import os

app = Flask(__name__)

# Path to wkhtmltopdf executable (update this to your installation path)
WKHTMLTOPDF_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
pdf_config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Gather form data
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        experiences = request.form.getlist("experience")
        skills = [s.strip() for s in request.form.get("skills", "").split(",") if s.strip()]
        goals = [s.strip() for s in request.form.get("goals", "").split(",") if s.strip()]
        interests = request.form.get("interests")

        # Render CV preview
        return render_template(
            "cv_template.html",
            name=name,
            email=email,
            phone=phone,
            experiences=experiences,
            skills=skills,
            goals=goals,
            interests=interests
        )
    # GET request: show the form
    return render_template("form.html")

@app.route("/preview-cv", methods=["POST"])
def preview_cv():
    # Gather form data
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    
    # Combine multiple experience fields into a list
    experience_str = "\n".join(request.form.getlist("experience"))
    experiences = [e.strip() for e in experience_str.split("\n") if e.strip()]
    
    skills = [s.strip() for s in request.form.get("skills", "").split(",") if s.strip()]
    goals = [s.strip() for s in request.form.get("goals", "").split(",") if s.strip()]
    interests = request.form.get("interests")

    # Render HTML template for preview
    return render_template(
        "cv_template.html",
        name=name,
        email=email,
        phone=phone,
        experiences=experiences,
        skills=skills,
        goals=goals,
        interests=interests
    )


@app.route("/download-cv", methods=["POST"])
def download_cv():
    # Gather form data
    name = request.form.get("name").replace(" ", "_")
    email = request.form.get("email")
    phone = request.form.get("phone")
    experience_str = request.form.get("experience", "")
    experiences = [e.strip() for e in experience_str.split("\n") if e.strip()]
    skills = [s.strip() for s in request.form.get("skills", "").split(",") if s.strip()]
    goals = [s.strip() for s in request.form.get("goals", "").split(",") if s.strip()]
    interests = request.form.get("interests")

    # Render HTML
    rendered = render_template(
        "cv_template.html",
        name=name,
        email=email,
        phone=phone,
        experiences=experiences,
        skills=skills,
        goals=goals,
        interests=interests
    )

    # Create a temporary file for PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
        pdf_file_path = tmpfile.name

    # Generate PDF from HTML
    pdfkit.from_string(rendered, pdf_file_path, configuration=pdf_config)

    # Send PDF to user
    response = send_file(pdf_file_path, as_attachment=True)

    # Delete the temp file after sending
    @response.call_on_close
    def remove_file():
        os.remove(pdf_file_path)

    return response

if __name__ == "__main__":
    app.run(debug=True)
