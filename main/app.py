from flask import Flask, request, render_template, send_file
import pdfkit
import tempfile
import os

app = Flask(__name__)

# Path to wkhtmltopdf executable (update if needed)
WKHTMLTOPDF_PATH = r"C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
pdf_config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)


# ---------------- CV ROUTES ----------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index.html")
def go_back_to_index():
    return render_template("/index.html")

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
    return render_template("form.html")


@app.route("/preview-cv", methods=["POST"])
def preview_cv():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    experience_str = "\n".join(request.form.getlist("experience"))
    experiences = [e.strip() for e in experience_str.split("\n") if e.strip()]
    skills = [s.strip() for s in request.form.get("skills", "").split(",") if s.strip()]
    goals = [s.strip() for s in request.form.get("goals", "").split(",") if s.strip()]
    interests = request.form.get("interests")

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
    name = request.form.get("name").replace(" ", "_")
    email = request.form.get("email")
    phone = request.form.get("phone")
    experience_str = request.form.get("experience", "")
    experiences = [e.strip() for e in experience_str.split("\n") if e.strip()]
    skills = [s.strip() for s in request.form.get("skills", "").split(",") if s.strip()]
    goals = [s.strip() for s in request.form.get("goals", "").split(",") if s.strip()]
    interests = request.form.get("interests")

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

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
        pdf_file_path = tmpfile.name

    pdfkit.from_string(
        rendered,
        pdf_file_path,
        configuration=pdf_config,
        options={"enable-local-file-access": ""}
    )


    response = send_file(pdf_file_path, as_attachment=True)

    @response.call_on_close
    def remove_file():
        os.remove(pdf_file_path)

    return response


# ---------------- COVER LETTER ROUTES ----------------

@app.route("/preview-coverletter", methods=["POST"])
def preview_coverletter():
    """Show HTML preview of cover letter"""
    form_data = request.form.to_dict()
    return render_template("cover_letter_template.html", **form_data)


@app.route("/download-coverletter", methods=["POST"])
def download_coverletter():
    """Generate and download cover letter PDF"""
    form_data = request.form.to_dict()
    rendered = render_template("cover_letter_template.html", **form_data)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
        pdf_file_path = tmpfile.name

    pdfkit.from_string(
        rendered,
        pdf_file_path,
        configuration=pdf_config,
        options={"enable-local-file-access": ""}
    )


    response = send_file(pdf_file_path, as_attachment=True)

    @response.call_on_close
    def remove_file():
        os.remove(pdf_file_path)

    return response


if __name__ == "__main__":
    app.run(debug=True)
