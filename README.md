#  Equity Research Intelligence Portal

A specialized Full-Stack application designed to automate the analysis of financial earnings transcripts. This tool uses Generative AI to parse complex PDF documents and extract strategic management insights in seconds.

---

##  Project Overview
This portal solves the problem of manually scanning through 50+ pages of earnings calls. it identifies sentiment, growth strategies, and operational risks, providing a structured summary for equity research analysts.

---

##  Key Features
* **Automated PDF Parsing:** High-precision text extraction from financial documents.
* **Structured Intelligence:** Extracts Tone, Confidence Level, Positives, Challenges, and Forward Guidance.
* **Hallucination Control:** Built with strict grounding to ensure AI only reports what is in the document.
* **Professional UI:** Modern, clean interface for seamless document uploads.

---

##  Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Frontend** | React.js, Axios, CSS Modules |
| **Backend** | FastAPI (Python), PyPDF2, Uvicorn |
| **AI Engine** | Cohere AI (Latest Chat API) |
| **DevOps** | Git, 

---
Live Demo:[varcel](https://research-portal-assignment-jeerank10-6837s-projects.vercel.app/)
Backend API: [render](https://research-portal-assignment.onrender.com/docs)

##  How to Run Locally

### 1. Backend Setup
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload