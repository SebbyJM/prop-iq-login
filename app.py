import streamlit as st

st.set_page_config(page_title="Login", layout="centered")

# Hide Streamlit UI
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ------------------ UI ------------------ #
st.markdown("""
<style>

/* MAIN FONT */
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Manrope', sans-serif;
    background: linear-gradient(-45deg, #0f0f1a, #1a1033, #0f0f1a, #1a1033);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
    color: white;
}

/* BACKGROUND ANIMATION */
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* CENTER */
.block-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 90vh;
}

/* CARD */
.card {
    width: 360px;
    padding: 35px;
    border-radius: 20px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 0 50px rgba(139,92,246,0.15);
    text-align: center;
}

/* INPUT (ARIAL BOLD) */
.input {
    width: 100%;
    padding: 14px;
    margin-bottom: 15px;
    border-radius: 10px;
    border: none;
    outline: none;
    background: rgba(255,255,255,0.08);
    color: white;
    font-family: Arial, sans-serif;
    font-weight: bold;
    font-size: 14px;
}

/* PLACEHOLDER STYLE */
.input::placeholder {
    color: #d1d5db;
    font-weight: bold;
}

/* BUTTON */
.btn {
    width: 100%;
    padding: 13px;
    border-radius: 10px;
    border: none;
    background: linear-gradient(90deg, #7c3aed, #9333ea);
    color: white;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
}

.btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 8px 20px rgba(139,92,246,0.25);
}

/* PARTICLES */
.particle {
    position: fixed;
    width: 5px;
    height: 5px;
    background: rgba(139,92,246,0.35);
    border-radius: 50%;
    animation: float 10s linear infinite;
}

@keyframes float {
    0% { transform: translateY(100vh); opacity: 0; }
    20% { opacity: 1; }
    100% { transform: translateY(-10vh); opacity: 0; }
}

</style>

<!-- PARTICLES -->
<div class="particle" style="left:10%; animation-delay:0s;"></div>
<div class="particle" style="left:25%; animation-delay:2s;"></div>
<div class="particle" style="left:40%; animation-delay:4s;"></div>
<div class="particle" style="left:60%; animation-delay:1s;"></div>
<div class="particle" style="left:75%; animation-delay:3s;"></div>
<div class="particle" style="left:90%; animation-delay:5s;"></div>

<!-- LOGIN CARD -->
<div class="card">
    <input class="input" type="text" placeholder="Username">
    <input class="input" type="password" placeholder="Password">
    <button class="btn">Login</button>
</div>

""", unsafe_allow_html=True)
