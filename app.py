# ==============================
# ASSUMPTION BREAKER – AI
# FINAL CLEAN WORKING CODE
# ==============================

import os
import datetime
import hashlib
import time

import streamlit as st
import pandas as pd
from dotenv import load_dotenv

from google import genai
from google.genai import errors

# ---------------------------
# Load API Key
# ---------------------------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Gemini API Key missing")
    st.stop()

# Initialize Gemini Client (NEW SDK)
client = genai.Client(api_key=api_key)

# ---------------------------
# Session State Initialization
# ---------------------------
if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_user" not in st.session_state:
    st.session_state.current_user = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------------------
# Helper Functions
# ---------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_ai_response(prompt):
    models = ["gemini-2.0-flash", "gemini-1.5-flash"]  # primary + fallback
    max_retries = 5

    for attempt in range(max_retries):
        for model in models:
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )
                return response.text.strip()
            except Exception as e:
                print(f"Attempt {attempt+1}, model {model} failed: {e}")
                time.sleep(2 * (attempt + 1))  # exponential backoff

    return "⚠️ Gemini servers are busy. Please try again later."


# ---------------------------
# Authentication UI
# ---------------------------
st.title("🧠 Assumption Breaker – AI")

if not st.session_state.logged_in:
    tab1, tab2 = st.tabs(["🔐 Login", "📝 Create Account"])

    with tab1:
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if (
                username in st.session_state.users
                and st.session_state.users[username] == hash_password(password)
            ):
                st.session_state.logged_in = True
                st.session_state.current_user = username
                st.success("✅ Login Successful")
                st.rerun()
            else:
                st.error("❌ Invalid credentials")

    with tab2:
        st.subheader("Create Account")
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Create Account"):
            if new_user in st.session_state.users:
                st.warning("⚠️ User already exists")
            else:
                st.session_state.users[new_user] = hash_password(new_pass)
                st.success("✅ Account Created")

    st.stop()

# ---------------------------
# Main Application
# ---------------------------
st.subheader(f"Welcome, {st.session_state.current_user} 👋")

problem = st.text_area(
    "📌 Enter a Problem Statement",
    placeholder="Example: Students are failing exams because they don’t study enough."
)

if st.button("🔍 Break Assumptions") and problem.strip():
    prompt = f"""
Problem Statement:
{problem}

1. Identify hidden assumptions behind this problem.
2. Challenge each assumption logically.
3. Suggest alternative viewpoints or solutions.
4. Perform risk analysis if assumptions are incorrect.

Use clear headings and bullet points.
"""

    with st.spinner("Analyzing assumptions..."):
        ai_response = generate_ai_response(prompt)

    record = {
        "time": datetime.datetime.now(),
        "problem": problem,
        "analysis": ai_response
    }

    st.session_state.chat_history.append(record)
    st.success("✅ Analysis Completed")

# ---------------------------
# Display Latest Analysis
# ---------------------------
if st.session_state.chat_history:
    st.subheader("🧠 AI Analysis Output")
    st.markdown(st.session_state.chat_history[-1]["analysis"])

# ---------------------------
# Sidebar – Chat History
# ---------------------------
st.sidebar.subheader("📜 Chat History")
for i, chat in enumerate(reversed(st.session_state.chat_history)):
    st.sidebar.write(f"{i+1}. {chat['problem'][:40]}...")

# ---------------------------
# Sidebar – Session Summary
# ---------------------------
st.sidebar.subheader("📊 Session Stats")
st.sidebar.write("Total Problems Analyzed:", len(st.session_state.chat_history))

# ---------------------------
# Logout
# ---------------------------
if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.session_state.current_user = None
    st.rerun()
