import os
import json
from parser import extract_text_from_pdf, extract_text_from_docx, extract_text_from_txt, parse_resume

# Accuracy counters
total_resumes = 0
name_found = 0
email_found = 0
skills_found = 0
experience_found = 0


resumes_folder = "resumes"
output_folder = "parsed"

os.makedirs(output_folder, exist_ok=True)


for filename in os.listdir(resumes_folder):
    print(f"Found file: {filename}")  

    file_path = os.path.join(resumes_folder, filename)


    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    elif filename.endswith(".txt"):
        text = extract_text_from_txt(file_path)
    else:
        print(f"Skipping unsupported file: {filename}")
        continue

    parsed_data = parse_resume(text)
    
    total_resumes += 1
    if parsed_data.get("name"):
        name_found += 1
    if parsed_data.get("email"):
        email_found += 1
    if parsed_data.get("skills"):
        skills_found += 1
    if parsed_data.get("experience"):
        experience_found += 1

    
    json_path = os.path.join(output_folder, filename.rsplit('.', 1)[0] + ".json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(parsed_data, f, indent=2)
    
    print(f"Parsed and saved: {json_path}\n")

print("\nAccuracy Report:")
print(f"Total resumes processed: {total_resumes}")
print(f"Name extracted: {name_found}/{total_resumes}")
print(f"Email extracted: {email_found}/{total_resumes}")
print(f"Skills extracted: {skills_found}/{total_resumes}")
print(f"Experience extracted: {experience_found}/{total_resumes}")
