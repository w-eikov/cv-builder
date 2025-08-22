# Pathbuddy CV Builder

This CV builder is written with **Python**, **Flask**, **JavaScript**, **HTML**, **Jinja2**, and **CSS**.  
It was built as part of work experience from **Pathbuddy**.

## Requirements
* Python Flask must be installed
  ```bash
  pip install flask
  ```
* Python pdfkit must be installed
  ```bash
  pip install pdfkit
  ```
* OpenAI must be installed
  ```bash
  pip install openai
  ```
* python-docx must be installed
  ```bash
  pip install python-docx
  ```
*  wkhtmltopdf must be installed (https://wkhtmltopdf.org/downloads.html)
## How to Use

1. Open 'app.py' with your preferred code editor or terminal and insert your API key in 'openai.api_key = ""'

2. Run `app.py` through your preferred code editor or terminal:

```bash
python app.py
```
3. Open the link that appears in the terminal (usually http://127.0.0.1:5000).
4. Fill in your details, submit the form, and preview/download your generated CV/Cover Letter.

Note: Getting the AI improved cover letters may take a few seconds.

## Features
* Dynamic CV generation using Jinja2 templates
* Input fields for personal details, skills and work experience
* Create a styled CV page in your browser
* Download a styled CV PDF onto your computer (.pdf)
* Dynamic Cover Letter generation using Jinja2 templates
* OpenAI implementation to help further personalise Cover Letters
* Create a styled Cover Letter page in your browser
* Download a styled Cover Letter page onto your computer (.docx)

## Credits
* Adeeb Haidari (<19haidaa@student.handsworth.bham.sch.uk>, github: https://github.com/Link101010)
* Patrik Sandu (<19sandua@student.handsworth.bham.sch.uk>, github: https://github.com/LudwigV7)
* Tinron Chan (<19chant@student.handsworth.bham.sch.uk>, github: https://github.com/w-eikov)
