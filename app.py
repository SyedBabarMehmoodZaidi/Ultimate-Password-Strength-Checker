import streamlit as st
import re

# 🎨 Full Blue Background with White Text Theme
st.markdown("""
    <style>
     /* Overall App */
    .stApp {
        background-color: #001f3f; /* Navy Blue */
        color: white;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }

    /* Paragraphs, spans, labels, divs */
    p, span, div, label {
        color: white !important;
    }

    /* Input text field */
    .stTextInput > div > div > input {
        background-color: #003366;
        color: white;
        border: 1px solid white;
    }

    /* Button Styling */
    div.stButton > button:first-child {
        background-color: #0056b3;
        color: white;
        border: none;
        padding: 0.5em 1em;
        border-radius: 5px;
        font-weight: bold;
    }

    div.stButton > button:first-child:hover {
        background-color: #004080;
        color: white;
    }

    /* Alert boxes */
    .stAlert {
        background-color: #003366;
        color: white;
        border-left: 5px solid #66b2ff;
    }

    /* Footer and misc */
    footer, .css-1v3fvcr {
        color: white;
    }

    /* Markdown content */
    .css-1cpxqw2, .css-1d391kg {
        color: white !important;
    }

    </style>
""", unsafe_allow_html=True)
# 🎉 Title
st.title("🔐 Password Strength Checker ")

# 📝 Description
st.markdown("""
Welcome to the **Password Strength Checker!**  
Simple tool to evaluate your password strength and improve your online security:

📋 Password Requirements:
- ✅ Minimum Length: Password should be at least 8 characters long
- ✅ Upper & Lowercase Letters: Use a mix like Aa for better security
- ✅ Numbers: Include digits like 1, 2, 3 to make it stronger
            
- ✅ Special Characters: Use symbols like !@#$%^&* for added protection
  
""")

# 🏷️ Input Field
password = st.text_input("🔑 Enter your password:", type="password")

# Password Strength Check Function
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least **8 characters** long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include **both uppercase and lowercase** letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least **one number (0-9)**.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least **one special character (!@#$%^&*)**.")

    return score, feedback

# ✅ Button to Check Password
if st.button("🔍 Check Password Strength"):
    if password:
        score, feedback = check_password_strength(password)

        st.subheader("🔒 Password Strength Result:")

        if score == 4:
            st.success("✅ Strong Password! Your password is secure.")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")

        if feedback:
            st.info("💡 Suggestions to improve your password:")
            for tip in feedback:
                st.write(tip)
    else:
        st.error("🚨 Please enter a password to check.")

# 🌟 Footer
st.markdown("""
---
Made with 💙 by **Syed Babar Mehmood Zaidi**
""")
