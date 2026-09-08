import streamlit as st
import streamlit.components.v1 as components
import random

st.set_page_config(page_title="Pro Calculator", page_icon="🧮", layout="centered")

# Hide Streamlit elements to fit whole screen without scrolling
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {
        padding: 0px !important;
        max-width: 100% !important;
    }
    .stApp {
        background-color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

# Aapke Exact Funny Dialogues
funny_multiplication = ["Naveen ka chusta lele"]
funny_division = ["Naveen ki nalayak santan division to seekh le"]
funny_subtraction = ["Kathu se gand marwata tha kya 10th mai"]
funny_addition = ["Mc add bhi nhi krr para dimag mai gu bhara h kya"]
funny_errors = ["Bio wala h na to maths walo ka chusta lele"]

# Dialogues convert for JavaScript Injection
msg_mult = random.choice(funny_multiplication)
msg_div = random.choice(funny_division)
msg_sub = random.choice(funny_subtraction)
msg_add = random.choice(funny_addition)
msg_err = random.choice(funny_errors)

calc_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<style>
    * {{
        box-sizing: border-box;
        user-select: none;
        -webkit-user-select: none;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}
    body {{
        background-color: #000000;
        margin: 0;
        padding: 10px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
        overflow: hidden;
    }}
    .calc-container {{
        width: 100%;
        max-width: 350px;
    }}
    #display {{
        width: 100%;
        height: 65px;
        background-color: #1a1a1a;
        color: #00ffcc;
        font-size: 32px;
        text-align: right;
        border: none;
        border-radius: 12px;
        padding: 10px 15px;
        outline: none;
        margin-bottom: 8px;
        font-weight: bold;
    }}
    #prank-box {{
        background-color: #330000;
        color: #ff4d4d;
        padding: 8px;
        border-radius: 10px;
        border: 1.5px solid #ff4d4d;
        text-align: center;
        font-size: 14px;
        font-weight: bold;
        min-height: 40px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        visibility: hidden;
    }}
    .grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 8px;
    }}
    .btn {{
        height: 58px;
        border-radius: 50px;
        border: none;
        background-color: #2b2b2b;
        color: white;
        font-size: 20px;
        font-weight: bold;
        outline: none;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    .btn:active {{
        background-color: #444444;
    }}
    .btn.top {{
        background-color: #a5a5a5;
        color: black;
    }}
    .btn.op {{
        background-color: #ff9500;
        color: white;
    }}
</style>
</head>
<body>

<div class="calc-container">
    <input type="text" id="display" value="0" readonly>
    <div id="prank-box"></div>
    
    <div class="grid">
        <button class="btn top" onclick="press('C')">C</button>
        <button class="btn top" onclick="press('⌫')">⌫</button>
        <button class="btn top" onclick="press('%')">%</button>
        <button class="btn op" onclick="press('/')">÷</button>
        
        <button class="btn" onclick="press('7')">7</button>
        <button class="btn" onclick="press('8')">8</button>
        <button class="btn" onclick="press('9')">9</button>
        <button class="btn op" onclick="press('*')">×</button>
        
        <button class="btn" onclick="press('4')">4</button>
        <button class="btn" onclick="press('5')">5</button>
        <button class="btn" onclick="press('6')">6</button>
        <button class="btn op" onclick="press('-')">-</button>
        
        <button class="btn" onclick="press('1')">1</button>
        <button class="btn" onclick="press('2')">2</button>
        <button class="btn" onclick="press('3')">3</button>
        <button class="btn op" onclick="press('+')">+</button>
        
        <button class="btn" onclick="press('0')">0</button>
        <button class="btn" onclick="press('.')">.</button>
        <button class="btn" onclick="press('00')">00</button>
        <button class="btn op" onclick="press('=')">=</button>
    </div>
</div>

<script>
    let expr = "";
    const disp = document.getElementById('display');
    const prank = document.getElementById('prank-box');

    function press(val) {{
        if (val === 'C') {{
            expr = "";
            disp.value = "0";
            prank.style.visibility = "hidden";
            prank.innerText = "";
        }} else if (val === '⌫') {{
            expr = expr.slice(0, -1);
            disp.value = expr || "0";
        }} else if (val === '=') {{
            if (expr.includes('*')) prank.innerText = "{msg_mult}";
            else if (expr.includes('/')) prank.innerText = "{msg_div}";
            else if (expr.includes('-')) prank.innerText = "{msg_sub}";
            else if (expr.includes('+')) prank.innerText = "{msg_add}";
            else prank.innerText = "{msg_err}";
            
            prank.style.visibility = "visible";
            disp.value = "Error 404";
            expr = "";
        }} else {{
            if (disp.value === "Error 404") {{
                disp.value = "";
            }}
            expr += val;
            disp.value = expr;
        }}
    }}
</script>

</body>
</html>
"""

components.html(calc_html, height=500)
