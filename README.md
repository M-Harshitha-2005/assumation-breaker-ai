# assumation-breaker-ai

# 🧠 Assumption Breaker – AI

An AI-powered web application built with **Streamlit** and **Google Gemini** that helps users identify, challenge, and analyze hidden assumptions behind problem statements.

---

## 🚀 Features

* 🔐 User Authentication (Login & Signup)
* 🔑 Secure password hashing (SHA-256)
* 🤖 AI-based assumption analysis using **Google Gemini**
* 🔄 Automatic model fallback & retry mechanism
* 🧠 Assumption identification, challenge, alternatives & risk analysis
* 📜 Chat history tracking per session
* 📊 Session statistics
* 🚪 Secure logout

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Google Gemini API (New SDK)**
* **dotenv** for environment variables
* **Pandas**
* **Hashlib** for password security

---

## 📂 Project Structure

```
assumption-breaker-ai/
│
├── app.py                 # Main Streamlit application
├── .env                   # Environment variables (API key)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🔑 Environment Setup

Create a `.env` file in the root directory and add:

```
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ Never upload your `.env` file to GitHub.

---

## 📦 Installation

1. Clone the repository

```
git clone https://github.com/your-username/assumption-breaker-ai.git
cd assumption-breaker-ai
```

2. Create a virtual environment (optional but recommended)

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 🧪 How It Works

1. User logs in or creates an account
2. Enters a problem statement
3. Gemini AI:

   * Identifies hidden assumptions
   * Challenges assumptions
   * Suggests alternatives
   * Performs risk analysis
4. Results are displayed and saved in session history

---

## 🔁 AI Model Strategy

* Primary model: `gemini-2.0-flash`
* Fallback model: `gemini-1.5-flash`
* Retry with exponential backoff for reliability

---

## 🔐 Security Notes

* Passwords are **never stored in plain text**
* API key is protected using environment variables
* Session data is isolated per user session

---

## 📌 Example Use Case

> **Problem:** Students are failing exams because they don’t study enough.

The AI reveals hidden assumptions and suggests alternative explanations such as teaching quality, exam design, stress, or learning styles.

---

