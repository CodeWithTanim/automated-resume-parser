# app/parser.py

import pdfplumber
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_resume_data(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    doc = nlp(text)

    name = ""
    email = ""
    phone = ""
    skills = []
    education = []

    # Extract email and phone manually
    for token in doc:
        if "@" in token.text and "." in token.text:
            email = token.text
        if token.like_num and len(token.text) >= 10:
            phone = token.text

    # Extract name
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
            break

    # Sample skill set
    skill_keywords = ["python", "java", "sql", "html", "css", "flask", "django", "excel", "c++", "machine learning"]
    skills = [token.text for token in doc if token.text.lower() in skill_keywords]

    # Extract education
    for ent in doc.ents:
        if ent.label_ == "ORG" and "university" in ent.text.lower():
            education.append(ent.text)

    return {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Skills": list(set(skills)),
        "Education": education
    }
