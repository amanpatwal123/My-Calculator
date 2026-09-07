import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="Ultra Smart Calculator 🧮", page_icon="🧮", layout="centered")

# Custom CSS for Phone Calculator UI
st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
    }
    .main .block-container {
        max-width: 360px;
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .stButton > button {
        width: 100%;
        height: 58px;
        font-size: 22px !important;
        font-weight: bold;
        border-radius: 50px;
        border: none;
        background-color: #2a2a2a;
        color: white;
        margin-bottom: 4px;
    }
    .stButton > button:hover {
        background-color: #3a3a3a;
        color: white;
    }
    /* Display Screen Styling */
    div[data-baseweb="input"] input {
        font-size: 30px !important;
        text-align: right;
        color: #00ffcc !important;
        background-color: #1e1e1e !important;
        border-radius: 12px;
        height: 70px;
    }
    /* Prank Box Styling */
    .prank-box {
        background-color: #2d1313;
        color: #ff4d4d;
        padding: 15px;
        border-radius: 12px;
        border: 2px solid #ff4d4d;
        text-align: center;
        margin-top: 15px;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Session States Initialize karna
if "display" not in st.session_state:
    st.session_state.display = ""
if "prank_msg" not in st.session_state:
    st.session_state.prank_msg = ""

# Aapke Code Ke Funny Responses
funny_multiplication = [
    "I don't Know 999 🤐",
    "You are not a 6 year old boy, do it yourself! 🤣"
]

funny_division = [
    "You are duffer! 🤦‍♂️",
    "Abe khud bhi krr le kuch! 😂"
]

funny_subtraction = [
    "Kathu ko bulau? 👻",
    "Ya maths wale sir ko? 👨‍🏫"
]

funny_addition = [
    "Abe Add krrna bhi nhi ara kya? 🤡",
    "Itna simple plus khud kar le bhai! 😜"
]

funny_errors = [
    "Abe ulta paida hua tha kya? 🤪",
    "Error 404: Calculator Is Busy! 🤖"
]

# Button Click Handle karne ka Function
def press(val):
    expr = st.session_state.display

    if val == "C":
        st.session_state.display = ""
        st.session_state.prank_msg = ""
    elif val == "⌫":
        st.session_state.display = expr[:-1]
    elif val == "=":
        if "*" in expr:
            st.session_state.prank_msg = random.choice(funny_multiplication)
        elif "/" in expr:
            st.session_state.prank_msg = random.choice(funny_division)
        elif "-" in expr:
            st.session_state.prank_msg = random.choice(funny_subtraction)
        elif "+" in expr:
            st.session_state.prank_msg = random.choice(funny_addition)
        else:
            st.session_state.prank_msg = random.choice(funny_errors)
        
        # Result "Calculator is busy" error show karega
        st.session_state.display = "Error 404"
    else:
        if st.session_state.display == "Error 404":
            st.session_state.display = ""
        st.session_state.display += str(val)

# Title
st.markdown("<h3 style='text-align: center; color: white;'>Pro Calculator 🧮</h3>", unsafe_allow_html=True)

# Main Display Screen
disp = st.session_state.display if st.session_state.display != "" else "0"
st.text_input("", value=disp, disabled=True, label_visibility="collapsed")

# Prank Dialogue Box
if st.session_state.prank_msg:
    st.markdown(f"<div class='prank-box'>{st.session_state.prank_msg}</div>", unsafe_allow_html=True)

st.write("")

# Touch Buttons Layout (Phone Format)
buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "00", "="]
]

# Grid Buttons Render karna
for row in buttons:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        cols[i].button(btn, on_click=press, args=(btn,))
