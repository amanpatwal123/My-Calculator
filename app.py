import streamlit as st
import random

# Page Configuration - Wide & Centered
st.set_page_config(page_title="Ultra Smart Calculator 🧮", page_icon="🧮", layout="centered")

# Responsive CSS - Fixed Mobile Alignment
st.markdown("""
    <style>
    /* Full Page Background & Centering */
    .stApp {
        background-color: #121212;
    }
    .main .block-container {
        max-width: 350px !important;
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        padding-left: 10px !important;
        padding-right: 10px !important;
        margin: 0 auto !important;
    }
    
    /* Column Grid Reset (Fixes Left Shift Glitch) */
    div[data-testid="column"] {
        padding: 2px !important;
        min-width: 0px !important;
    }
    div[data-testid="stHorizontalBlock"] {
        gap: 0px !important;
    }

    /* Touch Button Design */
    .stButton > button {
        width: 100% !important;
        height: 60px !important;
        font-size: 22px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
        border: none !important;
        background-color: #2a2a2a !important;
        color: white !important;
        margin: 0 !important;
    }
    .stButton > button:hover {
        background-color: #3a3a3a !important;
        color: white !important;
    }

    /* Display Screen Styling */
    div[data-baseweb="input"] input {
        font-size: 32px !important;
        text-align: right !important;
        color: #00ffcc !important;
        background-color: #1e1e1e !important;
        border-radius: 12px !important;
        height: 70px !important;
        padding-right: 15px !important;
    }

    /* Prank Response Box */
    .prank-box {
        background-color: #2d1313;
        color: #ff4d4d;
        padding: 12px;
        border-radius: 12px;
        border: 2px solid #ff4d4d;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 10px;
        font-size: 16px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Session States Initialize
if "display" not in st.session_state:
    st.session_state.display = ""
if "prank_msg" not in st.session_state:
    st.session_state.prank_msg = ""

# Funny Responses List
funny_multiplication = [
    "I don't Know 999 🤐",
    "do it yourself! 🤣"
    "Abe dharti mai bhoj khud krr ise"
]

funny_division = [
    "You are duffer! 🤦‍♂️",
    "Abe khud bhi krr le kuch! 😂"
    "Chulu bhar pani mai dub ke marr ja"
]

funny_subtraction = [
    "Kathu ko bulau? 👻",
    "Ya maths wale sir ko? 👨‍🏫"
    "Gand mrwale itna ni ara to"
]

funny_addition = [
    "Abe Add krrna bhi nhi ara kya? 🤡",
    "Itna simple plus khud kar le bhai! 😜"
    "Tu glt hi paida hua mc"
]

funny_errors = [
    "Abe ulta paida hua tha kya? 🤪",
    "Error 404: Calculator Is Busy! 🤖"
    "Gandu ke bache"
]

# Button Click Handle Function
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
        
        st.session_state.display = "Error 404"
    else:
        if st.session_state.display == "Error 404":
            st.session_state.display = ""
        st.session_state.display += str(val)

# Title
st.markdown("<h3 style='text-align: center; color: white; margin-bottom: 10px;'>Pro Calculator 🧮</h3>", unsafe_allow_html=True)

# Main Display Screen
disp = st.session_state.display if st.session_state.display != "" else "0"
st.text_input("", value=disp, disabled=True, label_visibility="collapsed")

# Prank Message Display
if st.session_state.prank_msg:
    st.markdown(f"<div class='prank-box'>{st.session_state.prank_msg}</div>", unsafe_allow_html=True)

# Touch Buttons Layout (Fixed Grid)
buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "00", "="]
]

# Render Responsive Grid
for row in buttons:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        cols[i].button(btn, on_click=press, args=(btn,))
        
