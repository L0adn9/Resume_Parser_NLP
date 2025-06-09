## 📄 AI-Powered Resume Parser using NLP

This project extracts structured information (Name, Email, Skills, Experience) from resumes in `.pdf`, `.docx`, and `.txt` formats using **Python**, **SpaCy**, **Regular Expressions**, and file parsers like **PDFMiner** and **python-docx**.

---

###  Features

* ✅ Parses resumes in **PDF**, **DOCX**, and **TXT** formats
* ✅ Extracts:

  * 👤 Name
  * 📧 Email
  * 💼 Skills
  * 🏢 Experience (title, company, years)
* ✅ Outputs each resume's data in a clean **JSON format**
* ✅ Prints an **accuracy report** summarizing extraction success

---

### 📁 Project Structure

```
resume_parser_project/
├── resumes/          # Folder containing input resumes (.pdf, .docx, .txt)
├── parsed/           # Folder where parsed .json files are saved
├── parser.py         # Main parser logic (NER, regex, etc.)
├── run_parser.py     # Orchestrates parsing and saving output
└── README.md         # This documentation file
```

---

### 🛠 Dependencies

Install required libraries with:

```bash
pip install spacy pdfminer.six python-docx
python -m spacy download en_core_web_sm
```

---

### 🧠 How It Works

The parser uses:

* **SpaCy NER** to detect names
* **Regex** to extract emails, company names, and year ranges
* **Keyword matching** to find skills from a predefined list

Example input (`.txt` file):

```
John Doe
Email: john.doe@example.com

SKILLS:
Python, SQL, Machine Learning

EXPERIENCE:
Data Scientist at TechCorp (2020 - Present)
```

Example output (`.json` file):

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "skills": ["Python", "SQL", "Machine Learning"],
  "experience": [
    {
      "title": "Data Scientist",
      "company": "TechCorp",
      "years": 5
    }
  ]
}
```

---

### ▶️ How to Run

1. Place your resumes inside the `resumes/` folder.
2. Run the script:

```bash
python run_parser.py
```

3. Check parsed JSON files inside the `parsed/` folder.
4. View the printed accuracy report in your terminal.

---

### 📊 Accuracy Report Example

```text
Found file: john_doe.pdf
Parsed and saved: parsed/john_doe.json

Accuracy Report:
Total resumes processed: 1
Name extracted: 1/1
Email extracted: 1/1
Skills extracted: 1/1
Experience extracted: 1/1
```

---

### 🧩 Notes

* Make sure resume text is structured clearly (names on top, bullet skills, “at” in experience lines).
* Company name is only extracted if formatted as:
  `"Job Title at Company (Year - Year)"`

