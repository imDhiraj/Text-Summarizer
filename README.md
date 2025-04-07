# 📝 Text Summarizer (FastAPI + Transformers)

A simple web application that summarizes long paragraphs of text using a powerful NLP model from HuggingFace Transformers (`facebook/bart-large-cnn`). Built with **FastAPI** for the backend and a minimal **HTML/CSS/JS** frontend.

---

## 🚀 Features

- Accepts raw text input from the user.
- Uses pre-trained BART model to generate a concise summary.
- Fast and lightweight web app.


---

## 🖼️ Demo


<p align="center">
  <img src="https://github.com/user-attachments/assets/ccf9af44-e87a-47f3-b0e8-e37c2eecc7d0"  alt="Image 1" width="45%"/>
  <img src="https://github.com/user-attachments/assets/931bd638-8ca3-4f42-a45d-f82277bc0e45" alt="Image 2" width="45%"/>
</p>


---

## 🧠 Tech Stack

- **Backend**: FastAPI
- **Model**: HuggingFace Transformers (`facebook/bart-large-cnn`)
- **Frontend**: HTML, JavaScript


---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/imDhiraj/Text-Summarizer.git
cd Text-Summarizer

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn app.main:app --reload

