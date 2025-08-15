# Pathbuddy CV Builder

This CV builder is written with **Python**, **Flask**, **HTML**, and **Jinja2**.  
It was built as part of work experience from **Pathbuddy**.

## Requirements
* Python Flask must be installed
* Python pdfkit must be installed
* wkhtmltopdf must be installed (https://wkhtmltopdf.org/downloads.html)
## How to Use

1. Run `app.py` through your preferred code editor or terminal:

```bash
python app.py
```
2. Open the link that appears in the terminal (usually http://127.0.0.1:5000).
3. Navigate to the form page by changing the URL to:
``` bash
http://127.0.0.1:5000/form
```
4. Fill in your details, submit the form, and view your generated CV.

## Features
* Dynamic CV generation using Jinja2 templates
* Input fields for personal details, skills and work experience
* Create a styled CV page in your browser
* Download a styled CV PDF onto your computer
