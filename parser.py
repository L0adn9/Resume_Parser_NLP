import os
import re
import json
import spacy
from pdfminer.high_level import extract_text
from docx import Document

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(path):
    return extract_text(path)

def extract_text_from_docx(path):
    doc = Document(path)
    lines = []
    for p in doc.paragraphs:
        lines.append(p.text)
    return '\n'.join(lines)


def extract_text_from_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

#  Parsing Resume 


def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
            if ent.label_ == "PERSON" and len(ent.text.split()) <= 4:
                return ent.text
    return None

def extract_email(text):
    email = re.findall(r"\S+@\S+", text)
    email = email[0] if email else None

def extract_experience(text):
    experience = []
    lines = text.splitlines()
    pattern = re.compile(
        r"(Data Scientist|Data Analyst|Software Engineer|.*Analyst)\s+at\s+([A-Za-z0-9 &]+)\s*\(?(\d{4})\)?\s*[-–]\s*\(?(\d{4}|Present)\)?",
        re.IGNORECASE
    )

    for line in lines:
        match = pattern.search(line)
        if match:
            title = match.group(1).strip()
            company = match.group(2).strip()
            start_year = int(match.group(3))
            end_year = 2025 if match.group(4).lower() == "present" else int(match.group(4))
            years = end_year - start_year
            experience.append({
                "title": title,
                "company": company if company else "Unknown",
                "years": years
            })
    return experience


def parse_resume(text):
    doc = nlp(text)

    #getting Name
    name = extract_name(text)
    if not name:
        name = "Unknown"

    # getting email
    email = re.findall(r"\S+@\S+", text)

    
    # getting skills 
    possible_skills = ["Python", "Java", "Machine Learning", "AWS", "SQL"]
    skills = []
    for skill in possible_skills:
        if skill.lower() in text.lower():
            skills.append(skill)
    

    resume = {
        "name": name,
        "email": email[0] if email else None,
        "skills": skills
    }

    resume["experience"] = extract_experience(text)

    return resume