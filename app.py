import streamlit as st
import random

st.set_page_config(page_title="Pro Calculator 🧮", page_icon="🧮", layout="centered")

# Custom Responsive Grid CSS (Full Mobile Support)
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
    }
    .main .block-container {
        max-width: 380px !important;
        padding: 1rem 10px !important;
        margin: 0 auto !important;
    }
    /* Input Display Box */
    div[data-baseweb="input"] input {
        font-size: 35px !important;
        text-align: right !important;
        color: #00ffcc !important;
        background-color: #1a1a1a !important;
        border-radius: 15px !important;
        height: 75px !important;
        padding-right: 15px !important;
        font-weight: bold;
    }
    
    /* 4 Column Fixed Responsive Grid */
    .calc-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 8px;
        margin-top: 15px;
    }
    
    /* Button Base Style */
    .calc-btn {
        width: 100%;
        height: 60px;
        font-size: 22px;
        font-weight: bold;
        border: none;
        border-radius: 50px;
        background-color: #2b2b2b;
        color: white;
        cursor: pointer;
    }
    .calc-btn:active {
        background-color: #444444;
    }
    .operator {
        background-color: #ff9500;
        color: white;
    }
    .top-btn {
        background-color: #a5a5a5;
        color: black;
    }
    
    /* Prank Box */
    .prank-box {
        background-color: #330000;
        color: #ff4d4d;
        padding: 12px;
        border-radius: 12px;
        border: 2px solid #ff4d4d;
        text-align: center;
        margin-top: 15px;
        font-size: 16px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Session States
if "display" not in st.session_state:
    st.session_state.display = ""
if "prank_msg" not in st.session_state:
    st.session_state.prank_msg = ""

# Query Params check for button clicks
query_params = st.query_params
if "btn" in query_params:
    val = query_params["btn"]
    st.query_params.clear()
    
    expr = st.session_state.display
    if val == "C":
        st.session_state.display = ""
        st.session_state.prank_msg = ""
    elif val == "back":
        st.session_state.display = expr[:-1]
    elif val == "=":
        funny_multiplication = ["Baap ka nokarr samjah", "I don't Know 999 🤐", "do it yourself! 🤣"]
        funny_division = ["Randi ke bache khud krr le", "You are duffer! 🤦‍♂️", "Abe khud bhi krr le kuch! 😂"]
        funny_subtraction = ["Kathu se gand marwata tha kya 10th mai", "Kathu ko bulau? 👻", "Ya maths wale sir ko? 👨‍🏫"]
        funny_addition = ["Mc add bhi nhi krr para', "Abe Add krrna bhi nhi ara kya?", "Itna simple plus khud kar le bhai! 😜"]
        funny_errors = ["Ak kaam krr land chus mera", "Abe ulta paida hua tha kya? 🤪", "Error 404: Calculator Is Busy! 🤖"]
        
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
st.markdown("<h3 style='text-align: center; color: white;'>Pro Calculator 🧮</h3>", unsafe_allow_html=True)

# Display Screen
disp = st.session_state.display if st.session_state.display != "" else "0"
st.text_input("", value=disp, disabled=True, label_visibility="collapsed")

# Prank Message
if st.session_state.prank_msg:
    st.markdown(f"<div class='prank-box'>{st.session_state.prank_msg}</div>", unsafe_allow_html=True)

# HTML Grid UI (100% Mobile Safe)
grid_html = """
<div class="calc-grid">
    <a href="?btn=C" target="_self"><button class="calc-btn top-btn">C</button></a>
    <a href="?btn=back" target="_self"><button class="calc-btn top-btn">⌫</button></a>
    <a href="?btn=%" target="_self"><button class="calc-btn top-btn">%</button></a>
    <a href="?btn=/" target="_self"><button class="calc-btn operator">/</button></a>
    
    <a href="?btn=7" target="_self"><button class="calc-btn">7</button></a>
    <a href="?btn=8" target="_self"><button class="calc-btn">8</button></a>
    <a href="?btn=9" target="_self"><button class="calc-btn">9</button></a>
    <a href="?btn=*" target="_self"><button class="calc-btn operator">×</button></a>
    
    <a href="?btn=4" target="_self"><button class="calc-btn">4</button></a>
    <a href="?btn=5" target="_self"><button class="calc-btn">5</button></a>
    <a href="?btn=6" target="_self"><button class="calc-btn">6</button></a>
    <a href="?btn=-" target="_self"><button class="calc-btn operator">-</button></a>
    
    <a href="?btn=1" target="_self"><button class="calc-btn">1</button></a>
    <a href="?btn=2" target="_self"><button class="calc-btn">2</button></a>
    <a href="?btn=3" target="_self"><button class="calc-btn">3</button></a>
    <a href="?btn=+" target="_self"><button class="calc-btn operator">+</button></a>
    
    <a href="?btn=0" target="_self"><button class="calc-btn">0</button></a>
    <a href="?btn=." target="_self"><button class="calc-btn">.</button></a>
    <a href="?btn=00" target="_self"><button class="calc-btn">00</button></a>
    <a href="?btn==" target="_self"><button class="calc-btn operator">=</button></a>
</div>
"""
st.markdown(grid_html, unsafe_allow_html=True)
